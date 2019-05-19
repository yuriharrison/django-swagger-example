from django.db import models
from django_extensions.db import fields as extension_fields


class Author(models.Model):
    first_name = models.CharField(max_length=60, blank=False)
    last_name = models.CharField(max_length=60, blank=False)
    age = models.IntegerField()
    slug = extension_fields.AutoSlugField(
        populate_from='full_name',
        blank=True,
        null=False,
        unique=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=500, blank=True)
    slug = extension_fields.AutoSlugField(
        populate_from='title',
        blank=True,
        null=False,
        unique=True,
    )

    authors = models.ManyToManyField(Author, related_name='books')
