from django.db import models
from app_auth.models import User


class RecruiterProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='users', blank=True, verbose_name='Profile Picture')
    phone = models.CharField(max_length=15,blank=True)
    identity = models.CharField(max_length=30,blank=True)
    dob = models.CharField(max_length=15,blank=True)
    bio = models.TextField()
    designation = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.user.first_name+ ' Recruiter'

class SeekerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='users', blank=True, verbose_name='Profile Picture')
    phone = models.CharField(max_length=15,blank=True)
    identity = models.CharField(max_length=30,blank=True)
    dob = models.CharField(max_length=15,blank=True)
    bio = models.TextField()
    expertise = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.user.first_name+ ' Seeker'

class Review(models.Model):
    reveiwer = models.ForeignKey(User,on_delete=models.CASCADE, related_name='reviewer')
    reviewed = models.ForeignKey(User,on_delete=models.CASCADE, related_name='reviewed')
    body = models.TextField(blank=True)
    def __str__(self):
        return self.reveiwer + ' reviewed '+ self.reviewed