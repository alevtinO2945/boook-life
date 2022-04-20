import time

import django.contrib.auth.models
from django.db import models
from PIL import Image
from django.contrib.auth.models import User
import datetime

class Book(models.Model):
    name = models.TextField(max_length=150)
    author = models.CharField(max_length=150, default="Undefined")
    descr = models.CharField(max_length=600, default=None)
    price = models.FloatField(null=True, blank=True)
    book_available = models.BooleanField(default=False)

    image = models.ImageField(default='default_book.jpg', upload_to='book_images')

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Book, max_length=100, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', unique=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    text = models.TextField(max_length=1500)
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=True)


    def __str__(self):
        return self.text
