from django.contrib import admin
from .models import Job,JobType,Company,Application,Work,Offer
# Register your models here.
admin.site.register(Job)
admin.site.register(JobType)
admin.site.register(Company)

admin.site.register(Application)
admin.site.register(Work)
admin.site.register(Offer)