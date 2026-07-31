from django.db import models
from account.models import CustomUser

# Create your models here.

class Payment(models.Model):
    
    PAYMENT_STATUS = (('pending','pending'),
                      ('success','success'),
                      ('failed','failed'))
    
    PLAN_CHOICE = (('monthly','Monthly'),
                   ('yearly','Yearly'))
    
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    plan = models.CharField(max_length=20,choices=PLAN_CHOICE)
    razorpay_order_id = models.CharField(max_length=100,null=True,blank=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null= True)
    razorpay_signature = models.CharField(max_length=300,blank=True,null=True)
    status = models.CharField(max_length=20,choices=PAYMENT_STATUS,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.user.username} - {self.status}"
    
        
    