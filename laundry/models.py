from django.db import models
# from accounts.models import StudentProfile
from django.contrib.auth.models import User

# Create your models here.
CHOICES = [(i, i) for i in range(0, 11)]

# class Laundry(models.Model):
#     jeans = models.PositiveIntegerField(default=0, choices=CHOICES)
#     pent = models.PositiveIntegerField(default=0, choices=CHOICES)
#     pyjama = models.PositiveIntegerField(default=0, choices=CHOICES)
#     shorts = models.PositiveIntegerField(default=0, choices=CHOICES)
#     t_shirt = models.PositiveIntegerField(default=0, choices=CHOICES)
#     bed_sheet = models.PositiveIntegerField(default=0, choices=CHOICES)
#     pillow_cover = models.PositiveIntegerField(default=0, choices=CHOICES)
#     towel_htowel = models.PositiveIntegerField(default=0, choices=CHOICES)
#     turban = models.PositiveIntegerField(default=0, choices=CHOICES)
#     upper_hood = models.PositiveIntegerField(default=0, choices=CHOICES)


class BLaundry(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    jeans = models.PositiveIntegerField(default=0, choices=CHOICES)
    pent = models.PositiveIntegerField(default=0, choices=CHOICES)
    pyjama = models.PositiveIntegerField(default=0, choices=CHOICES)
    shorts = models.PositiveIntegerField(default=0, choices=CHOICES)
    t_shirt = models.PositiveIntegerField(default=0, choices=CHOICES)
    bed_sheet = models.PositiveIntegerField(default=0, choices=CHOICES)
    pillow_cover = models.PositiveIntegerField(default=0, choices=CHOICES)
    towel_htowel = models.PositiveIntegerField(default=0, choices=CHOICES)
    turban = models.PositiveIntegerField(default=0, choices=CHOICES)
    upper_hood = models.PositiveIntegerField(default=0, choices=CHOICES)
    
    def __str__(self):
        return f"{self.student.username}"


class GLaundry(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    jeans = models.PositiveIntegerField(default=0, choices=CHOICES)
    pent = models.PositiveIntegerField(default=0, choices=CHOICES)
    pyjama = models.PositiveIntegerField(default=0, choices=CHOICES)
    shorts = models.PositiveIntegerField(default=0, choices=CHOICES)
    t_shirt = models.PositiveIntegerField(default=0, choices=CHOICES)
    bed_sheet = models.PositiveIntegerField(default=0, choices=CHOICES)
    pillow_cover = models.PositiveIntegerField(default=0, choices=CHOICES)
    towel_htowel = models.PositiveIntegerField(default=0, choices=CHOICES)
    turban = models.PositiveIntegerField(default=0, choices=CHOICES)
    upper_hood = models.PositiveIntegerField(default=0, choices=CHOICES)

    kurta_salwar = models.PositiveIntegerField(default=0, choices=CHOICES)
    skirt = models.PositiveIntegerField(default=0, choices=CHOICES)
    dupatta = models.PositiveIntegerField(default=0, choices=CHOICES)

    def __str__(self):
        return f"{self.student.username}"
