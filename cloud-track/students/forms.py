

from django import forms

from students.models import Student


class StudentForm(forms.Form):
    name = forms.CharField(label="Student Name", max_length=100)
    email = forms.EmailField(label="Student Email", max_length=100)
    age = forms.IntegerField(label="Student Age")
    grade = forms.IntegerField(label="Student Grade")
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    image = forms.ImageField()

    # any logic related to the form ??
    def clean_email(self):
        email = self.cleaned_data['email']
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("Student with this email already exists")
        return email

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18 or age > 25:
            raise forms.ValidationError("Student Age must be greater than 18 and < 25")
        return age

    def clean_gender(self):
        gender = self.cleaned_data['gender']
        if gender not in ['M', 'F']:
            raise forms.ValidationError("Student Gender must be either M or F")
        return gender


    # check size,extension of image



class StudentModelForm(forms.ModelForm):
    # use model to create form  --> fields with its basic validation based on
    # information given by model ??
    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'gender', 'image', 'grade']

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18 or age > 25:
            raise forms.ValidationError("Student Age must be greater than 18 and < 25")
        return age