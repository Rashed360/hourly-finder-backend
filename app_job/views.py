from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.pagination import PageNumberPagination
from .models import Job,JobType,Company,Application
from .serializers import JobSerializer,JobTypeSerializer,CompanySerializer,ApplicationSerializer,AllJobSerializer

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10

class AllJobListAPIView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Job.objects.all()
    serializer_class = AllJobSerializer


class JobViewSet(ModelViewSet):
    serializer_class = JobSerializer
    authentication_classes = []
    permission_classes = []
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = Job.objects.all()
        slug = self.request.query_params.get('slug',None)
        if slug is not None:
            queryset = queryset.filter(slug=slug)
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
    permission_classes = [IsAuthenticated,]
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
