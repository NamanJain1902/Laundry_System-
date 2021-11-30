from django.contrib import admin
from .models import GLaundry, BLaundry
# Register your models here.

class GLaundryAdminModel(admin.ModelAdmin):
    list_display = ['student', 'date']
    search_field=['date']

class BLaundryAdminModel(admin.ModelAdmin):
    list_display = ['student', 'date']
    search_field=['date']

# admin.site.register(Laundry)
admin.site.register(GLaundry, GLaundryAdminModel)
admin.site.register(BLaundry, BLaundryAdminModel)
