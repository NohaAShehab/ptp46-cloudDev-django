from django.db import models

# Create your models here.
"""
    table students
    id, name, grade, age, email, image, gender
"""
"""
    any table generate via model (framework)
    default of table fields not null --> unless say it is null 
"""
class Student(models.Model):
    name = models.CharField(max_length=255)
    grade = models.IntegerField(null=True)
    age = models.IntegerField(default=10)
    email = models.EmailField(null=True, unique=True, blank=True)
    image= models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name}({self.id})"
