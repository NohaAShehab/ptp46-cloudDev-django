"""
URL configuration for iti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from students.views import hello, students_index, student_profile, landing
from courses.views import courses_landing

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # ___________ students
    # path('hello', hello, name='hello.test'),
    # path('index/', students_index, name='students.index'),
    # # path('index/<id>', student_profile, name='students.profile'),
    # path('index/<int:id>', student_profile, name='students.profile'),
    # path('landing/', landing, name='students.landing'),
    path('students/', include('students.urls')),
    # courses
    # path('courses/', courses_landing, name='courses.index'),
    path('courses/', include('courses.urls')),
]
