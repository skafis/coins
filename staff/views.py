from django.shortcuts import render

import staff.class_views.staffprofiles as staffprofiles
import staff.class_views.staffphoneno as staffphoneno

#STAFF PROFILES
def staffprofiles_home(request,template_name='staff/staffprofiles_list.html'):
 return staffprofiles.staffprofiles_home(request,template_name='staff/staffprofiles_list.html')

def staffprofiles_create(request, template_name='staff/staffprofiles_form.html'):
	return staffprofiles.staffprofiles_create(request, template_name='staff/staffprofiles_form.html')

def staffprofiles_update(request , pk, template_name='staff/staffprofiles_form.html'):
	return staffprofiles.staffprofiles_update(request , pk, template_name='staff/staffprofiles_form.html')

def staffprofiles_delete(request, pk, template_name='staff/staffprofiles_confirm_delete.html'):
	return staffprofiles.staffprofiles_delete(request, pk, template_name='staff/staffprofiles_confirm_delete.html')

#STAFF PROFILES
def staffphoneno_home(request,template_name='staff/staffphoneno_list.html'):
 return staffphoneno.staffphoneno_home(request,template_name='staff/staffphoneno_list.html')

def staffphoneno_create(request, template_name='staff/staffphoneno_form.html'):
	return staffphoneno.staffphoneno_create(request, template_name='staff/staffphoneno_form.html')

def staffphoneno_update(request , pk, template_name='staff/staffphoneno_form.html'):
	return staffphoneno.staffphoneno_update(request , pk, template_name='staff/staffphoneno_form.html')

def staffphoneno_delete(request, pk, template_name='staff/staffphoneno_confirm_delete.html'):
	return staffphoneno.staffphoneno_delete(request, pk, template_name='staff/staffphoneno_confirm_delete.html')

