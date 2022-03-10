from django.contrib import admin
from .models import Job,JobType,Company
# Register your models here.
admin.site.register(Job)
admin.site.register(JobType)
admin.site.register(Company)