from dataclasses import fields

from rest_framework.serializers import ModelSerializer

from .models import Blog


class AllBlogSerializers(ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'slug', 'description', 'thumbnail', 'author', 'keyword', 'published_date']

class SingleBlogSerializers(ModelSerializer):
    class Meta:
        model = Blog
        exclude = ['status']
