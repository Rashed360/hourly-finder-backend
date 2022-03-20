from django.contrib import admin
from .models import User

admin.site.register(User)
admin.site.site_header = 'Hourly-Finder : Administration'