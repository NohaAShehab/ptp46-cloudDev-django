from django.urls import path

from students.views import (hello, students_index, student_profile, landing,
                            index, show, delete, create, create_via_form,
                            create_via_model_form)

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
    path('create/form', create_via_form, name='students.create.form'),
    path('create/form-model', create_via_model_form, name='students.create.form.model'),

]
