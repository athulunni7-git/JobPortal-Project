from django.shortcuts import render , redirect
from django.views import View
from account.models import RecruiterProfile , CandidateProfile,CustomUser
from jobs.models import Job,Application

# Create your views here.

class AdminDashboardView(View):
    
    def get(self,request):
        
        if not request.user.is_superuser:
            return redirect("home")
        
        total_recruiters = RecruiterProfile.objects.count()
        total_candidates = CustomUser.objects.filter(user_type="candidate").count()
        total_jobs = Job.objects.count()
        total_applications = Application.objects.count()
        premium_recruiters = RecruiterProfile.objects.filter(is_premium=True).count()
        
        context = { "total_recruiters": total_recruiters,
                    "total_candidates": total_candidates,
                    "total_jobs": total_jobs,
                    "total_applications": total_applications,
                    "premium_recruiters": premium_recruiters,}
        
        return render(request,'adminpanel/dashboard.html',context)
    
    
class ManageRecruitersView(View):
    
    def get(self,request):
        
        if not request.user.is_superuser:
            return redirect("home")
        
        recruiters = RecruiterProfile.objects.select_related('user')
        
        context = {"recruiters":recruiters}
        
        return render(request,'adminpanel/recruiters.html',context)
    
class RecruiterDetailsView(View):
    
    def get(self,request,i):
        
        recruiter = RecruiterProfile.objects.get(id=i)
        
        jobs = Job.objects.filter(recruiter=recruiter).count()
        
        context = {"recruiter":recruiter,"jobs":jobs}
        
        return render(request,'adminpanel/recruiterdetail.html',context)
        
    
    