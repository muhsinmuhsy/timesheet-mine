from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
   
    is_employee = models.BooleanField(default=False)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='s_teacher' ,null=True, blank=True)