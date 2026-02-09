from django.db import models
from students.models import Student
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    logo = models.ImageField(upload_to='courses/images/', null=True, blank=True)
    max_grade = models.IntegerField(default=100)
    modules = models.IntegerField(default=2)
    tabs = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    # create relationship table, and creation multi-select drop field in templates , admin board
    # access students related to this course course.students.all (in template )
    # backword relation --> if you have an object from student ==> you can get relationship objects
    students = models.ManyToManyField(Student, related_name='courses',
                                      null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('id')

    @property
    def image_url(self):
        return f"/media/{self.logo}" if self.logo else None
