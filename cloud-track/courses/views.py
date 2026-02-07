from django.shortcuts import render

# Create your views here.


def courses_landing(request):
    # courses =["python", "django", 'Kubernetes', 'jenkins', 'SQL', 'MicroService']
    courses = [
        {
            "id":1, "name":"python", "image":"python.png"
        },
        {
            "id": 2, "name": "Kubernetes", "image": "kubernetes.png"
        },
        {
            "id": 3, "name": "docker", "image": "docker.png"
        }
    ]
    return render(request, 'courses/landing.html',
                  context={'courses':courses})