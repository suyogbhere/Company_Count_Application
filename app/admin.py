from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Company_data)
class CompanydataAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','industry','city','country','year','state')
