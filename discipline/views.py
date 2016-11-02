from django.shortcuts import render

import discipline.class_views.disciplinecases as disciplinecases


#DISCPLINE
def disciplinecases_home(request,template_name='discipline/disciplinecases_list.html'):
 return disciplinecases.disciplinecases_home(request,template_name=template_name)

def disciplinecases_single_list(request,tid,template_name='discipline/disciplinecases_list.html'):
 return disciplinecases.disciplinecases_single_list(request,tid,template_name=template_name)

def disciplinecases_create(request, template_name='discipline/create_update_form.html'):
	return disciplinecases.disciplinecases_create(request, template_name=template_name)

def disciplinecases_update(request , pk, template_name='discipline/create_update_form.html'):
	return disciplinecases.disciplinecases_update(request , pk, template_name=template_name)

def disciplinecases_delete(request, pk, template_name='discipline/confirm_delete.html'):
	return disciplinecases.disciplinecases_delete(request, pk, template_name=template_name)

