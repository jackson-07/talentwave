from django.contrib import admin
from .models import Record
from .models import Job

admin.site.register(Record)
admin.site.register(Job)