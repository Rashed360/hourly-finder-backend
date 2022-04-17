from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Contact, Newsletter
from .serializers import ContactSerializer, NewsletterSerializer

# Create your views here.

def send_email(data):
    subject = data['subject']
    body = {
        'Name' : "Name : " +data['first_name'] + " " + data['last_name'],
        'Phone' : "Phone : " + data['phone'],
        'Profile' : "Profile Name : " + data['profile'],
        'Message' : "Query : " + data['message']
    }

    message = '\n'.join(body.values())
    sender = data['email']
    recipient = ['info.hourlyfinder@gmail.com']
    send_mail(subject, message, sender, recipient, fail_silently=True)

# Contact Us
class ContactCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        send_email(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Newsletter 

