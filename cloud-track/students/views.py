from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from students.models import  Student
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

    # get students from database then send it to the template
    # select * from students_student;  # based dbms >>> mysql -->pk, postgres --> last update
    # students  = Student.objects.all().order_by('id')
    students= Student.get_all()

    # <QuerySet [<Student: noha(1)>, <Student: noha__(2)>, <Student: new(4)>, <Student: new(3)>]>
    print(students)
    return render(request, 'students/index.html',
                  context={'students': students})







def show(request, id ):
    student = Student.objects.get(id=id)  # one object
    print(student)
    return render(request, 'students/show.html', context={'student': student})



# def delete(request, id):
#     # check if object exists ---> delete it if not return 404
#     try:
#         student = Student.objects.get(id=id)
#         student.delete()
#         return redirect("students.index")
#     except Exception as e:
#         return redirect("students.index")

def delete(request, id):
    deleted = Student.delete_object_by_id(id )
    print(deleted)
    # student = get_object_or_404(Student, id=id)
    # student.delete()
    return redirect("students.index")



def create(request):
    print(request) # info about request
    if request.method == "POST":
        # check data sent in the request body
        print(request.POST)
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        grade = request.POST['grade']
        image = request.POST['image']
        gender = request.POST['gender']
        student = Student(name=name, age=age, email=email, grade=grade, image=image,
                          gender=gender)
        student.save()


        # return HttpResponse('Student created successfully')
        return redirect(student.show_url)

    return render(request, 'students/create.html')