from django.contrib import admin
from .models import Exams,Subjects,Students

admin.site.register(Students)
admin.site.register(Subjects)
admin.site.register(Exams)