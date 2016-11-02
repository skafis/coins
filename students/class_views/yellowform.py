from django.shortcuts import render, redirect, get_object_or_404

from students.models import YellowForm, SchoolProfiles

from students.forms import YellowFormForm


from django.contrib import messages

from django.contrib.auth.models import User

#yellowform_home page for yellowform
def yellowform_home(request,template_name='yellowform_list.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.view_yellowform'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/', request.path))
	form = YellowFormForm(request.POST or None)
	try:
		rows = YellowForm.objects.all()
		ctx = {}
		ctx['rows'] = rows
		ctx['modelfields'] = YellowForm._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10
		ctx['form'] = form

	except:
		rows =  YellowForm.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)

#create page for yellowform
def yellowform_create(request, template_name='yellowform_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.add_yellowform'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/', request.path))

	form = YellowFormForm(request.POST or None)

	if form.is_valid():

		try:
			form.save()
		except:
			raise
			messages.add_message(request, messages.INFO, yellowform+'already exists ')
		return redirect('students:yellowform_home')
	ctx = {}
	ctx['form'] = form
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['span_size'] = 6

	return render(request, template_name, ctx)

#update page for yellowform
def yellowform_update(request , pk, template_name='yellowform_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.change_yellowform'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/', request.path))

	yellowform = get_object_or_404(YellowForm, pk=pk)
	form = YellowFormForm(request.POST or None, instance=yellowform)
	if form.is_valid():
		try:
			form.save()
		except:
			messages.add_message(request, messages.INFO, 'Cannot update,record already exists ')

		return redirect('students:yellowform_home')
	ctx = {}
	ctx['form'] = form
	ctx['yellowform'] = yellowform
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['pk'] = pk
	ctx['span_size'] = 6
	return render(request, template_name, ctx)

#delete page for yellowform
def yellowform_delete(request, pk, template_name='yellowform_confirm_delete.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.delete_yellowform'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/', request.path))

	yellowform = get_object_or_404(YellowForm, pk=pk)    
	if request.method=='POST':
		try:
			yellowform.delete()
		except:
			messages.add_message(request, messages.INFO, 'Cannot delete '+yellowform+' this record is linked to other data')

		return redirect('students:yellowform_home')
	ctx = {}
	ctx['yellowform'] = yellowform
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	return render(request, template_name, ctx)

