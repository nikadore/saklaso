from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book
from rest_framework import ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericAPIView, IsAuthenticated


class FavoriteProductViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)