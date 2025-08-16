from django.db import models
import random
import string

import string, random
from django.db import models

class Student(models.Model):
    reg_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, help_text="Leave blank to auto-generate a password.")  # plain text password (not secure!)

    def save(self, *args, **kwargs):
        if not self.password:  # Only generate if no password is set
            chars = string.ascii_letters + string.digits
            self.password = ''.join(random.choice(chars) for _ in range(8))
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.reg_number} - {self.name}"
        

# Course model (optional but useful)
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)  # e.g., "CSC101"

    def __str__(self):
        return f"{self.code} - {self.name}"
    
class Session(models.Model):
    name = models.CharField(max_length=100, help_text="eg 2024/2025")  # e.g., "2024/2025"
    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=20, help_text="eg First semester or Second")  # e.g., "First", "Second"
    def __str__(self):
        return self.name
    
# Result model
class Result(models.Model):
    GRADE_CHOICES = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),
        ("F", "F"),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, blank=True, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)  # e.g., "2024/2025"

    class Meta:
        unique_together = ("student", "course", "semester", "session")

    def __str__(self):
        return f"{self.student.reg_number} - {self.course.code} - {self.score}"
    


