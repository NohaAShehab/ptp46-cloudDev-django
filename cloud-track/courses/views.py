from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from courses.forms import CourseForm
from courses.models import Course
# Create your views here.


def courses_landing(request):
    courses = Course.get_all()
    return render(request, 'courses/landing.html',
                  context={'courses':courses})


def create(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course=form.save()
            return redirect('courses.landing')

    return render(request, 'courses/create.html', {'form':form})


def show(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'courses/show.html', {'course': course})