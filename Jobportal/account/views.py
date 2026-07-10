from django.shortcuts import render , redirect
from django.views import View
from .forms import UserRegisterForm ,UserLoginForm
from .models import CandidateProfile , RecruiterProfile
from django.contrib.auth import authenticate , login , logout

# Create your views here.


class Home(View):
    
    def get(self,request):
        
        return  render(request,'home.html')
 

    
class UserRegisterView(View):
    
    def get(self,request):
        
        form_instance = UserRegisterForm()
        context = {'form':form_instance}
        return render(request,'register.html',context)
    
    def post(self,request):
        
        form_instance = UserRegisterForm(request.POST)
        if form_instance.is_valid():
            user = form_instance.save()
            
            if user.user_type == 'candidate':
                CandidateProfile.objects.create(user=user)
            elif user.user_type == 'recruiter':
                RecruiterProfile.objects.create(user=user)
                
            return redirect('account:userlogin')
        context = {'form':form_instance}
        return render(request,'register.html',context)
       

class UserLogin(View):
    
    def get(self,request):
        
        form_instance = UserLoginForm()
        context = {'form':form_instance}
        return render(request,'login.html',context)
    
    def post(self,request):
        
        form_instance = UserLoginForm(request.POST)
        if form_instance.is_valid():
            data = form_instance.cleaned_data
            
            u = data['username']
            p = data['password']
            
            user = authenticate(username = u , password = p)
            
            if user and user.user_type == 'candidate':
                
                login(request , user)
                return redirect('account:candidate_dashboard')
            
            elif user and user.user_type == 'recruiter':
                
                login(request,user)
                return redirect('account:recruiter_dashboard')
            
class UserLogout(View):
    
    def get(self,request):
        
        logout(request)
        
        return redirect('account:userlogin')
    
class RecruiterDashView(View):
    def get(self,request):
        return render(request,'recruiterdash.html')
    
class CandidateDashView(View):
    def get(self,request):
        return render(request,'candidatedash.html')