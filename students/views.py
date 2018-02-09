# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
# Views for students

def students_list(request):
	students = ({
		'id': 1,
		'first_name': 'Андрій',
		'last_name': 'Корост',
		'ticket': 2123,
		'image': 'img/lama.jpg',
		'group': 'IC-11'
		},
		{
		'id': 2,
		'first_name': 'Марія',
		'last_name': 'Струганець',
		'ticket': 1918,
		'image': 'img/mari.jpg',
		'group': 'IC-21'
		},
		{
		'id': 3,
		'first_name': 'Володимир',
		'last_name': 'Струганець',
		'ticket': 1030,
		'image': 'img/volod.jpg',
		'group': 'IC-31'
		})
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for groups

def groups_list(request):
	groups = ({
		'id': 1,
		'groupa': 'IC-11',
		'name': 'Корост Андрій'
		
		},
		{
		'id': 2,
		'groupa': 'IC-21',
		'name': 'Струганець Марія'
		},
		{
		'id': 3,
		'groupa': 'IC-31',
		'name': 'Струганець Володимир'
		})
	return render(request, 'students/groups.html', {"groups": groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)