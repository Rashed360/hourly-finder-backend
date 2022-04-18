from django.urls import path

from .views import AllBlogListAPIView

urlpatterns = [
    path('', AllBlogListAPIView.as_view()),

]
