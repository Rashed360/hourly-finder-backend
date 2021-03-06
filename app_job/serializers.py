from rest_framework.serializers import ModelSerializer,Serializer
from app_auth.models import User
from app_user.models import RecruiterProfile, SeekerProfile
from .models import Job,JobType,Company,Application, Offer, Work


class JobTypeSerializer(ModelSerializer):
    class Meta:
        model = JobType
        fields = '__all__'


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyViewSerializer(ModelSerializer):
    class Meta:
        model = Company
        exclude = ('id','recruiter')

class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = "__all__"

class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"

class WorkViewSerializer(ModelSerializer):
    class JobSerial(ModelSerializer):
        class Meta:
            model = Job
            fields = ('title','location','type')
    class SeekerSerializer(ModelSerializer):
        class UserSerial(ModelSerializer):
            class Meta:
                model = User
                fields = ('username','first_name','last_name')
        user = UserSerial()
        class Meta:
            model = SeekerProfile
            fields = ('picture','expertise','user')
    job = JobSerial()
    seeker = SeekerSerializer()
    class Meta:
        model = Work
        fields = "__all__"

class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class JobInfoSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = ('title','starting','type','slug','location','status')


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"

class ApplicationViewSerializer(ModelSerializer):
    class SeekerSerializer(ModelSerializer):
        class UserSerial(ModelSerializer):
            class Meta:
                model = User
                fields = ('username','first_name','last_name')
        user = UserSerial()
        class Meta:
            model = SeekerProfile
            fields = ('picture','expertise','user')
    seeker = SeekerSerializer()
    class Meta:
        model = Application
        fields = ('id','message','status','seeker')

class ApplicationSeekerViewSerializer(ModelSerializer):
    class JobSerializer(ModelSerializer):
        class Meta:
            model = Job
            fields = ('title','location','type','starting')
    job = JobSerializer()
    class Meta:
        model = Application
        fields = ('id','status','job')


class CombinedSerializer(Serializer):
    class JobSerial(ModelSerializer):
        class Meta:
            model = Job
            exclude = ['company','recruiter']
    class RecruiterProfileSerial(ModelSerializer):
        class Meta:
            model = RecruiterProfile
            exclude = ['id','user','dob','identity']
    class CompanySerial(ModelSerializer):
        class Meta:
            model = Company
            exclude = ['id','recruiter']
    class UserSerial(ModelSerializer):
        class Meta:
            model = User
            fields = ('email','username','first_name','last_name')
    job = JobSerial(read_only=True)
    recruiter = RecruiterProfileSerial(read_only=True)
    company = CompanySerial(read_only=True)
    user = UserSerial(read_only=True)



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