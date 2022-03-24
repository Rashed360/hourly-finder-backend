from rest_framework.serializers import ModelSerializer,Serializer
from app_auth.models import User
from app_auth.serializers import UserSerializer
from app_user.models import RecruiterProfile
from app_user.serializers import RecruiterProfileSerializer
from .models import Job,JobType,Company,Application


class JobTypeSerializer(ModelSerializer):
    class Meta:
        model = JobType
        fields = '__all__'


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"


class CombinedSerializer(Serializer):
    job = JobSerializer(read_only=True)
    recruiter = RecruiterProfileSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    user = UserSerializer(read_only=True)



class AllJobSerializer(ModelSerializer):
    class CompanySerial(ModelSerializer):
        class Meta:
            model = Company
            fields = ('logo','name','location')
    company = CompanySerial()
    class RecruiterSerial(ModelSerializer):
        class UserSerial(ModelSerializer):
            class Meta:
                model = User
                fields = ('username',)
        user = UserSerial()
        class Meta:
            model = RecruiterProfile
            fields = ('user',)
    recruiter = RecruiterSerial()
    
    class Meta:
        model = Job
        fields = ('title','slug','type','keyword','created','company','recruiter')
        read_only_fields = ('created',)