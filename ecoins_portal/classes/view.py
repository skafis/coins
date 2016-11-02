from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages

from pos_portal.models import Pos,Merchants
from pos_portal.models import Transactions

from pos_portal.forms import SchoolForm
from sysadmin.forms import SchoolDropdownForm

from django.http import Http404, HttpResponse
import json

from school.models import SchoolProfiles

from students.models import StudentProfiles

def index(request):
	ctx = {}
	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		#pos = Pos.objects.all().values('id','posnumber','accountnumber','serialnum','merchant_id__firstname','merchant_id__name__schname')
		#data = {'pos': list(pos)}
		transactions = Transactions.objects.all().values('id','transaction_type','amount','trace_no','ref_no','currency','location','terminal_id__posnumber','terminal_id__accountnumber','terminal_id__merchant_id__firstname', 'location_id__schname','wallet_id__studentprofiles_id__accountnumber','wallet_id__walletname_name','reverse').distinct('location')
		transactionspos = Transactions.objects.all().values('id','terminal__posnumber','terminal__accountnumber','terminal__serialnum','location_id__schname','terminal_id__merchant_id__firstname','balance','reverse',)
		posmerchantecoinsportal = Merchants.objects.all().values('id','name__schname','firstname','secondname','lastname','phonenumber','email','username__username')
		ecoins_portalschools = SchoolProfiles.objects.all().values('id','schname')
		ecoins_portalstudentprofiles = StudentProfiles.objects.all().values('name__schname','admno','username__username','firstname','secondname','lastname','gender__gender__gender','current_classes__classes__classes','current_stream__streams__stream','accountnumber','encryped_acc_no',)
		data = {'transactions': list(transactions),'transactionspos': list(transactionspos),'posmerchantecoinsportal': list(posmerchantecoinsportal),'ecoins_portalschools': list(ecoins_portalschools),'ecoins_portalstudentprofiles': list(ecoins_portalstudentprofiles),}
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		#rows = Pos.objects.all()
		#ctx['rows'] = rows
		ctx['main_title'] = 'Ecoins'
		ctx['breadcrump'] = 'Ecoins'
		ctx['span_size'] = 12

		return render(request, 'ecoins_portal/index.html', ctx)


def pos(request):
	ctx = {}
	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		#pos = Pos.objects.all().values('id','posnumber','accountnumber','serialnum','merchant_id__firstname','merchant_id__name__schname')
		#data = {'pos': list(pos)}
		transactions = Transactions.objects.all().values('id','terminal__posnumber','terminal__accountnumber','terminal__serialnum','location_id__schname','terminal_id__merchant_id__firstname','balance','reverse',)
		data = {'transactions': list(transactions)}
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		#rows = Pos.objects.all()
		#ctx['rows'] = rows
		ctx['main_title'] = 'Ecoins'
		ctx['breadcrump'] = 'Ecoins'
		ctx['span_size'] = 12

		return render(request, 'ecoins_portal/pos.html', ctx)

def pos_by_schools(request):
	ctx = {}
	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		#pos = Pos.objects.all().values('id','posnumber','accountnumber','serialnum','merchant_id__firstname','merchant_id__name__schname')
		#data = {'pos': list(pos)}
		transactions = Transactions.objects.all().values('id','transaction_type','amount','trace_no','ref_no','currency','location','terminal_id__posnumber','terminal_id__accountnumber','terminal_id__merchant_id__firstname', 'location_id__schname','wallet_id__studentprofiles_id__accountnumber','wallet_id__walletname_name','reverse').distinct('location') #'id','name','studentprofiles','accountnumber','encryped_acc_no','bank_name','expirerydate',)
		data = {'transactions': list(transactions),}
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		#rows = Pos.objects.all()
		#ctx['rows'] = rows
		ctx['main_title'] = 'Ecoins'
		ctx['breadcrump'] = 'Ecoins'
		ctx['span_size'] = 12

		return render(request, 'ecoins_portal/pos_by_schools.html', ctx)

def pos_by_posname(request,pk):
	ctx = {}
	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		#pos = Pos.objects.all().values('id','posnumber','accountnumber','serialnum','merchant_id__firstname','merchant_id__name__schname')
		#data = {'pos': list(pos)}
		transactions = Transactions.objects.filter(location_id=pk).values('id','transaction_type','amount','trace_no','ref_no','currency','location','terminal_id__posnumber','terminal_id__accountnumber','terminal_id__merchant_id__firstname', 'location_id__schname','wallet_id__studentprofiles_id__accountnumber','wallet_id__walletname_name','reverse') #'id','name','studentprofiles','accountnumber','encryped_acc_no','bank_name','expirerydate',)
		data = {'transactions': list(transactions)}
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		#rows = Pos.objects.all()
		#ctx['rows'] = rows
		ctx['main_title'] = 'Ecoins'
		ctx['breadcrump'] = 'Ecoins'
		ctx['span_size'] = 12

		return render(request, 'ecoins_portal/pos_by_posname.html', ctx)


def pos_transactions(request):
	ctx = {}
	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		#pos = Pos.objects.all().values('id','posnumber','accountnumber','serialnum','merchant_id__firstname','merchant_id__name__schname')
		#data = {'pos': list(pos)}
		transactions = Transactions.objects.all().values('id','transaction_type','amount','trace_no','ref_no','currency','location','terminal_id__posnumber','terminal_id__accountnumber','terminal_id__merchant_id__firstname', 'location_id__schname','wallet_id__studentprofiles_id__accountnumber','wallet_id__walletname_name','reverse').distinct('location') #'id','name','studentprofiles','accountnumber','encryped_acc_no','bank_name','expirerydate',)
		data = {'transactions': list(transactions)}
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		#rows = Pos.objects.all()
		#ctx['rows'] = rows
		ctx['main_title'] = 'Ecoins'
		ctx['breadcrump'] = 'Ecoins'
		ctx['span_size'] = 12

		return render(request, 'ecoins_portal/pos_by_schools.html', ctx)



def merchant(request):
	schform = SchoolDropdownForm(request.POST or None)
	ctx = {}
	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		merchants = Merchants.objects.all().values('id','name__schname','firstname','secondname','lastname','phonenumber','email','username__username')
		#data = json.dumps(list(obj))
		data = {'merchants': list(merchants)}
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'Merchants Register'
		ctx['breadcrump'] = 'Merchants Register'
		ctx['schform'] = schform
		ctx['span_size'] = 12
		return render(request, 'ecoins_portal/merchant.html', ctx)


def pos_create(request):
	if request.is_ajax() and request.POST:
		posnumber= request.POST.get('posnumber')
		posaccountnumber= request.POST.get('posaccountnumber')
		posserialnum= request.POST.get('posserialnum')

		try:
			sp=Pos(name=1,posnumber=posnumber,accountnumber=posaccountnumber,serialnum=posserialnum)
			sp.save()
			data = {'message': "%s Saved "%(posnumber),'id': sp.id,'schoolname':posnumber,'posaccountnumber':posaccountnumber,'posserialnum':posserialnum}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(schoolname)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def transactions(request):
	ctx = {}

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		#schools = SchoolProfiles.objects.all().values('id','schname')
		studentprofiles = StudentProfiles.objects.all().values('name__schname','admno','username__username','firstname','secondname','lastname','gender__gender','current_classes__classes','current_stream__streams',)

		#data = json.dumps(list(obj))
		data = {'schools': list(schools),'studentprofiles': list(studentprofiles),}

		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'POS Transactions'
		ctx['breadcrump'] = 'POS Transactions'
		ctx['span_size'] = 12

		return render(request, 'ecoins_portal/postransactions.html', ctx)

def merchant_create(request):
	if request.is_ajax() and request.POST:
		posnumber= request.POST.get('posnumber')
		posaccountnumber= request.POST.get('posaccountnumber')
		posserialnum= request.POST.get('posserialnum')
		schoolprofiles= request.POST.get('schoolprofiles')
		firstname= request.POST.get('firstname')
		secondname= request.POST.get('secondname')
		lastname= request.POST.get('lastname')
		phonenumber= request.POST.get('phonenumber')
		email= request.POST.get('email')

		try:
			obj = User.objects.create_user(username=firstname, password=firstname)
			obj.save()
			obj.first_name=firstname
			obj.last_name=lastname
			obj.is_active=True
			obj.email=email
			obj.is_staff=True
			obj.save()

			sp=Merchants(name_id=schoolprofiles,firstname=firstname,secondname=secondname,lastname=lastname,phonenumber=phonenumber,email=email,username_id=obj.id)
			sp.save()

			p=Pos(merchant_id=sp.pk,posnumber=posnumber,accountnumber=posaccountnumber,serialnum=posserialnum)
			p.save()

			data = {'message': "%s Saved "%(posnumber),'id': sp.id,'schoolname':posnumber,'posaccountnumber':posaccountnumber,'posserialnum':posserialnum}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(schoolname)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404
