from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blog
from .serializers import BlogSerializers


# Create your views here.
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 12

#---All-Blog-Custom-View
class AllBlogListAPIView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    pagination_class = CustomPageNumberPagination

#---Single-Blog--View
class SingleBlogAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = 'slug'
