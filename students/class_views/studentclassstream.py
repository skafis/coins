from django.shortcuts import render, redirect, get_object_or_404

from students.models import StudentClassStream, SchoolProfiles

from students.forms import StudentClassStreamForm

from django.contrib import messages

from smsgateway.models import PhoneBook

from django.contrib.auth.models import User

#studentclassstream_home page for studentclassstream
def studentclassstream_home(request,template_name='studentclassstream_list.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.view_studentclassstream'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	try:
		rows = StudentClassStream.objects.all()
		ctx = {}
		ctx['rows'] = rows
		ctx['modelfields'] = StudentClassStream._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		rows =  StudentClassStream.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)

#create page for studentclassstream
def studentclassstream_create(request, template_name='studentclassstream_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.add_studentclassstream'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	form = StudentClassStreamForm(request.POST or None)

	if form.is_valid():
		studentprofiles = request.POST['studentprofiles']
		classes = request.POST['classes']
		streams = request.POST['streams']
		entryyear = request.POST['entryyear']

		try:
			name = SchoolProfiles.objects.get(owner_id=request.user.id)
			obj=StudentClassStream(name_id=name.id,studentprofiles_id=studentprofiles,classes_id=classes,streams_id=streams, entryyear_id=entryyear, owner_id=request.user.id)
			obj.save()
		except:
			raise
			messages.add_message(request, messages.INFO, studentclassstream+'already exists ')
		return redirect('students:studentclassstream_home')
	ctx = {}
	ctx['form'] = form
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['span_size'] = 6

	return render(request, template_name, ctx)

#update page for studentclassstream
def studentclassstream_update(request , pk, template_name='studentclassstream_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.change_studentclassstream'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	studentclassstream = get_object_or_404(StudentClassStream, pk=pk)
	form = StudentClassStreamForm(request.POST or None, instance=studentclassstream)
	if form.is_valid():
		try:
			form.save()
		except:
			messages.add_message(request, messages.INFO, 'Cannot update,record already exists ')

		return redirect('students:studentclassstream_home')
	ctx = {}
	ctx['form'] = form
	ctx['studentclassstream'] = studentclassstream
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['pk'] = pk
	ctx['span_size'] = 6
	return render(request, template_name, ctx)

#delete page for studentclassstream
def studentclassstream_delete(request, pk, template_name='studentclassstream_confirm_delete.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.delete_studentclassstream'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	studentclassstream = get_object_or_404(StudentClassStream, pk=pk)    
	if request.method=='POST':
		try:
			studentclassstream.delete()
		except:
			messages.add_message(request, messages.INFO, 'Cannot delete '+studentclassstream+' this record is linked to other data')

		return redirect('students:studentclassstream_home')
	ctx = {}
	ctx['studentclassstream'] = studentclassstream
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	return render(request, template_name, ctx)

