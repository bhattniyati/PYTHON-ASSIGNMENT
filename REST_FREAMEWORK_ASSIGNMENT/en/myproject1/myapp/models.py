# Create your models here.
from django.db import models

# create a class name of Book 
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    publisher = models.CharField(max_length=100)

    # this method show in admin panel 
    def __str__(self):
        return self.author