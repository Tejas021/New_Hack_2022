from django.contrib import admin
from .models import StudentForm, SiteConfig
# Register your models here.

# admin.site.register(models.CompanyInfo)

class StudentFormAdmin(admin.ModelAdmin):
    readonly_fields = ('application_date', )

admin.site.register(StudentForm, StudentFormAdmin)
admin.site.register(SiteConfig)
