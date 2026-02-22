from django.db import models

class Author(models.Model):
    name = models.CharField()
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField()
    description = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    published_at = models.DateTimeField()


