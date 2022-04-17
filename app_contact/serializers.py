from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from .models import Contact, Newsletter


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class NewsletterSerializer(ModelSerializer):
    class Meta:
        model = Newsletter
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Newsletter.objects.all(),
                fields=['email']
            )
        ]
