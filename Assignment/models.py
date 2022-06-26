from django.db import models 
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


# Create your models here.

class User(AbstractUser):
    username = None
    id =  models.AutoField(primary_key=True)
    password = models.CharField(max_length=125,unique=True)
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300, unique=True)
    dob = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)
    objects = UserManager()
    

    def __str__(self):
        return self.email
    
class Paragraphs(models.Model):
    id =  models.AutoField(primary_key=True)
    paragraphs = models.TextField()
    