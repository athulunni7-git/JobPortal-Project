from django.shortcuts import render , redirect
from django.views import View
from account.models import RecruiterProfile , CandidateProfile,CustomUser
from jobs.models import Job,Application,Category
from payment.models import Payment

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
    
       
class ManageCandidateview(View):
    
    def get(self,request):
        
        if not request.user.is_superuser:
            return redirect('home')
        
        candidates = CandidateProfile.objects.select_related("user")
        
        context = {"candidates":candidates}
        
        return render(request,'adminpanel/candidates.html',context)
    
    
class CandidateDetailsView(View):
    
    def get(self,request,i):
        
        candidates = CandidateProfile.objects.get(id=i)
        applied_jobs = Application.objects.filter(candidate=candidates).count()
        
        context = {"candidate":candidates,"applied_jobs":applied_jobs}
        
        return render(request,'adminpanel/candidatedetail.html',context)
        
    
class ManageJobsView(View):
    
    def get(self,request):
        
        if not request.user.is_superuser:
            
            return redirect("home")
        
        jobs = Job.objects.select_related("recruiter","category")
        
        context ={"jobs":jobs}
        
        return render(request,'adminpanel/jobs.html',context)
    
class JobDetailsview(View):
    
    def get(self,request,i):
        
        job = Job.objects.select_related('recruiter','category').get(id=i)
        
        applicants = Application.objects.filter(job=job).count()
        
        context = {'job':job,'applicants':applicants}
        
        return render(request,'adminpanel/jobdetail.html',context)
    
class ManageCategoryView(View):
    
    def get(self,request):
        
        if not request.user.is_superuser:
            
            return redirect("home")
        
        categories = Category.objects.all()
        
        context = {'categories':categories}
        
        return render(request,'adminpanel/categories.html',context)
   
   
from adminpanel.forms import CategoryForm
    
class AddCategory(View):
    
    def get(self,request):
        
        form_instance = CategoryForm()
        context = {"form":form_instance}
        return render(request,'adminpanel/category_form.html',context)
    
    def post(self,request):
        
        form_instance = CategoryForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('adminpanel:categories')
        
        context = {'form':form_instance}
        
        return render(request,'adminpanel/category_form.html',context)
    
class EditCategoryView(View):
    
    def get(self,request,i):
        
        category = Category.objects.get(id=i)
        
        form_instance = CategoryForm(instance=category)
        context = {"form":form_instance}
        return render(request,'adminpanel/category_form.html',context)
    
    def post(self,request,i):
        
        category = Category.objects.get(id=i)
        
        form_instance = CategoryForm(request.POST,instance=category)
        
        if form_instance.is_valid():
            form_instance.save()
            return redirect('adminpanel:categories')
        
        context = {'form':form_instance}
        return render(request,'adminpanel/category_form.html',context)
    
    
class DeleteCategoryView(View):
    
    def get(self,request,i):
        
        category = Category.objects.get(id=i)
        
        context = {'category':category}
        
        return render(request,'adminpanel/category_confirm_delete.html',context)
    
    def post(self,request,i):
        
        category = Category.objects.get(id=i)
        
        category.delete()
        return redirect('adminpanel:categories')
    
    
    
    
class ManagePaymentView(View):
    
    def get(self,request):
        
        if not request.user.is_superuser:
            return redirect("home")
        
        payments = Payment.objects.all()
        
        context = {"payments":payments}
        
        return render(request,'adminpanel/payments.html',context)

class PaymentDetailView(View):
    
    def get(self,request,i):
        
        if not request.user.is_superuser:
            return redirect("home")
        
        payment = Payment.objects.select_related("user").get(id=i)
        
        context = {'payment':payment}
        
        return render(request,'adminpanel/payment_detail.html',context)
    
    
    
class DeleteRecruiterView(View):
    
    def get(self,request,i):
        
        recruiter = RecruiterProfile.objects.get(id=i)
        
        context = {'recruiter':recruiter}
        
        return render(request,'adminpanel/recruiter_confirm_delete.html',context)
    
    def post(self,request,i):
        
        recruiter = RecruiterProfile.objects.get(id=i)
        
        recruiter.user.delete()
        
        return redirect('adminpanel:recruiters')
    
class DeleteCandidateView(View):
    
    def get(self,request,i):
        
        candidate = CandidateProfile.objects.get(id=i)
        
        context = {'candidate':candidate}
        
        return render(request,'adminpanel/confirm_delete.html',context)
    
    def post(self,request,i):
        
        candidate = CandidateProfile.objects.get(id=i)
        
        candidate.user.delete()
        
        return redirect('adminpanel:candidates')
        
        