from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

"""The Employee class stores useful contact information for each Employee.
	It also stores who the employee reports to (parent).

    Attributes:
        name: The employee's first and last name
        title: The employee's job title
        email_address: The employee's email address
        phone: The employee's phone number
        parent: The employee's supervisor. Can be null if employee doesn't 
        	report to another employee (i.e. CEO)
"""
class Employee(MPTTModel):
	name=models.CharField(max_length=30)
	title=models.CharField(max_length=30)
	email_address=models.EmailField(max_length=75)
	phone=models.CharField(max_length=20)
	parent=TreeForeignKey('self', null=True, blank=True, related_name='children')

	def __unicode__(self):
		return "%s" % self.name

	class MPTTMeta:
		order_insertion_by = ['name']