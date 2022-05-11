from django.urls import path
from .views import SingleJobAPIView,SingleJobCreateAPIView,JobListAPIView, JobTypeViewSet,CompanyViewSet,ApplicationViewSet,AllJobListAPIView,JobViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'job', JobViewSet, basename='job')
router.register(r'type', JobTypeViewSet, basename='jobType')
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'apply', ApplicationViewSet, basename='apply')

urlpatterns = [
    path('', JobListAPIView.as_view()),
    path('single/<slug:slug>', SingleJobAPIView.as_view()),
    path('create/', SingleJobCreateAPIView.as_view()),
    path('all/', AllJobListAPIView.as_view()),
]

urlpatterns += router.urls