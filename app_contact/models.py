
from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='First Name')
    last_name = models.CharField(max_length=50,verbose_name='Last Name')
    email = models.EmailField(max_length=100,verbose_name='Email')
    phone = models.CharField(max_length=15,verbose_name='Phone')
    profile = models.CharField(max_length=200, blank=True, verbose_name='Profile Name')
    subject = models.CharField(max_length=250, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    report_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-report_date',]

    def __str__(self):
        return self.subject


