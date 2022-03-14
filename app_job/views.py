from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Job,JobType,Company,Application
from .serializers import JobSerializer,JobTypeSerializer,CompanySerializer,ApplicationSerializer


class JobViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = Job.objects.all()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(user__id=id)
        return queryset

class JobTypeViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = JobTypeSerializer

    def get_queryset(self):
        queryset = JobType.objects.all()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(user__id=id)
        return queryset

class CompanyViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = CompanySerializer

    def get_queryset(self):
        queryset = Company.objects.all()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(user__id=id)
        return queryset

class ApplicationViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        queryset = Application.objects.all()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(job_id=id)
        return queryset
