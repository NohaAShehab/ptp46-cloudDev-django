
from django.urls import path

from courses.views import courses_landing

urlpatterns = [
    # courses
    path('landing', courses_landing, name='courses.index'),
]
