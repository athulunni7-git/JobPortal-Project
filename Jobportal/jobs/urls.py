"""
URL configuration for Jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views

app_name = 'jobs'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createjob',views.CreateJobView.as_view(),name='createjob'),
    path('myjobs',views.MyJobView.as_view(),name='myjobs'),
    path('editjob/<int:i>',views.JobUpdateView.as_view(),name='editjob'),
    path('delete/<int:i>',views.DeleteJobView.as_view(),name='delete'),
    path('joblist',views.JobListView.as_view(),name='joblist'),
    path('recruiterupdate',views.RecruiterUpdateView.as_view(),name='recruiterupdate'),
    path('jobdetails/<int:i>',views.JobDetailsView.as_view(),name='jobdetails'),
    path('applyjob/<int:i>',views.ApplyJobView.as_view(),name='jobapply'),
    path('applysucces',views.ApplySuccessView.as_view(),name='applysuccess'),
    path('myapplications',views.MyApplicationsView.as_view(),name='myapplications'),
    path('viewapplications/<int:i>',views.ViewApplicantsView.as_view(),name='viewapplications'),
    path('candidatedetails/<int:i>',views.CandidateDetailsView.as_view(),name='candidatedetails'),
    path('candidateprofileupdate',views.CandidateUpdateView.as_view(),name="candidate_profileupdate"),
    path('myprofile',views.MyProfileView.as_view(),name="myprofile"),
    path('companyprofile',views.CompanyProfileView.as_view(),name="companyprofile"),
    path('acceptapplicant/<int:i>',views.AcceptApplicant.as_view(),name="acceptapplicant"),
    path('rejectapplicant/<int:i>',views.RejectApplicant.as_view(),name='rejectapplicant'),
    path('search',views.SearchView.as_view(),name="search"),
    path('categorylist',views.Categorylist.as_view(),name="categorylist")
    
    
    
]
