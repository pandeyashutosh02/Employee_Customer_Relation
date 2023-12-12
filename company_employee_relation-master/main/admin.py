from django.contrib import admin
from .models import Employee,Company

# Register your models here.

@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','comment']


@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display=['id','name']

