from django.shortcuts import render, redirect, get_object_or_404

from smsgateway.models import Sms, SchoolProfiles

from smsgateway.forms import SmsForm

from smsgateway.forms import SmsFilterForm

from django.contrib import messages

from django.contrib.auth.models import User

#sms_home page for sms
def sms_home(request,template_name='sms_list.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('smsgateway.view_sms'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	form = SmsFilterForm(request.POST or None)
	try:
		rows = Sms.objects.all()
		ctx = {}
		ctx['form'] = form
		ctx['rows'] = rows
		ctx['modelfields'] = Sms._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		rows =  Sms.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)

#create page for sms
def sms_create(request, template_name='sms_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('smsgateway.add_sms'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	form = SmsForm(request.POST or None)

	if form.is_valid():
		smstype = request.POST['smstype']
		sms = request.POST['sms']
		try:
			name = SchoolProfiles.objects.get(owner_id=request.user.id)
			obj=Sms(name_id=name.id,sms_id=sms,smstype_id=smstype,owner_id=request.user.id)
			obj.save()
		except:
			raise
			messages.add_message(request, messages.INFO, sms+'already exists '+smstype+' '+sms)
		return redirect('smsgateway:sms_home')
	ctx = {}
	ctx['form'] = form
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['span_size'] = 6

	return render(request, template_name, ctx)

#update page for sms
def sms_update(request , pk, template_name='sms_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('smsgateway.change_sms'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	sms = get_object_or_404(Sms, pk=pk)
	form = SmsForm(request.POST or None, instance=sms)
	if form.is_valid():
		try:
			form.save()
		except:
			messages.add_message(request, messages.INFO, 'Cannot update,record already exists ')

		return redirect('smsgateway:sms_home')
	ctx = {}
	ctx['form'] = form
	ctx['sms'] = sms
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['pk'] = pk
	ctx['span_size'] = 6
	return render(request, template_name, ctx)

#delete page for sms
def sms_delete(request, pk, template_name='sms_confirm_delete.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('smsgateway.delete_sms'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	sms = get_object_or_404(Sms, pk=pk)    
	if request.method=='POST':
		try:
			sms.delete()
		except:
			messages.add_message(request, messages.INFO, 'Cannot delete '+sms+' this record is linked to other data')

		return redirect('smsgateway:sms_home')
	ctx = {}
	ctx['sms'] = sms
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	return render(request, template_name, ctx)

