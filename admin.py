from django.contrib import admin
from SMS.models import Student22

# Register your models here.

#admin.site.register(Student22)

@admin.register(Student22)
class stdAdmin(admin.ModelAdmin):
     
     list_display= ['name','age','mobileno']
