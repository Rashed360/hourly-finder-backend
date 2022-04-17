from django.urls import path

from .views import ContactCreateAPIView, NewsletterCreateAPIView

urlpatterns = [
    path('create', ContactCreateAPIView.as_view()),
    path('newsletter', NewsletterCreateAPIView.as_view()),
]
