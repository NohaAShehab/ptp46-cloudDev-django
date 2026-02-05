from django.shortcuts import render

# Create your views here.


def courses_landing(request):
    return render(request, 'courses/landing.html')