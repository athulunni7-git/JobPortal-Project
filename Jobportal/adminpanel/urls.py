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

app_name = "adminpanel"

urlpatterns = [
    
    path('',views.AdminDashboardView.as_view(),name="admindashboard"),
    path("recruiters",views.ManageRecruitersView.as_view(),name="recruiters"),
    path('recruiter_details<int:i>',views.RecruiterDetailsView.as_view(),name="recruiterdetail"),
    path('candidates',views.ManageCandidateview.as_view(),name="candidates"),
    path('candidate_detail/<int:i>',views.CandidateDetailsView.as_view(),name="candidate_detail"),
    path('jobs',views.ManageJobsView.as_view(),name="jobs"),
    path("jobdetails/<int:i>",views.JobDetailsview.as_view(),name="jobdetail"),
    path('categories',views.ManageCategoryView.as_view(),name="categories"),
    path('category/add/',views.AddCategory.as_view(),name="add_category"),
    path('category/edit/<int:i>',views.EditCategoryView.as_view(),name="edit_category"),
    path('category/delete/<int:i>',views.DeleteCategoryView.as_view(),name="delete_category"),
    path('payment',views.ManagePaymentView.as_view(),name="payments"),
    path('paymentdetail/<int:i>',views.PaymentDetailView.as_view(),name="payment_detail"),
    path('recruiterdelete/<int:i>',views.DeleteRecruiterView.as_view(),name="delete_recruiter"),
    path('candidatedelete/<int:i>',views.DeleteCandidateView.as_view(),name="delete_candidate"),
    path('premium',views.PremiumMembers.as_view(),name="premium_members")
      
    
   
]
