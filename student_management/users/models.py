from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

# Student Profile Model
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    grade = models.CharField(max_length=2, blank=True,default= "A")  # Grade field for students
    attendance = models.CharField(max_length=3,blank=True,default=0)

    def __str__(self):
        return f"{self.user.username} - {self.grade}"