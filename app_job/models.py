from django.db import models
from app_user.models import RecruiterProfile


class JobType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Job Type Name')
    salary = models.CharField(max_length=50, verbose_name='Salary Type',blank=True)
    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Company Name')
    moto = models.CharField(max_length=200, verbose_name='Company Moto')
    description = models.TextField(blank=True,verbose_name='Description')
    logo = models.ImageField(upload_to='jobs', verbose_name='Company Logo')
    location = models.CharField(max_length=50, verbose_name='Company Location')
    def __str__(self):
        return self.name +', '+ self.location


class Job(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='company')
    recruiter = models.ForeignKey(RecruiterProfile,on_delete=models.CASCADE,related_name='recruiter')

    title = models.CharField(max_length=150, verbose_name='Job Title')
    image = models.ImageField(upload_to='jobs', verbose_name='Job Banner')

    salary = models.CharField(max_length=10, verbose_name='Salary')
    type = models.ForeignKey(JobType,on_delete=models.CASCADE,related_name='type')
    duration = models.CharField(max_length=50, verbose_name='Job Duration')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=50, verbose_name='Job Language')
    vacancy = models.CharField(max_length=10, verbose_name='Job Vacancy')
    LEVELS = ((1,'Novice'),(2,'Beginner'),(3,'Intermediate'),(4,'Advanced'),(5,'Expert'))
    level = models.PositiveSmallIntegerField(choices=LEVELS,default=1,verbose_name='Level Required')
    starting = models.CharField(max_length=80, verbose_name='Starting Date')
    latlng = models.CharField(max_length=50, verbose_name='Latitute,Longitude')

    overview = models.TextField(blank=True,verbose_name='Job Overview')
    todo = models.TextField(blank=True,verbose_name='Job Responsibilities')
    skill = models.CharField(max_length=100, verbose_name='Job Skills')
    keyword = models.CharField(max_length=100, verbose_name='Job Keywords')
    
    class Meta:
        ordering = ['-created',]
    
    def __str__(self):
        return self.title