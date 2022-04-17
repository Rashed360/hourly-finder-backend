from rest_framework.parsers import FormParser,MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from app_auth.models import User
from app_user.models import RecruiterProfile
from .models import Job,JobType,Company,Application
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .serializers import CombinedSerializer,JobSerializer,JobTypeSerializer,CompanySerializer,ApplicationSerializer, AllJobSerializer, JobInfoSerializer, CompanyViewSerializer

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 12

class JobListAPIView(ListAPIView):
    permission_classes = []
    serializer_class = JobInfoSerializer

    def get_queryset(self):
        queryset = Job.objects.all()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(recruiter=id)
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

    def get_queryset(self):
        queryset = Company.objects.all()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(recruiter=id)
        return queryset
    
    def get_serializer_class(self):
        id = self.request.query_params.get('id',None)
        if id is not None:
            return CompanyViewSerializer
        return CompanySerializer

class ApplicationViewSet(ModelViewSet):
    permission_classes = []
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        queryset = Application.objects.all()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(job_id=id)
        return queryset

#---Single-Job-View
class SingleJobAPIView(APIView):
    permission_classes = []
    def get(self, request, slug):
        job = Job.objects.get(slug=slug)
        recruiter = RecruiterProfile.objects.get(id=job.recruiter.id)
        filters = {}
        filters['job'] = Job.objects.get(slug=slug)
        filters['recruiter'] = RecruiterProfile.objects.get(id=job.recruiter.id)
        filters['company'] = Company.objects.get(id=job.company.id)
        filters['user'] = User.objects.get(id=recruiter.user.id)
        serializer = CombinedSerializer(filters)
        return Response(serializer.data)

#---Single-Job-Create
class SingleJobCreateAPIView(CreateAPIView):
    permission_classes = []
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    parser_classes = [FormParser,MultiPartParser]

#---All-Job-Custom-View
class AllJobListAPIView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Job.objects.all()
    serializer_class = AllJobSerializer
    pagination_class = CustomPageNumberPagination