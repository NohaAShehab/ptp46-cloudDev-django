
from django.urls import path

from courses.views import courses_landing, create, show

urlpatterns = [
    # courses
    path('landing', courses_landing, name='courses.landing'),
    path('create', create, name='courses.create'),
    path('show/<int:id>/', show, name='courses.show'),
]
