from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import SeekerProfile,RecruiterProfile
from .serializers import SeekerProfileSerializer,RecruiterProfileSerializer
from django.shortcuts import redirect


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


# Redirect Views
def activate(request,uid,token):
    return redirect(f"http://127.0.0.1:3000/activate/{uid}/{token}")

def password_reset(request,uid,token):
    return redirect(f"http://127.0.0.1:3000/password-reset/{uid}/{token}")