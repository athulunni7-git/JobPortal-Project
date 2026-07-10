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
from account import views

app_name = 'account'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.UserRegisterView.as_view(),name='userregister'),
    path('userlogin',views.UserLogin.as_view(),name='userlogin'),
    path('logout',views.UserLogout.as_view(),name='userlogout'),
    path('recruiterdashboard',views.RecruiterDashView.as_view(),name='recruiter_dashboard'),
    path('candidatedashboard',views.CandidateDashView.as_view(),name='candidate_dashboard'),

]
