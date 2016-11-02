from django.shortcuts import render, redirect, get_object_or_404

from students.models import ParentPhoneNo, SchoolProfiles

from students.forms import ParentPhoneNoForm


from django.contrib import messages

from smsgateway.models import PhoneBook

from django.contrib.auth.models import User

#parentphoneno_home page for parentphoneno
def parentphoneno_home(request,template_name='parentphoneno_list.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.view_parentphoneno'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	try:
		rows = ParentPhoneNo.objects.all()
		ctx = {}
		ctx['rows'] = rows
		ctx['modelfields'] = ParentPhoneNo._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		rows =  ParentPhoneNo.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)

#create page for parentphoneno
def parentphoneno_create(request, template_name='parentphoneno_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.add_parentphoneno'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	form = ParentPhoneNoForm(request.POST or None)

	if form.is_valid():
		parent = request.POST['parent']
		phoneno = request.POST['phoneno']

		try:
			name = SchoolProfiles.objects.get(owner_id=request.user.id)
			obj=ParentPhoneNo(name_id=name.id,parent_id=parent,phoneno_id=phoneno, owner_id=request.user.id)
			obj.save()
		except:
			raise
			messages.add_message(request, messages.INFO, parentphoneno+'already exists ')
		return redirect('students:parentphoneno_home')
	ctx = {}
	ctx['form'] = form
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['span_size'] = 6

	return render(request, template_name, ctx)

#update page for parentphoneno
def parentphoneno_update(request , pk, template_name='parentphoneno_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.change_parentphoneno'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	parentphoneno = get_object_or_404(ParentPhoneNo, pk=pk)
	form = ParentPhoneNoForm(request.POST or None, instance=parentphoneno)
	if form.is_valid():
		try:
			form.save()
		except:
			messages.add_message(request, messages.INFO, 'Cannot update,record already exists ')

		return redirect('students:parentphoneno_home')
	ctx = {}
	ctx['form'] = form
	ctx['parentphoneno'] = parentphoneno
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['pk'] = pk
	ctx['span_size'] = 6
	return render(request, template_name, ctx)

#delete page for parentphoneno
def parentphoneno_delete(request, pk, template_name='parentphoneno_confirm_delete.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.delete_parentphoneno'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	parentphoneno = get_object_or_404(ParentPhoneNo, pk=pk)    
	if request.method=='POST':
		try:
			parentphoneno.delete()
		except:
			messages.add_message(request, messages.INFO, 'Cannot delete '+parentphoneno+' this record is linked to other data')

		return redirect('students:parentphoneno_home')
	ctx = {}
	ctx['parentphoneno'] = parentphoneno
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	return render(request, template_name, ctx)

