from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorListCreateAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        """List all authors"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Create new author"""
        return self.create(request, *args, **kwargs)



class BookListCreateAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        """List all books"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Create new book"""
        return self.create(request, *args, **kwargs)


class BookDeleteAPIView(GenericAPIView, DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"

    def delete(self, request, *args, **kwargs):
        """Delete a book"""
        return self.destroy(request, *args, **kwargs)