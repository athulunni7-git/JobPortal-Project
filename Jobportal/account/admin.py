from django.contrib import admin
from account.models import CustomUser , CandidateProfile , RecruiterProfile
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(CandidateProfile)
admin.site.register(RecruiterProfile)
