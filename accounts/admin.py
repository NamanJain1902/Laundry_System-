from accounts.models import StudentProfile
from django.contrib import admin
from .models import  StudentProfile, Hostel, Gender

# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(Hostel)
admin.site.register(Gender)
