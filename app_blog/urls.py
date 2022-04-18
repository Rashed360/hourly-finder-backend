from django.urls import path

from .views import AllBlogListAPIView, SingleBlogAPIView

urlpatterns = [
    path('', AllBlogListAPIView.as_view()),
    path('<slug>', SingleBlogAPIView.as_view()),

]
