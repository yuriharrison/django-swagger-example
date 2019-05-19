from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    lookup_field = 'slug'


class BookViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'slug'
