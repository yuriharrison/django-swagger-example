from rest_framework import serializers

from . import models


class AuthorSerializer(serializers.ModelSerializer):

    _id = serializers.HyperlinkedIdentityField(
        view_name='api:author-detail',
        lookup_field='slug'
    )
    # books = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     view_name='api:author-books-detail',
    #     queryset=models.Book.objects.all(),
    #     lookup_field='id',
    # )
    books = serializers.SlugRelatedField(
        slug_field='slug',
        many=True,
        queryset=models.Book.objects.all()
    )

    class Meta:
        model = models.Author
        fields = ('_id', 'full_name', 'first_name', 'last_name', 'age', 'books')


class BookSerializer(serializers.ModelSerializer):
    _id = serializers.HyperlinkedIdentityField(
        view_name='api:book-detail',
        lookup_field='slug'
    )
    # authors = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     view_name='api:author-detail',
    #     queryset=models.Author.objects.all(),
    #     lookup_field='slug',
    # )

    class Meta:
        model = models.Book
        fields = ('_id', 'title', 'description', 'slug', 'authors')
