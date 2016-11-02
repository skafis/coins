from django.shortcuts import render

import smsgateway.class_views.phonebook as phonebook
import smsgateway.class_views.sms as sms

#PHONEBOOK
def phonebook_home(request,template_name='smsgateway/phonebook_list.html'):
 return phonebook.phonebook_home(request,template_name='smsgateway/phonebook_list.html')

def phonebook_create(request, template_name='smsgateway/phonebook_form.html'):
	return phonebook.phonebook_create(request, template_name='smsgateway/phonebook_form.html')

def phonebook_update(request , pk, template_name='smsgateway/phonebook_form.html'):
	return phonebook.phonebook_update(request , pk, template_name='smsgateway/phonebook_form.html')

def phonebook_delete(request, pk, template_name='smsgateway/phonebook_confirm_delete.html'):
	return phonebook.phonebook_delete(request, pk, template_name='smsgateway/phonebook_confirm_delete.html')

#SMS
def sms_home(request,template_name='smsgateway/sms_list.html'):
 return sms.sms_home(request,template_name='smsgateway/sms_list.html')

def sms_create(request, template_name='smsgateway/sms_form.html'):
	return sms.sms_create(request, template_name='smsgateway/sms_form.html')

def sms_update(request , pk, template_name='smsgateway/sms_form.html'):
	return sms.sms_update(request , pk, template_name='smsgateway/sms_form.html')

def sms_delete(request, pk, template_name='smsgateway/sms_confirm_delete.html'):
	return sms.sms_delete(request, pk, template_name='smsgateway/sms_confirm_delete.html')
