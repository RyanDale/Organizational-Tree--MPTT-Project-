from django.shortcuts import render, redirect,render_to_response,  HttpResponse, HttpResponseRedirect
from orgtree.models import Employee
from orgtree.forms import EmployeeForm

def add_employee(request):
	"""First checks to see if this is a new request or if the user has already tryed to fill out the form. If the form 
	has been correctly filled out the model is saved and the user is redirected to the view structure page. If there 
	were errors then those are returned so the user can fix them."""
	if request.method=='POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/view_structure/')
	else:
		form = EmployeeForm
	return render(request,"add_employee.html",{'form':form})

def view_structure(request):
	"""Returns all of the employee objects to the template so they can be displayed in a tree"""
	return render(request,"view_structure.html",
			{
				'employees':Employee.objects.all()
			})