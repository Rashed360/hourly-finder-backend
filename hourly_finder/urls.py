from django.contrib import admin
from .views import getRoutes
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', getRoutes),
    path('admin/', admin.site.urls),
    path('auth/', include('app_auth.urls')),
    path('user/', include('app_user.urls')),
    path('jobs/', include('app_job.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)