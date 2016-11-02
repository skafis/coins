from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages

def index(request):
	ctx = {}
	try:
		rows=User.objects.all()
		ctx['rows'] = rows
		ctx['main_title'] = 'Ministry of education'
		ctx['breadcrump'] = 'Ministry of education'
		ctx['span_size'] = 12
	except:
		#raise
		#messages.add_message(request, messages.INFO, 'Record already exists ')
		pass
	return render(request, 'moe_portal/index.html', ctx)

def moe(request):
	ctx = {}
	try:
		rows=User.objects.all()
		ctx['rows'] = rows
		ctx['main_title'] = 'Ministry of education'
		ctx['breadcrump'] = 'Ministry of education'
		ctx['span_size'] = 12
	except:
		#raise
		#messages.add_message(request, messages.INFO, 'Record already exists ')
		pass
	return render(request, 'moe_portal/register.html', ctx)
