from django.urls import path

from students.views import (hello, students_index, student_profile, landing,
                            index, show, delete, create)

urlpatterns = [
    path('hello', hello, name='students.hello'),
    path('std/', students_index, name='std.index'),
    # path('index/<id>', student_profile, name='students.profile'),
    path('index/<int:id>', student_profile, name='students.profile'),
    path('landing/', landing, name='students.landing'),
    path('index', index, name='students.index'),
    path('show/<int:id>', show, name='students.show'),
    path('delete/<int:id>', delete, name='students.delete'),
    path('create', create, name='students.create'),

]
