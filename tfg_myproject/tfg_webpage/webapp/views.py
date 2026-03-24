from django.shortcuts import render
from .models import Storygraph_Book
from .serializers import BookDBSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

class BooksDB(viewsets.ReadOnlyModelViewSet):
# supports list and retrieve pk
# maybe it will be more useful to do a generic view set and define the methods on our own, since they may be more complex
    queryset = Storygraph_Book.objects.all()
    serializer_class = BookDBSerializer