from django.shortcuts import render
from rest_framework import generics
from library.models import Book
from library.serializers import BookSerializer

# Create your views here.

class BookList(generics.ListCreateAPIView):
   queryset = Book.objects.all()
   
   serializer_class = BookSerializer

class BookDeatail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Book
   serializer_class = BookSerializer
