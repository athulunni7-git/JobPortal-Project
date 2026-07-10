from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    
    user_types = (
        ('candidate', 'Candidate'),
        ('recruiter', 'Recruiter'),
    )
    
    user_type = models.CharField(max_length=20,choices=user_types)
    
    
class CandidateProfile(models.Model):
    
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    phone = models.IntegerField(null=True,blank=True)
    skills = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/',blank=True,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True,null=True)
    
    def __str__(self):
        return self.user.username
    
class RecruiterProfile(models.Model):
    
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_website = models.URLField(blank=True)
    company_logo = models.ImageField(upload_to='company_logo/',blank=True,null=True)
    
    def  __str__(self):
        return self.company_name
    