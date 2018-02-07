"""podoba_tut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path, re_path

from students import views

urlpatterns = [
    # Students urls
	path('', views.students_list, name='home'),

	path('students/add/', views.students_add, name='students_add'),

	path('students/<sid>/edit/', views.students_edit, name='students_edit'),

	path('students/<sid>/delete/', views.students_delete, name='students_delete'),

	# Groups urls
	path('groups/', views.groups_list, name='groups'),

	path('groups/add/', views.groups_add, name='groups_add'),

	path('groups/<gid>/edit/', views.groups_edit, name='groups_edit'),
	
	path('groups/<gid>/delete/', views.groups_delete, name='groups_delete'),



	# re_path('^admin/', include(admin.site.urls)),

]
