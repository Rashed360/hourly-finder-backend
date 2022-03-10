from .views import JobViewSet,JobTypeViewSet,CompanyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'job', JobViewSet, basename='job')
router.register(r'type', JobTypeViewSet, basename='jobType')
router.register(r'company', CompanyViewSet, basename='company')

urlpatterns = []

urlpatterns += router.urls