import json
from django.core import serializers
from .models import Storygraph_Book
from .serializers import BookDBSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from .scripts.storygraph_scraper import book_search, book_info, add_weights_to_book
from rest_framework.response import Response

class BooksDB(viewsets.ReadOnlyModelViewSet):
# supports list and retrieve pk
# maybe it will be more useful to do a generic view set and define the methods on our own, since they may be more complex
    queryset = Storygraph_Book.objects.all()
    serializer_class = BookDBSerializer

class GetBookByISBNorUID(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        # get request with isbn/uid param
        print(pk)
        book = Storygraph_Book.objects.filter(isbn_uid=pk)
        book = serializers.serialize('json', book)
        book = json.loads(book)
        # print(book[0])
        return Response(book[0]['fields'])


class StorygraphSearch(viewsets.ViewSet):
# accesses StoryGraph to retrieve a certain book
    def create(self, request):
        # post request with search query in body
        b = json.loads(request.body.decode("utf-8"))
        # print(b)
        id = book_search([b['searchItem']])
        # print(id)
        book = book_info(id)
        book = add_weights_to_book(book)
        # print(book)
        return Response(book)


        
