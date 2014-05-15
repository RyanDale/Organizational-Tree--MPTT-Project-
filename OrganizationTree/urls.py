from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.views.generic import list_detail
from orgtree.models import Employee
from orgtree.views import EmployeeCreate, EmployeeDetail

orgstructure_data = {
    "queryset":Employee.objects.all(),
    "template_name":"view_structure.html",
}

urlpatterns = patterns('',
	url(r'^employee_detail/(?P<pk>.*?)/$', EmployeeDetail.as_view(), name="employee_detail"),
	url(r'^view_structure/', list_detail.object_list, orgstructure_data, name='view_structure'),
	url(r'^add_employee/', EmployeeCreate.as_view(), name='add_employee'),
    url(r'^admin/', include(admin.site.urls)),
)
