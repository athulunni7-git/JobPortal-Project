
from django import forms 
from .models import Job
from account.models import RecruiterProfile,CandidateProfile

class JobForm(forms.ModelForm):
    
    class Meta:
        model = Job
        fields = ('job_title','description','location','salary','requirements','category','job_type','experience','status')
        
class RecruiterProfileForm(forms.ModelForm):
    
    class Meta:
        model = RecruiterProfile
        fields = ['company_logo','company_name','company_website']
        
        
class CandidateProfileform(forms.ModelForm):
    
    class Meta:
        model = CandidateProfile
        fields = ['phone','skills','resume','profile_picture']