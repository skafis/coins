from django.shortcuts import render, redirect, get_object_or_404

from staff.models import StaffPhoneNo

from staff.forms import StaffPhoneNoForm


from django.contrib import messages

from smsgateway.models import PhoneBook

from django.contrib.auth.models import User

#staffphoneno_home page for staffphoneno
def staffphoneno_home(request,template_name='staffphoneno_list.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('staff.view_staffphoneno'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/', request.path))

	try:
		rows = StaffPhoneNo.objects.all()
		ctx = {}
		ctx['rows'] = rows
		ctx['modelfields'] = StaffPhoneNo._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		rows =  StaffPhoneNo.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)

#create page for staffphoneno
def staffphoneno_create(request, template_name='staffphoneno_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('staff.add_staffphoneno'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/', request.path))

	form = StaffPhoneNoForm(request.POST or None)

	if form.is_valid():
		staffprofiles = request.POST['staffprofiles']
		phoneno = request.POST['phoneno']

		try:
			name = Hospitals.objects.get(owner_id=request.user.id)
			obj=StaffPhoneNo(name_id=name.id,staffprofiles_id=staffprofiles,phoneno_id=phoneno, owner_id=request.user.id)
			obj.save()
		except:
			raise
			messages.add_message(request, messages.INFO, staffphoneno+'already exists ')
		return redirect('staff:staffphoneno_home')
	ctx = {}
	ctx['form'] = form
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['span_size'] = 6

	return render(request, template_name, ctx)

#update page for staffphoneno
def staffphoneno_update(request , pk, template_name='staffphoneno_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('staff.change_staffphoneno'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/', request.path))

	staffphoneno = get_object_or_404(StaffPhoneNo, pk=pk)
	form = StaffPhoneNoForm(request.POST or None, instance=staffphoneno)
	if form.is_valid():
		try:
			form.save()
		except:
			messages.add_message(request, messages.INFO, 'Cannot update,record already exists ')

		return redirect('staff:staffphoneno_home')
	ctx = {}
	ctx['form'] = form
	ctx['staffphoneno'] = staffphoneno
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['pk'] = pk
	ctx['span_size'] = 6
	return render(request, template_name, ctx)

#delete page for staffphoneno
def staffphoneno_delete(request, pk, template_name='staffphoneno_confirm_delete.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('staff.delete_staffphoneno'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/', request.path))

	staffphoneno = get_object_or_404(StaffPhoneNo, pk=pk)    
	if request.method=='POST':
		try:
			staffphoneno.delete()
		except:
			messages.add_message(request, messages.INFO, 'Cannot delete '+staffphoneno+' this record is linked to other data')

		return redirect('staff:staffphoneno_home')
	ctx = {}
	ctx['staffphoneno'] = staffphoneno
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	return render(request, template_name, ctx)

