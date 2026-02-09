from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView

from departments.forms import DepartmentForm
from departments.models import Department



# Create your views here.


class DepartmentView(View):
    def get(self, request):
        departments = Department.objects.all()
        return render(request, 'departments/index.html', {'departments': departments})

    # create new object.
    def post(self, request):
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Created")



# generic views ??
# list all departments

class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/index.html'
    context_object_name = 'departments'

    # model --> sort data with id , get
    # def get_queryset(self):
    #     departments = Department.objects.all()

class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/create.html'
    success_url = '/departments/index'



class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'departments/delete.html'
    context_object_name = 'department'
    success_url = '/departments/index'




