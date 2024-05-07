# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# this class using for add data
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# this class using for update and delete data 
class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    