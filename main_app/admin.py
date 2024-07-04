from django.contrib import admin
from .models import Candidate
from .models import Job

admin.site.register(Candidate)
admin.site.register(Job)