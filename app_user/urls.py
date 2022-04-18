from .views import SeekerProfileViewSet,RecruiterProfileViewSet,PublicProfileView,AvailableSeekerView
from rest_framework.routers import DefaultRouter
from django.urls import path


router = DefaultRouter()
router.register(r'seeker', SeekerProfileViewSet, basename='seeker')
router.register(r'recruiter', RecruiterProfileViewSet, basename='recruiter')

urlpatterns = [
    path('profile/<str:username>', PublicProfileView.as_view(), name='profile-view'),
    path('available/', AvailableSeekerView.as_view(), name='available-seeker'),
]

urlpatterns += router.urls
