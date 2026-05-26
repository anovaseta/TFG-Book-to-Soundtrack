import json
import io
from django.core import serializers
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from .models import Storygraph_Book, Storygraph_Tag, Synonym, Synonym_Relation
from .serializers import BookDBSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from .scripts.storygraph_scraper import book_search, book_info, add_weights_to_book
from .scripts.get_track_pool import get_track_pool
from rest_framework.response import Response


class BooksDB(viewsets.ReadOnlyModelViewSet):
# supports list and retrieve pk
# maybe it will be more useful to do a generic view set and define the methods on our own, since they may be more complex
    queryset = Storygraph_Book.objects.all().order_by('authors').values()
    serializer_class = BookDBSerializer

class GetBookByISBNorUID(viewsets.ViewSet):
# has online and offline mode
    def create(self, request):
        # get request with isbn/uid param
        # print(pk)
        b = json.loads(request.body)
        print(b)
        if b['mode'] == 'offline':
            book = Storygraph_Book.objects.filter(isbn_uid=b['book_id'])
            book = serializers.serialize('json', book)
            book = json.loads(book)
            # print(book[0])
            return Response(book[0]['fields'])
        elif b['mode'] == 'online':
            print('online')
            id = book_search([b['book_id']])
            book = book_info(id)
            book = add_weights_to_book(book)
            return Response(book)


class StorygraphSearch(viewsets.ViewSet):
# accesses StoryGraph to retrieve a certain book
    def create(self, request):
        # post request with search query in body
        b = json.loads(request.body.decode("utf-8"))
        print(b)
        id = book_search([b['searchItem']])
        print(id)
        book = book_info(id)
        if book == None:
            return Response('error')
        book = add_weights_to_book(book)
        # print(book)
        return Response(book)
    
class getTagSynonyms(viewsets.ViewSet):
# retrieve the list of synonyms associated to a StoryGraph tag
    def retrieve(self, request, pk=None):
        # print(pk)
        tag = Storygraph_Tag.objects.get(tag_name=pk)
        # print(tag)
        query_list = Synonym_Relation.objects.filter(tag_id=tag.id)
        # print(query_list)
        syn_list = []
        for s in query_list:
            syn_list.append((Synonym.objects.get(id=s.synonym_id).synonym, s.affinity)) # (synonym, affinity)
        # print(syn_list)
        syn_dict = {pk:{'strongest':[], 'strong': [], 'weak': []}}
        for s in syn_list:
            syn_dict[pk][s[1]].append(s[0])
        # print(syn_dict)
        # book = serializers.serialize('json', book)
        # book = json.loads(book)
        return Response(syn_dict)
    
class getTrackPool(viewsets.ViewSet):
# has offline and online mode
    def create(self, request):
        # receives the book, returns the track pool
        b = json.loads(request.body.decode("utf-8"))

        # gather the book either offline (from db) or online (from scraping)
        if b['mode'] == 'offline':
            book = Storygraph_Book.objects.filter(isbn_uid=b['book_id'])
            book = serializers.serialize('json', book)
            book = json.loads(book)
            book = book[0]['fields']
        elif b['mode'] == 'online':
            print('online')
            id = book_search([b['book_id']])
            book = book_info(id)
            book = add_weights_to_book(book)
        # print(book)

        return Response(get_track_pool(book, b['n_tracks']))


class exportToPDF(viewsets.ViewSet):
# has offline and online mode
    def create(self, request):
        # get request with isbn/uid param
        # print(pk)
        b = json.loads(request.body)
        print(b)
        if b['mode'] == 'offline':
            book = Storygraph_Book.objects.filter(isbn_uid=b['book_id'])
            book = serializers.serialize('json', book)
            book = json.loads(book)
            tag_weights = book[0]['fields']['tag_weights']
            # print(tag_weights)
            book[0]['fields']['synonyms'] = {}
            for t in tag_weights:
                tt = t[0]
                tag = Storygraph_Tag.objects.get(tag_name=tt)
                # print(tag)
                query_list = Synonym_Relation.objects.filter(tag_id=tag.id)
                # print(query_list)
                syn_list = []
                for s in query_list:
                    syn_list.append((Synonym.objects.get(id=s.synonym_id).synonym, s.affinity)) # (synonym, affinity)
                # print(syn_list)
                syn_dict = {'strongest':[], 'strong': [], 'weak': []}
                for s in syn_list:
                    syn_dict[s[1]].append(s[0])
                # print(syn_dict)
                book[0]['fields']['synonyms'][tt] = syn_dict
            return Response(book[0]['fields'])
        elif b['mode'] == 'online':
            # print('online')
            # id = book_search([b['book_id']])
            # book = book_info(id)
            # book = add_weights_to_book(book)
            # return Response(book)
            return Response({})
