from django.db.models import fields
from accounts.models import StudentProfile
from django.contrib import admin
from .models import  StudentProfile, EmployeeProfile, Hostel, Gender

# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(EmployeeProfile)
admin.site.register(Hostel)
admin.site.register(Gender)
