# Generated by Django 2.2.1 on 2019-05-19 12:44

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='full_name')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('authors', models.ManyToManyField(related_name='books', to='api.Author')),
            ],
        ),
    ]
