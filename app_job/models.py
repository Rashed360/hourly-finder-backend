from django.db import models


class JobType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Job Type Name')
    salary = models.CharField(max_length=50, verbose_name='Salary Type')
    def __str__(self):
        return self.name

class JobSkill(models.Model):
    name = models.CharField(max_length=50, verbose_name='Job Skill Name')
    def __str__(self):
        return self.name

class JobKeyword(models.Model):
    name = models.CharField(max_length=100, verbose_name='Keyword Name')
    color = models.CharField(max_length=6, verbose_name='Keyword Color')
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Company Name')
    logo = models.ImageField(upload_to='jobs', verbose_name='Company Logo')
    location = models.CharField(max_length=50, verbose_name='Company Location')
    # more fields required
    def __str__(self):
        return self.name +', '+ self.location


class Job(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='company')
    recruiter = models.ForeignKey(RecruterProfile,on_delete=models.CASCADE,related_name='recruiter')

    title = models.CharField(max_length=150, verbose_name='Job Title')
    image = models.ImageField(upload_to='jobs', verbose_name='Job Banner')

    salary = models.CharField(max_length=10, verbose_name='Job Title')
    type = models.ForeignKey(JobType,on_delete=models.CASCADE,related_name='type')
    duration = models.CharField(max_length=50, verbose_name='Job Duration')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    language = models.CharField(max_length=50, verbose_name='Job Language')
    vacancy = models.CharField(max_length=10, verbose_name='Job Vacancy')
    level = models.CharField(max_length=10, verbose_name='Job Vacancy')
    starting = models.CharField(max_length=80, verbose_name='Job Vacancy')
    latlng = models.CharField(max_length=50, verbose_name='Latitute,Longitude')

    overview = models.TextField(blank=True,verbose_name='Job Overview')
    todo = models.TextField(blank=True,verbose_name='Job Responsibilities')
    skill = models.ForeignKey(JobSkill,on_delete=models.CASCADE,related_name='skills')
    keyword = models.ForeignKey(JobKeyword,on_delete=models.CASCADE,related_name='keywords')
    
    class Meta:
        ordering = ['-created',]
    
    def __str__(self):
        return self.title