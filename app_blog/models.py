import os
import random
from uuid import uuid4

from django.db import models


# Create your models here.
def rename_image(instance, filename):
    path = 'blogs/'
    brand = 'HourlyFinder_blog-'
    extension = "." + filename.split('.')[-1]
    stringId = str(uuid4())
    randInt = str(random.randint(10, 99))

    # Filename reformat
    filename_reformat = brand + stringId + randInt + extension
    return os.path.join(path, filename_reformat)

class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    sub_title = models.CharField(max_length=250, verbose_name=' Sub Title')
    slug = models.SlugField(max_length=264, unique=True)
    thumbnail = models.ImageField(upload_to=rename_image, verbose_name='Blog Thumbnail')
    image_one = models.ImageField(upload_to=rename_image, blank=True, verbose_name='Blog Image One')
    image_two = models.ImageField(upload_to=rename_image, blank=True, verbose_name='Blog Image Two')
    description = models.TextField(verbose_name='Blog Description')
    keyword = models.CharField(max_length=100, verbose_name='Blog Keywords')
    author = models.CharField(max_length=150, verbose_name='Author')
    status = models.BooleanField(default=True,verbose_name='Blog Status')
    published_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date',]

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(" ","-")+'-'+str(uuid4())
        super(Blog, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
