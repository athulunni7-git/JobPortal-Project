from django.shortcuts import render , redirect
from django.http import HttpResponse    
from django.views import View
from .forms import JobForm,RecruiterProfileForm
from account.models import RecruiterProfile , CandidateProfile
from django.contrib import messages

# Create your views here.

class CreateJobView(View):
    
    def get(self,request):
        
        print(request.user)
        print(request.user.user_type)
        
        if not request.user.is_authenticated:
        
            return redirect('account:userlogin')
        
        if request.user.user_type != 'recruiter':
            messages.warning(request, "Only recruiters can access this page.")
            return redirect('home')
        else:
            form_instance = JobForm()
            context = {'form':form_instance}
            return render(request,'createjob.html',context)
    
    def post(self,request):
        
        if not request.user.is_authenticated:
        
            return redirect('account:userlogin')
        
        if request.user.user_type != 'recruiter':
            messages.warning(request, "Only recruiters can access this page.")
            return redirect('home')
        else:
            form_instance = JobForm(request.POST)
            if form_instance.is_valid():
               job =  form_instance.save(commit=False)
               recruiter = request.user.recruiterprofile
               job.recruiter = recruiter
               job.save()
               messages.success(request,"job Created Successfully")
               
               return redirect('jobs:myjobs')
                
        
from .models import Job            
            
class MyJobView(View):
    
    def get(self,request):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')
            
        if request.user.user_type != 'recruiter':
            messages.warning(request, "Only recruiters can access this page.")
            return redirect('home')
        jobs = Job.objects.filter(recruiter = request.user.recruiterprofile)
        context = {'jobs':jobs}
        return render(request,'myjobs.html',context)
        
        
        
class JobUpdateView(View):
    
    def get(self,request,i):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')
        
        if request.user.user_type != 'recruiter':
            messages.warning(request, "Only recruiters can access this page.")
            return redirect('home')
        try:
            j = Job.objects.get(id=i)
        except Job.DoesNotExist:
                return HttpResponse('job not found')
        else:
            return redirect('jobs:myjobs')
                
        if j.recruiter == request.user.recruiterprofile:
            
            form_instance = JobForm(instance=j)
            context = {'form':form_instance}
            return render(request,'editpage.html',context)
        
        
    def post(self,request,i):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')
        
        if request.user.user_type != 'recruiter':
            messages.warning(request, "Only recruiters can access this page.")
            return redirect('home')
        
        try:
            j = Job.objects.get(id=i)
        except Job.DoesNotExist:
            return HttpResponse("job not found")
            
            
        if j.recruiter != request.user.recruiterprofile:
            return redirect('account:userlogin')
        
        form_instance = JobForm(request.POST,instance = j)
        if form_instance.is_valid():
            form_instance.save()
            messages.success(request,"job Updated Successfully")
            return redirect('jobs:myjobs')
        
    
class DeleteJobView(View):
    
    def get(self,request,i):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')
        
        if request.user.user_type != 'recruiter':
            messages.warning(request, "Only recruiters can access this page.")
            return redirect('home')
        
        try:
            j = Job.objects.get(id=i)
        except Job.DoesNotExist:
            return HttpResponse("job not found")
        
        if j.recruiter != request.user.recruiterprofile:
            return redirect('home')
        
        j.delete()
        messages.success(request,"Job Deleted Successfully")
        
        return redirect('jobs:myjobs')
    
    
class JobListView(View):
    
    def get(self,request):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')
        
        if request.user.user_type != 'candidate':
            messages.warning(request, "Only candidates can apply for jobs.")
            return redirect('home')
        
        jobs = Job.objects.filter(status='available')
        context = {'jobs':jobs}
        return render(request,'joblist.html',context)
            

class RecruiterUpdateView(View):
    
    def get(self,request):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')
        
        if request.user.user_type != 'recruiter':
            messages.warning(request, "Only recruiters can access this page.")
            return redirect('home')
        
        profile = request.user.recruiterprofile
        
        form_instance = RecruiterProfileForm(instance = profile)
        context = {'form':form_instance}
        return render(request,'recruiterupdate.html',context)
    
    def post(self,request):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')
        
        if request.user.user_type != 'recruiter':
            messages.warning(request, "Only recruiters can access this page.")
            return redirect('home')
        
        profile = request.user.recruiterprofile
        
        form_instance = RecruiterProfileForm(request.POST,instance = profile)
        if form_instance.is_valid():
            form_instance.save()
            messages.success(request,"Profile Updated Successfully")
            
            return redirect('jobs:myjobs')
        
        
            
            
class JobDetailsView(View):
    
    def get(self,request,i):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')
        
        if request.user.user_type != 'candidate':
            messages.warning(request, "Only candidates can apply for jobs.")
            return redirect('home')
                
        try:
            job = Job.objects.get(id=i)
        except Job.DoesNotExist:
            return HttpResponse("Job not found")
        context = {'job':job}
        return render(request,'jobdetails.html',context)
        
   
from .models import Application
            
class ApplyJobView(View):
    
    def post(self,request,i):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')
        
        if request.user.user_type != 'candidate':
            messages.warning(request, "Only candidates can apply for jobs.")
            return redirect('home')
        
        try:
            job = Job.objects.get(id=i)
        except Job.DoesNotExist:
            return HttpResponse("Job not found")
        
        already_applied =  Application.objects.filter(candidate=request.user.candidateprofile,job=job).exists()
        
        if already_applied:
            messages.warning(request,"You have already applied for this job.")
            return redirect('jobs:joblist')
           
            
        else:
            
            Application.objects.create(candidate = request.user.candidateprofile,job=job)
            
            return redirect('jobs:applysuccess')
        
class ApplySuccessView(View):
    
    def get(self,request):
        return render(request,'applysuccess.html')
    
    
class MyApplicationsView(View):
    
    def get(self,request):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')
        
        if request.user.user_type != 'candidate':
            
            messages.warning(request, 'Only candidates can this page')
            return redirect("home")
        
        my_application = Application.objects.filter(candidate=request.user.candidateprofile)
        context = {'applications':my_application}
        return render(request,'myapplications.html',context)
    


class ViewApplicantionView(View):
    
    def get(self,request,i):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')
        
        if request.user.user_type!='recruiter':
            messages.warning(request,'only recruiters can view this page')
            return redirect('home')
            
        try:
            j = Job.objects.get(id=i)
        except Job.DoesNotExist:
                return HttpResponse('job not found')
            
        if j.recruiter != request.user.recruiterprofile:
            messages.warning(request, "You are not authorized.")
            return redirect('jobs:myjobs')
            
        applications = Application.objects.filter(job=j)
        
        context = {'job':j,'applications':applications}
        return render(request,'viewapplications.html',context)
        
            
    
            
class CandidateDetailsView(View):
    
    def get(self,request,i):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')
        
        if request.user.user_type!='recruiter':
            messages.warning(request,'only recruiters can view this page')
            return redirect('home')
        
        try:
            candidate = Application.objects.get(id=i)
        except Job.DoesNotExist:
                return HttpResponse('job not found')
            
        if candidate.job.recruiter != request.user.recruiterprofile:
            messages.warning(request, "You are not authorized to view this application.")
            return redirect('jobs:myjobs')
        
        context = {'details':candidate}
        return render(request,'candidatedetail.html',context)
        

class CandidateUpdateView(View):
    
    def get(self,request):
        
        if not request.user.is_authenticated:
            return redirect('account:userlogin')
        
        if request.user.user_type!='candidate':
            messages.warning(request,'only recruiters can view this page')
            return redirect('home')
        
         
        
        