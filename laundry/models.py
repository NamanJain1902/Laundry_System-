from django.db import models

# Create your models here.
CHOICES = [(i, i) for i in range(0, 11)]


class BLaundry(models.Model):
    student = models.ForeignKey("accounts.StudentProfile", on_delete=models.CASCADE)
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
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.student.user.username}"
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in BLaundry._meta.fields]

# "accounts.StudentProfile"
class GLaundry(models.Model):
    student = models.ForeignKey("accounts.StudentProfile", on_delete=models.CASCADE)
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
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name}"

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in GLaundry._meta.fields]