from laundry.models import CHOICES
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Gender(models.Model):
    
    gender = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.gender


class Hostel(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    laundry_id = models.AutoField(primary_key=True, help_text='Unique laundry num. for student table')
    college_id = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=200)
    mobile_num = PhoneNumberField(null=False, blank=True, unique=False)
    room_num = models.CharField(max_length=10)

    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    hostel = models.ForeignKey(Hostel, on_delete=models.SET_NULL, null=True)


    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    class Meta:
        # ordering = ['hostel']
        verbose_name_plural = 'Students'

