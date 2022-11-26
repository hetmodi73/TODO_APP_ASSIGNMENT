from django.contrib import admin
from .models import task
# Register your models here.

class showtask(admin.ModelAdmin):
    list_display = ['date','title','details']

admin.site.register(task,showtask)
