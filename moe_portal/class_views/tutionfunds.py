from django.shortcuts import render, redirect, get_object_or_404

from moe_portal.models import TutionFunds
from school.models import SchoolProfiles

from moe_portal.forms import TutionFundsForm


from django.contrib import messages

from django.contrib.auth.models import User

#tutionfunds_home page for tutionfunds
def tutionfunds_home(request,template_name):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('moe_portal.view_tutionfunds'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	try:
		rows = TutionFunds.objects.all()
		ctx = {}
		ctx['rows'] = rows
		ctx['modelfields'] = TutionFunds._meta.get_fields()
		ctx['main_title'] = 'TutionFunds'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		rows =  TutionFunds.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)

#tutionfunds_school_list page for studentfees
def tutionfunds_school_list(request,tid,template_name):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('moe_portal.view_tutionfunds'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	try:
		rows = TutionFunds.objects.filter(county=tid)
		ctx = {}
		ctx['form'] = form
		ctx['rows'] = rows
		ctx['tid'] = tid
		ctx['modelfields'] = TutionFunds._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		rows =  TutionFunds.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)


#create page for tutionfunds
def tutionfunds_create(request, template_name='tutionfunds_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('moe_portal.add_tutionfunds'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	form = TutionFundsForm(request.POST or None)

	if form.is_valid():
		name = request.POST['name']
		county = request.POST['county']
		bankname = request.POST['bankname']
		county = request.POST['county']
		sch_bank_acc = request.POST['sch_bank_acc']
		amount = request.POST['amount']
		transactiontype = request.POST['transactiontype']

		try:
			name = SchoolProfiles.objects.get(owner_id=request.user.id)
			obj=TutionFunds(name=name,county=county,bankname=bankname,sch_bank_acc=sch_bank_acc,amount=amount,transactiontype=transactiontype, owner_id=request.user.id)
			obj.save()
		except:
			raise
			messages.add_message(request, messages.INFO, tutionfunds+'already exists ')
		return redirect('moe_portal:tutionfunds_home')
	ctx = {}
	ctx['form'] = form
	ctx['main_title'] = 'TutionFunds'
	ctx['breadcrump'] = 'Manage '
	ctx['span_size'] = 6

	return render(request, template_name, ctx)

#update page for tutionfunds
def tutionfunds_update(request , pk, template_name):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('moe_portal.change_tutionfunds'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	tutionfunds = get_object_or_404(TutionFunds, pk=pk)
	form = TutionFundsForm(request.POST or None, instance=tutionfunds)
	if form.is_valid():
		try:
			form.save()
		except:
			messages.add_message(request, messages.INFO, 'Cannot update,record already exists ')

		return redirect('moe_portal:tutionfunds_home')
	ctx = {}
	ctx['form'] = form
	ctx['tutionfunds'] = tutionfunds
	ctx['main_title'] = 'TutionFunds'
	ctx['breadcrump'] = 'Manage '
	ctx['pk'] = pk
	ctx['span_size'] = 6
	return render(request, template_name, ctx)

#delete page for tutionfunds
def tutionfunds_delete(request, pk, template_name='tutionfunds_confirm_delete.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('moe_portal.delete_tutionfunds'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	tutionfunds = get_object_or_404(TutionFunds, pk=pk)    
	if request.method=='POST':
		try:
			tutionfunds.delete()
		except:
			messages.add_message(request, messages.INFO, 'Cannot delete '+tutionfunds+' this record is linked to other data')

		return redirect('moe_portal:tutionfunds_home')
	ctx = {}
	ctx['tutionfunds'] = tutionfunds
	ctx['main_title'] = 'TutionFunds'
	ctx['breadcrump'] = 'Manage '
	return render(request, template_name, ctx)

