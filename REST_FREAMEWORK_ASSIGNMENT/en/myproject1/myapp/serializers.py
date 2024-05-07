# Importing serializers module from Django REST framework
from rest_framework import serializers

# importing Book model
from .models import Book

# Defining a serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # specifying the fields
        fields = ['id', 'title', 'author', 'isbn', 'publisher'] 