from rest_framework.serializers import ModelSerializer
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

class CompanySerial(ModelSerializer):
    class Meta:
        model = Company
        fields = ('logo','name','location')
class AllJobSerializer(ModelSerializer):
    company = CompanySerial()
    class Meta:
        model = Job
        fields = ('title','type','keyword','created','company')
        read_only_fields = ('created',)