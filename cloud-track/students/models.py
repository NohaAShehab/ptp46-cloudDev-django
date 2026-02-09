from django.db import models
from django.shortcuts import reverse , get_object_or_404

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
    # image = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='students/images', null=True, blank=True)
    gender = models.CharField(null=True, blank=True, choices=[("M", "Male"), ("F", "Female")])
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f"{self.name}({self.id})"

    # model object contain info about object
    @property
    def show_url(self):
        # self represent current object model --> id
        # students.show and accept param ? self.id
        url = reverse("students.show", args=[self.id])
        return url

    @property
    def delete_url(self):
        delete_url = reverse("students.delete", args=[self.id])
        return delete_url

    @property
    def image_url(self):
        return f"/media/{self.image}"


    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('id')


    @classmethod
    def delete_object_by_id(cls, id):
        student = get_object_or_404(cls, id=id)
        student.delete()
        return True