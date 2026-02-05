from django.shortcuts import render

# Create your views here.


def courses_landing(request):
    courses =["python", "django", 'Kubernetes', 'jenkins', 'SQL', 'MicroService']
    return render(request, 'courses/landing.html',
                  context={'courses':courses})