from .views import SeekerProfileViewSet,RecruiterProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'seeker', SeekerProfileViewSet, basename='seeker')
router.register(r'recruiter', RecruiterProfileViewSet, basename='recruiter')

urlpatterns = []

urlpatterns += router.urls
