from django.shortcuts import render
from .models import Exams, Subjects, Students

def project_info(request):
    exams = Exams.objects.all()
    subjects = Subjects.objects.all()
    students = Students.objects.all()

    return render(request, 'university_project_name/project_info.html', {'exams': exams, 'subjects': subjects, 'students': students})
