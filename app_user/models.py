from django.db import models
from app_auth.models import User


class RecruiterProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    phone = models.CharField(max_length=15)
    designation = models.CharField(max_length=50)
    def __str__(self):
        return self.user.first_name+ ' Recruiter'

class SeekerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    phone = models.CharField(max_length=15)
    expertise = models.CharField(max_length=50)
    def __str__(self):
        return self.user.first_name+ ' Seeker'