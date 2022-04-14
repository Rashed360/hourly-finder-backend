from asyncio.windows_events import NULL
from app_auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import SeekerProfile,RecruiterProfile
from .serializers import SeekerProfileSerializer,RecruiterProfileSerializer,RecruiterProfileUpdateSerializer,SeekerProfileUpdateSerializer
from django.shortcuts import redirect
from decouple import config


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

#---Update-Profile
class ProfileUpdateAPIView(APIView):
    permission_classes = []
    def patch(self, request, id):
        user = User.objects.get(id=id)
        if user.user_type == 1:
            filters = {}
            filters['user'] = User.objects.get(id=id)
            filters['recruiter'] = RecruiterProfile.objects.get(user=user)
            serializer = RecruiterProfileUpdateSerializer(filters)
            return Response(serializer.data)
        elif user.user_type == 2:
            filters = {}
            filters['user'] = User.objects.get(id=id)
            filters['seeker'] = SeekerProfile.objects.get(user=user)
            serializer = SeekerProfileUpdateSerializer(filters)
            return Response(serializer.data)         


#---Redirect Views
def activate(request,uid,token):
    return redirect(f"{config('FRONT_END_SERVER')}/activate/{uid}/{token}")

def password_reset(request,uid,token):
    return redirect(f"{config('FRONT_END_SERVER')}/password-reset/{uid}/{token}")