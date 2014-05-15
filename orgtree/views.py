from django.shortcuts import get_object_or_404
from orgtree.models import Employee
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from orgtree.forms import EmployeeForm

class EmployeeDetail(DetailView):
    model=Employee
    context_object_name = "employee"
    template_name = "employee_detail.html"
    slug_field = "pk"

    def get_queryset(self):
        return Employee.objects.filter(id=self.kwargs['pk'])

class EmployeeCreate(CreateView):
    model=Employee
    fields = ['name','title','email_address','phone','parent']
    template_name = "employee_form.html"