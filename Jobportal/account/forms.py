
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.forms import PasswordInput

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username','email','password1','password2','user_type','first_name','last_name')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].help_text = None
        
        
class UserLoginForm(forms.Form):
    
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=PasswordInput)