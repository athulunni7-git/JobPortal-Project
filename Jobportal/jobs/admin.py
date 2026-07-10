from django.contrib import admin
from jobs.models import Category , Job , Application
# Register your models here.

admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Application)