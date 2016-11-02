from django.shortcuts import render, redirect, get_object_or_404

from students.models import StudentSubject, SchoolProfiles

from students.forms import StudentSubjectForm


from django.contrib import messages

from smsgateway.models import PhoneBook

from django.contrib.auth.models import User

#studentsubject_home page for studentsubject
def studentsubject_home(request,template_name='studentsubject_list.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.view_studentsubject'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	try:
		rows = StudentSubject.objects.all()
		ctx = {}
		ctx['rows'] = rows
		ctx['modelfields'] = StudentSubject._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		rows =  StudentSubject.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)

#create page for studentsubject
def studentsubject_create(request, template_name='studentsubject_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.add_studentsubject'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	form = StudentSubjectForm(request.POST or None)

	if form.is_valid():
		studentprofiles = request.POST['studentprofiles']
		subjects = request.POST['subjects']

		try:
			name = SchoolProfiles.objects.get(owner_id=request.user.id)
			obj=StudentSubject(name_id=name.id,studentprofiles_id=studentprofiles,subjects_id=subjects, owner_id=request.user.id)
			obj.save()
		except:
			raise
			messages.add_message(request, messages.INFO, studentsubject+'already exists ')
		return redirect('students:studentsubject_home')
	ctx = {}
	ctx['form'] = form
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['span_size'] = 6

	return render(request, template_name, ctx)

#update page for studentsubject
def studentsubject_update(request , pk, template_name='studentsubject_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.change_studentsubject'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	studentsubject = get_object_or_404(StudentSubject, pk=pk)
	form = StudentSubjectForm(request.POST or None, instance=studentsubject)
	if form.is_valid():
		try:
			form.save()
		except:
			messages.add_message(request, messages.INFO, 'Cannot update,record already exists ')

		return redirect('students:studentsubject_home')
	ctx = {}
	ctx['form'] = form
	ctx['studentsubject'] = studentsubject
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['pk'] = pk
	ctx['span_size'] = 6
	return render(request, template_name, ctx)

#delete page for studentsubject
def studentsubject_delete(request, pk, template_name='studentsubject_confirm_delete.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.delete_studentsubject'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	studentsubject = get_object_or_404(StudentSubject, pk=pk)    
	if request.method=='POST':
		try:
			studentsubject.delete()
		except:
			messages.add_message(request, messages.INFO, 'Cannot delete '+studentsubject+' this record is linked to other data')

		return redirect('students:studentsubject_home')
	ctx = {}
	ctx['studentsubject'] = studentsubject
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	return render(request, template_name, ctx)

