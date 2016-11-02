from django.shortcuts import render, redirect, get_object_or_404

from discipline.models import DisciplineCases

from school.models import SchoolProfiles

from discipline.forms import DisciplineCasesForm


from django.contrib import messages
from django.contrib.auth.models import User


#disciplinecases_home page for disciplinecases
def disciplinecases_home(request,template_name):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('disciplinecases.view_disciplinecases'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	try:
		rows = DisciplineCases.objects.all().distinct('studentprofiles')
		ctx = {}
		ctx['rows'] = rows
		ctx['modelfields'] = DisciplineCases._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		rows =  DisciplineCases.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)

#disciplinecases_single_list page for disciplinecases
def disciplinecases_single_list(request,tid,template_name):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('finance.view_disciplinecases'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	try:
		rows = DisciplineCases.objects.filter(studentprofiles_id=tid)
		ctx = {}
		ctx['rows'] = rows
		ctx['tid'] = tid
		ctx['modelfields'] = DisciplineCases._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		rows =  DisciplineCases.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)


#create page for disciplinecases
def disciplinecases_create(request, template_name):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('disciplinecases.add_disciplinecases'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	form = DisciplineCasesForm(request.POST or None)

	if form.is_valid():
		studentprofiles = request.POST['studentprofiles']
		blacklist = request.POST['blacklist']
		blacklistdate = request.POST['blacklistdate']
		whitelist = request.POST['whitelist']
		whitelistdate = request.POST['whitelistdate']

		try:
			name = SchoolProfiles.objects.get(owner_id=request.user.id)

			obj=DisciplineCases(name_id=name.id,studentprofiles_id=studentprofiles,blacklist=blacklist,blacklistdate=blacklistdate, whitelist=whitelist,whitelistdate=whitelistdate,owner_id=request.user.id)
			obj.save()

		except:
			raise
			messages.add_message(request, messages.INFO, 'Record already exists ')
		return redirect('discipline:disciplinecases_home')
	ctx = {}
	ctx['form'] = form
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['span_size'] = 6
	ctx['home_url'] = 'discipline:disciplinecases_home'
	ctx['delete_url'] = 'discipline:disciplinecases_delete'

	return render(request, template_name, ctx)

#update page for disciplinecases
def disciplinecases_update(request , pk, template_name):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('disciplinecases.change_disciplinecases'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	disciplinecases = get_object_or_404(DisciplineCases, pk=pk)
	form = DisciplineCasesForm(request.POST or None, instance=disciplinecases)
	if form.is_valid():
		try:
			studentprofiles = request.POST['studentprofiles']
			blacklist = request.POST['blacklist']
			blacklistdate = request.POST['blacklistdate']
			whitelist = request.POST['whitelist']
			whitelistdate = request.POST['whitelistdate']


			obj = DisciplineCases.objects.get(id=pk)
			obj.studentprofiles_id=studentprofiles
			obj.blacklist=blacklist
			obj.whitelist=whitelist
			obj.whitelistdate=whitelistdate
			obj.save()

		except:
			raise
			messages.add_message(request, messages.INFO, 'Cannot update,record already exists ')

		return redirect('discipline:disciplinecases_home')
	ctx = {}
	ctx['form'] = form
	ctx['disciplinecases'] = disciplinecases
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['pk'] = pk
	ctx['span_size'] = 6
	ctx['home_url'] = 'discipline:disciplinecases_home'
	ctx['delete_url'] = 'discipline:disciplinecases_delete'
	return render(request, template_name, ctx)

#delete page for disciplinecases
def disciplinecases_delete(request, pk, template_name):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('disciplinecases.delete_disciplinecases'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	object_del = get_object_or_404(DisciplineCases, pk=pk)    
	if request.method=='POST':
		try:
			object_del.delete()
		except:
			messages.add_message(request, messages.INFO, 'Cannot delete '+object_del+' this record is linked to other data')

		return redirect('discipline:disciplinecases_home')
	ctx = {}
	ctx['object_del'] = object_del
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['home_url'] = 'discipline:disciplinecases_home'
	ctx['delete_url'] = 'discipline:disciplinecases_delete'
	return render(request, template_name, ctx)
