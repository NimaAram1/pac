from django.db import models
from django.contrib.auth.models import  AbstractUser

class User(AbstractUser):
    profile_image = models.ImageField(upload_to='media',verbose_name='عکس پروفایل',default='default.png')
    bio = models.TextField(verbose_name='درباره کاربر',blank=True,null=True)