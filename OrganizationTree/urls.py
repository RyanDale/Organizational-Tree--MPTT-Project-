from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OrganizationTree.views.home', name='home'),
    # url(r'^OrganizationTree/', include('OrganizationTree.foo.urls')),

	url(r'^view_structure/', 'orgtree.views.view_structure', name='View Structure'),
	url(r'^add_employee/', 'orgtree.views.add_employee', name='Add Employee'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
