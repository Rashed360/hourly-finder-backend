from django.db import models
from app_user.models import RecruiterProfile,SeekerProfile
from uuid import uuid4


class JobType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Job Type Name')
    salary = models.CharField(max_length=50, verbose_name='Salary Type',blank=True)
    def __str__(self):
        return self.name


class Company(models.Model):
    recruiter = models.ForeignKey(RecruiterProfile,on_delete=models.CASCADE,related_name='com_recter')
    name = models.CharField(max_length=100, blank=True, verbose_name='Company Name')
    moto = models.CharField(max_length=200, blank=True, verbose_name='Company Moto')
    description = models.TextField(blank=True,verbose_name='Description')
    logo = models.ImageField(upload_to='jobs', blank=True, verbose_name='Company Logo')
    location = models.CharField(max_length=50, blank=True, verbose_name='Company Location')
    def __str__(self):
        return self.name +', '+ self.location


class Job(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='company')
    recruiter = models.ForeignKey(RecruiterProfile,on_delete=models.CASCADE,related_name='recruiter')

    title = models.CharField(max_length=150, verbose_name='Job Title')
    image = models.ImageField(upload_to='jobs',blank=True, verbose_name='Job Banner')
    slug = models.SlugField(max_length=264, unique=True)

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
    location = models.CharField(max_length=50, verbose_name='Job Location', default='')
    STATUS = ((1,'Pending'),(2,'Hidden'),(3,'Completed'))
    status = models.PositiveSmallIntegerField(choices=STATUS,default=1,verbose_name='Job Status') 

    overview = models.TextField(blank=True,verbose_name='Job Overview')
    todo = models.TextField(blank=True,verbose_name='Job Responsibilities')
    skill = models.CharField(max_length=100, verbose_name='Job Skills')
    keyword = models.CharField(max_length=100, verbose_name='Job Keywords')
    
    class Meta:
        ordering = ['-created',]

    def save(self, *args, **kwargs):
        re_chars = {' ': '-', '/': '', '?': '', '=': ''}
        self.slug = self.title.lower().translate(str.maketrans(re_chars))+'-'+str(uuid4())
        super(Job, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title+' by '+self.company.name+','+self.company.location

class Application(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='job')
    seeker = models.ForeignKey(SeekerProfile,on_delete=models.CASCADE,related_name='seeker')
    message = models.TextField(blank=True,verbose_name='message')
    applied = models.DateTimeField(auto_now_add=True)

    STATUS = ((1,'Pending'),(2,'Rejected'),(3,'Short-listed'),(4,'Hired'))
    status = models.PositiveSmallIntegerField(choices=STATUS,default=1,verbose_name='status')    
    
    class Meta:
        ordering = ['-applied',]    
    def __str__(self):
        return self.seeker.user.first_name+"'s Application for "+self.job.title


class Work(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='work_job')
    seeker = models.ForeignKey(SeekerProfile,on_delete=models.CASCADE,related_name='work_seeker')
    recruiter = models.ForeignKey(RecruiterProfile,on_delete=models.CASCADE,related_name='work_recruiter')
    created = models.DateTimeField(auto_now_add=True)
    STATUS = ((1,'Accept'),(2,'Prepare'),(3,'Complete'),(4,'Review'),(5,'Done'))
    status = models.PositiveSmallIntegerField(choices=STATUS,default=1,verbose_name='Work Status')

    class Meta:
        ordering = ['-created',]    
    def __str__(self):
        return self.job.title+" - Work"