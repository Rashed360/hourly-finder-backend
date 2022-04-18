from dataclasses import fields

from rest_framework.serializers import ModelSerializer

from .models import Blog


class BlogSerializers(ModelSerializer):
    class Meta:
        model = Blog
        exclude = ['status']
