from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255,unique=True)

    TYPES = ((1,'Seeker'),(2,'Recruiter'))
    user_type = models.PositiveSmallIntegerField(choices=TYPES,default=1)

    REQUIRED_FIELDS = ['username','user_type']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email