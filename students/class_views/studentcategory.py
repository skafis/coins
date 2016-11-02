from django.shortcuts import render, redirect, get_object_or_404

from students.models import StudentCategory, SchoolProfiles

from students.forms import StudentCategoryForm


from django.contrib import messages

from django.contrib.auth.models import User

#studentcategory_home page for studentcategory
def studentcategory_home(request,template_name='studentcategory_list.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.view_studentcategory'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	try:
		rows = StudentCategory.objects.all()
		ctx = {}
		ctx['rows'] = rows
		ctx['modelfields'] = StudentCategory._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		rows =  StudentCategory.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)

#create page for studentcategory
def studentcategory_create(request, template_name='studentcategory_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.add_studentcategory'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	form = StudentCategoryForm(request.POST or None)

	if form.is_valid():
		studentprofiles = request.POST['studentprofiles']
		category = request.POST['category']
		entryyear = request.POST['entryyear']
		try:
			name = SchoolProfiles.objects.get(owner_id=request.user.id)
			obj=StudentCategory(name_id=name.id,studentprofiles_id=studentprofiles,category_id=category,entryyear_id=entryyear, owner_id=request.user.id)
			obj.save()
		except:
			raise
			messages.add_message(request, messages.INFO, studentcategory+'already exists ')
		return redirect('students:studentcategory_home')
	ctx = {}
	ctx['form'] = form
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['span_size'] = 6

	return render(request, template_name, ctx)

#update page for studentcategory
def studentcategory_update(request , pk, template_name='studentcategory_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.change_studentcategory'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	studentcategory = get_object_or_404(StudentCategory, pk=pk)
	form = StudentCategoryForm(request.POST or None, instance=studentcategory)
	if form.is_valid():
		try:
			form.save()
		except:
			messages.add_message(request, messages.INFO, 'Cannot update,record already exists ')

		return redirect('students:studentcategory_home')
	ctx = {}
	ctx['form'] = form
	ctx['studentcategory'] = studentcategory
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['pk'] = pk
	ctx['span_size'] = 6
	return render(request, template_name, ctx)

#delete page for studentcategory
def studentcategory_delete(request, pk, template_name='studentcategory_confirm_delete.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('students.delete_studentcategory'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	studentcategory = get_object_or_404(StudentCategory, pk=pk)    
	if request.method=='POST':
		try:
			studentcategory.delete()
		except:
			messages.add_message(request, messages.INFO, 'Cannot delete '+studentcategory+' this record is linked to other data')

		return redirect('students:studentcategory_home')
	ctx = {}
	ctx['studentcategory'] = studentcategory
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	return render(request, template_name, ctx)

