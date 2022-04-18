from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.views.generic.base import RedirectView

from .views import getRoutes

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('', getRoutes),
    path('admin/', admin.site.urls),
    path('auth/', include('app_auth.urls')),
    path('user/', include('app_user.urls')),
    path('jobs/', include('app_job.urls')),
    path('contact/', include('app_contact.urls')),
    path('blogs/', include('app_blog.urls')),
    re_path(r'^favicon\.ico$', favicon_view),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
