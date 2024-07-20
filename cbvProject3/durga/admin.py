from django.contrib import admin
from durga.models import Company


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=['name','location', 'ceo']


admin.site.register(Company, CompanyAdmin)