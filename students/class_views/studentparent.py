from django.shortcuts import render, redirect, get_object_or_404

from students.models import StudentParent, SchoolProfiles

from students.forms import StudentParentForm


from django.contrib import messages

from django.contrib.auth.models import User

#studentparent_home page for studentparent
def studentparent_home(request,template_name='studentparent_list.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.view_studentparent'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	try:
		rows = StudentParent.objects.all()
		ctx = {}
		ctx['rows'] = rows
		ctx['modelfields'] = StudentParent._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		rows =  StudentParent.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)

#create page for studentparent
def studentparent_create(request, template_name='studentparent_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.add_studentparent'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	form = StudentParentForm(request.POST or None)

	if form.is_valid():
		studentprofiles = request.POST['studentprofiles']
		username = request.POST['username']
		firstname = request.POST['firstname']
		secondname = request.POST['secondname']
		lastname = request.POST['lastname']
		gender = request.POST['gender']
		specialcases = request.POST['specialcases']

		try:
			name = SchoolProfiles.objects.get(owner_id=request.user.id)
			obj=StudentParent(name_id=name.id,studentprofiles_id=studentprofiles,user_id=username,firstname=firstname, secondname=secondname,lastname=lastname,gender=gender,specialcases=specialcases, owner_id=request.user.id)
			obj.save()
		except:
			raise
			messages.add_message(request, messages.INFO, studentparent+'already exists ')
		return redirect('students:studentparent_home')
	ctx = {}
	ctx['form'] = form
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['span_size'] = 6

	return render(request, template_name, ctx)

#update page for studentparent
def studentparent_update(request , pk, template_name='studentparent_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.change_studentparent'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	studentparent = get_object_or_404(StudentParent, pk=pk)
	form = StudentParentForm(request.POST or None, instance=studentparent)
	if form.is_valid():
		try:
			form.save()
		except:
			messages.add_message(request, messages.INFO, 'Cannot update,record already exists ')

		return redirect('students:studentparent_home')
	ctx = {}
	ctx['form'] = form
	ctx['studentparent'] = studentparent
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['pk'] = pk
	ctx['span_size'] = 6
	return render(request, template_name, ctx)

#delete page for studentparent
def studentparent_delete(request, pk, template_name='studentparent_confirm_delete.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.delete_studentparent'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	studentparent = get_object_or_404(StudentParent, pk=pk)    
	if request.method=='POST':
		try:
			studentparent.delete()
		except:
			messages.add_message(request, messages.INFO, 'Cannot delete '+studentparent+' this record is linked to other data')

		return redirect('students:studentparent_home')
	ctx = {}
	ctx['studentparent'] = studentparent
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	return render(request, template_name, ctx)

