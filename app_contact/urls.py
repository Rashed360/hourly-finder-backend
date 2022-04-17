from django.urls import path

from .views import ContactCreateAPIView

urlpatterns = [
    path('create', ContactCreateAPIView.as_view()),
]
