from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from app_auth.models import User
from .models import SeekerProfile,RecruiterProfile
from .serializers import SeekerProfileSerializer,RecruiterProfileSerializer,PublicRecruiterProfileSerializer


class SeekerProfileViewSet(ModelViewSet):
    permission_classes = [ ]
    serializer_class = SeekerProfileSerializer

    def get_queryset(self):
        queryset = SeekerProfile.objects.all()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(user=id)
        return queryset

class RecruiterProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = RecruiterProfileSerializer

    def get_queryset(self):
        queryset = RecruiterProfile.objects.all()
        id = self.request.query_params.get('id',None)
        if id is not None:
            queryset = queryset.filter(user=id)
        return queryset

class PublicProfileView(APIView):
    permission_classes = []
    def get(self, request, username):
        user = User.objects.get(username=username)
        filters = {}
        # filters['job'] = Job.objects.get(slug=slug)
        filters['recruiter'] = RecruiterProfile.objects.get(user=user)
        # filters['company'] = Company.objects.get(id=job.company.id)
        filters['user'] = User.objects.get(username=username)
        serializer = PublicRecruiterProfileSerializer(filters)
        return Response(serializer.data)