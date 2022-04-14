from dataclasses import fields
from app_auth.models import User
from .models import RecruiterProfile
from rest_framework.serializers import Serializer,ModelSerializer
from .models import SeekerProfile, RecruiterProfile

class SeekerProfileSerializer(ModelSerializer):
    class Meta:
        model = SeekerProfile
        fields = '__all__'

class RecruiterProfileSerializer(ModelSerializer):
    class Meta:
        model = RecruiterProfile
        fields = '__all__'

class RecruiterProfileUpdateSerializer(Serializer):
    class UserSerial(ModelSerializer):
        class Meta:
            model = User
            fields = ('first_name','last_name')
    class RecruiterSerial(ModelSerializer):
        class Meta:
            model = RecruiterProfile
            fields = ('dob','phone')
    user = UserSerial()
    recruiter = RecruiterSerial()

class SeekerProfileUpdateSerializer(Serializer):
    class UserSerial(ModelSerializer):
        class Meta:
            model = User
            fields = ('first_name','last_name')
    class SeekerSerial(ModelSerializer):
        class Meta:
            model = SeekerProfile
            fields = ('dob','phone')
    user = UserSerial()
    recruiter = SeekerSerial()