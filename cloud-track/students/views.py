from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# what is view --> action will be called when you receive http request

# 1- views --> as a function
# def hello(request): # handle http request
#     ## must return with http response
#     return HttpResponse("Hello, world.")

def hello(request): # handle http request
    ## must return with http response
    return HttpResponse("<h1 style='color:red; text-align:center'> Hello, world.</h1>")


students = [
    {'id':1, 'name': 'ahmed', 'age': 25},
    {'id':2 , 'name': 'ali', 'age': 25},
    {'id':3, 'name':'abc', 'age':23}
]

def students_index(request):
    return HttpResponse(students)

"""
def student_profile(request, id):
    print(request)
    try:
        id = int(id)
        # loop over list --> get dict  --> id = id
        filter_student = list(filter(lambda student: student['id'] == id, students))
        print(filter_student)
        if filter_student:
            student_data = f"id: {id}, name: {filter_student[0]['name']}, age: {filter_student[0]['age']}"
            return HttpResponse(student_data)
        else:
            return HttpResponse("====Student not found===")
    except Exception as e:
        print(e)
        return HttpResponse("No student with the given id ")

"""

def student_profile(request, id):
        # loop over list --> get dict  --> id = id
    filter_student = list(filter(lambda student: student['id'] == id, students))
    print(filter_student)
    if filter_student:
        student_data = f"id: {id}, name: {filter_student[0]['name']}, age: {filter_student[0]['age']}"
        return HttpResponse(student_data)
    else:
        return HttpResponse("====Student not found===")



def landing(request):
    # return HttpResponse("Landing page")
    return render(request, 'students/landing.html')





def index(request):
    return render(request, 'students/index.html',
                  context={'students': students})





