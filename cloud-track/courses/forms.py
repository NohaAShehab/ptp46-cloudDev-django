from courses.models import Course
from django import forms


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = '__all__' # display all fields except ? created_at, updated_at
        fields = ['name', 'description', 'logo', 'max_grade',
                  'tabs', 'modules', 'students']