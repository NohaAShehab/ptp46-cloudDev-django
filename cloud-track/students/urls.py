from django.urls import path

from students.views import hello, students_index, student_profile, landing

urlpatterns = [
    path('hello', hello, name='hello.test'),
    path('index/', students_index, name='students.index'),
    # path('index/<id>', student_profile, name='students.profile'),
    path('index/<int:id>', student_profile, name='students.profile'),
    path('landing/', landing, name='students.landing'),
]
