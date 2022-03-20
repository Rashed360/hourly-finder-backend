from django.contrib import admin
from .models import SeekerProfile,RecruiterProfile,Review
# Register your models here.
admin.site.register(SeekerProfile)
admin.site.register(RecruiterProfile)
admin.site.register(Review)