from django.contrib import admin
from testapp.models import Hydrabad_jobs, Bengluru_jobs, Pune_jobs


# Register your models here.
class Hydrabad_jobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibilty', 'address', 'email', 'phone_number']

admin.site.register(Hydrabad_jobs, Hydrabad_jobsAdmin)


class Bengluru_jobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibilty', 'address', 'email', 'phone_number']

admin.site.register(Bengluru_jobs, Bengluru_jobsAdmin)


class Pune_jobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibilty', 'address', 'email', 'phone_number']

admin.site.register(Pune_jobs, Pune_jobsAdmin)
 