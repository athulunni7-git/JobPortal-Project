
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms import PasswordInput

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('user_type','username','email','password1','password2','first_name','last_name')
        
        
class UserLoginForm(forms.Form):
    
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=PasswordInput)