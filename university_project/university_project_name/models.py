from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class DepartmentChoices(models.TextChoices):
    AGR_MANAGEMENT = 'аграрного менеджменту', 'Аграрного менеджменту'
    ECONOMICS = 'економіки', 'Економіки'
    IT = 'інформаційних технологій', 'Інформаційних технологій'

class Students(models.Model):
    Student_ID = models.AutoField(primary_key=True)
    Last_Name = models.CharField(max_length=255)
    First_Name = models.CharField(max_length=255)
    Middle_Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Phone = models.CharField(max_length=15)
    Year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    Department = models.CharField(max_length=50, choices=DepartmentChoices.choices)
    Group_Name = models.CharField(max_length=10)
    Class_Representative = models.BooleanField()

class Subjects(models.Model):
    Subject_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Hours_Per_Semester = models.IntegerField()
    Semesters = models.IntegerField()
    Taught_Over = models.IntegerField()

class Exams(models.Model):
    Exam_ID = models.AutoField(primary_key=True)
    Exam_Date = models.DateField()
    Student_ID = models.ForeignKey(Students, on_delete=models.CASCADE)
    Subject_ID = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    Grade = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(5)])
