import json
from django.shortcuts import render
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

class StorygraphSearch(viewsets.ViewSet):
    def create(self, request):
        b = json.loads(request.body.decode("utf-8"))
        # print(b)
        id = book_search([b['searchItem']])
        # print(id)
        book = book_info(id)
        book = add_weights_to_book(book)
        # print(book)
        return Response(book)


        
