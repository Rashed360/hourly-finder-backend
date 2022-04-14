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


# class RecruiterProfileUpdateSerializer(ModelSerializer):
#     class RecruiterSerial(ModelSerializer):
#         class Meta:
#             model = RecruiterProfile
#             fields = ('dob','phone')
#     recruiter = RecruiterSerial()

#     class Meta:
#         model = User
#         fields = ('first_name','last_name')

#     def update(self, validated_data):
#         profile_data = validated_data.pop('recruiter')
#         user = User.objects.update(
#             first_name=validated_data["first_name"],
#             last_name=validated_data["last_name"]
#         )
#         RecruiterProfile.objects.update(
#             dob=profile_data.get('dob'),
#             phone=profile_data.get('phone')
#         )
#         return user
        
# class SeekerProfileUpdateSerializer(ModelSerializer):
#     class SeekerSerial(ModelSerializer):
#         class Meta:
#             model = SeekerProfile
#             fields = ('dob','phone')
#     seeker = SeekerSerial()

#     class Meta:
#         model = User
#         fields = ('first_name','last_name')

#     def update(self, validated_data):
#         profile_data = validated_data.pop('seeker')
#         user = User.objects.update(
#             first_name=validated_data["first_name"],
#             last_name=validated_data["last_name"]
#         )
#         SeekerProfile.objects.update(
#             dob=profile_data.get('dob'),
#             phone=profile_data.get('phone')
#         )
#         return user