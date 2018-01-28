from django.contrib import admin

# Register your models here.

from .models import Job



class JobAdmin(admin.ModelAdmin):

    search_fields = ("uuid", "identifier", "percent_done",)
    list_display = ("uuid", "identifier", "percent_done", "status",)

admin.site.register(Job, JobAdmin)
