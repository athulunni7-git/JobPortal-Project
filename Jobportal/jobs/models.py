from django.db import models
from account.models import  RecruiterProfile
from account.models import CandidateProfile
# Create your models here.

class Category(models.Model):
    
    category_name = models.CharField(max_length=100)
    
    icon = icon = models.CharField(max_length=100,default="fa-solid fa-briefcase")
        
        
    
    
    def __str__(self):
        return self.category_name
    
    
class Job(models.Model):
    
    job_types_choices = [("full-time", "Full Time"),
                         ("part-time", "Part Time"),]
    
    
    experiences_choices = [ ("0-1", "0-1 Years"),
                    ("1-3", "1-3 Years"),
                    ("3-5", "3-5 Years"),
                    ("5+", "5+ Years"),]
    
    status_choices = [('available','available'),('closed','closed')]
    
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=50)
    salary = models.IntegerField()
    requirements = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='jobs')
    recruiter = models.ForeignKey(RecruiterProfile,on_delete=models.CASCADE,related_name='jobs')
    job_type = models.CharField(max_length=20, choices=job_types_choices)
    experience = models.CharField(max_length=20 , choices=experiences_choices)
    status = models.CharField(max_length=20,choices=status_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    
    def __str__(self):
        return self.job_title
     
     
class Application(models.Model):
    
    status_choices = [
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
]
    
    candidate = models.ForeignKey(CandidateProfile,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE) 
    status = models.CharField(max_length=50,choices=status_choices,default='pending') 
    applied_at = models.DateTimeField(auto_now_add=True)
    
    
    

