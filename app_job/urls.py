from .views import JobViewSet,JobTypeViewSet,CompanyViewSet,ApplicationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'job', JobViewSet, basename='job')
router.register(r'type', JobTypeViewSet, basename='jobType')
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'apply', ApplicationViewSet, basename='apply')

urlpatterns = []

urlpatterns += router.urls