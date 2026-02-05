from django.urls import path

from students.views import hello, students_index, student_profile, landing, index

urlpatterns = [
    path('hello', hello, name='students.hello'),
    path('std/', students_index, name='std.index'),
    # path('index/<id>', student_profile, name='students.profile'),
    path('index/<int:id>', student_profile, name='students.profile'),
    path('landing/', landing, name='students.landing'),
    path('index', index, name='students.index'),
]
