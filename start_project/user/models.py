from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model

# User = get_user_model()

class CustomUser(AbstractUser):
    country_of_residence = models.CharField(max_length=15, null=True, blank=True)
    city_of_residence = models.CharField(max_length=15, blank=True, null=True)
    

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    
