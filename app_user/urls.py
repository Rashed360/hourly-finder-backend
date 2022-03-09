from .views import SeekerProfileViewSet,RecruiterProfileViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path
from app_user.views import activate,password_reset

router = DefaultRouter()
router.register(r'seeker', SeekerProfileViewSet, basename='seeker')
router.register(r'recruiter', RecruiterProfileViewSet, basename='recruiter')

urlpatterns = [
    path('activate/<uid>/<token>', activate, name='activate'),
    path('password-reset/<uid>/<token>', password_reset, name='password-reset'),
]

urlpatterns += router.urls
