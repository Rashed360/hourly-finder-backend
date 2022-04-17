from django.core.mail import EmailMultiAlternatives, send_mail
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
    from_email = data['email']
    recipient = ['info.hourlyfinder@gmail.com']
    send_mail(subject, message, from_email, recipient, fail_silently=True)

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
def newsletter_mail(data):
    subject = 'Thanks for HourlyFinder Newsletter Subscription.'
    text_content = 'Subscription Notification'
    from_email = 'info.hourlyfinder@gmail.com'
    to = data['email']
    html_content = '<p>Dear User, Thanks for being with us.You will get notification of latest update of our website. <strong>-Team HourlyFinder</strong></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

class NewsletterCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        newsletter_mail(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
