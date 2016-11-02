from django.shortcuts import render, redirect, get_object_or_404

from moe_portal.models import Bursery
from school.models import SchoolProfiles

from students.models import StudentProfiles

from moe_portal.forms import BurseryForm


from django.contrib import messages

from django.contrib.auth.models import User

#bursery_home page for bursery
def bursery_home(request,template_name):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('moe_portal.view_bursery'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	try:
		rows = Bursery.objects.all().distinct('county')
		ctx = {}
		ctx['rows'] = rows
		ctx['modelfields'] = Bursery._meta.get_fields()
		ctx['main_title'] = 'Bursery'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		raise
		rows =  Bursery.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)

#bursery_school_list page for studentfees
def bursery_school_list(request,tid,template_name):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('moe_portal.view_bursery'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	try:
		rows = Bursery.objects.filter(county=tid).distinct('name')
		ctx = {}
		ctx['rows'] = rows
		ctx['tid'] = tid
		ctx['modelfields'] = Bursery._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		raise
		rows =  Bursery.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)


#bursery_school_stud_list page for studentfees
def bursery_school_stud_list(request,tid,template_name):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('moe_portal.view_bursery'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	try:
		rows = Bursery.objects.filter(name_id=tid)
		ctx = {}
		ctx['form'] = form
		ctx['rows'] = rows
		ctx['tid'] = tid
		ctx['modelfields'] = Bursery._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		rows =  Bursery.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)

#create page for bursery
def bursery_create(request, template_name='bursery_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('moe_portal.add_bursery'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	form = BurseryForm(request.POST or None)

	if form.is_valid():
		#name = request.POST['name']
		studentprofiles = request.POST['studentprofiles']
		amount = request.POST['amount']
		#county = request.POST['county']
		sch_bank_acc = request.POST['sch_bank_acc']

		try:
			name = SchoolProfiles.objects.get(owner_id=request.user.id)
			sp = StudentProfiles.objects.get(admno=studentprofiles)
			schp = SchoolProfiles.objects.get(id=sp.name_id)
			obj=Bursery(name_id=sp.name_id,studentprofiles_id=studentprofiles,amount=amount,county=schp.county,sch_bank_acc=sch_bank_acc, owner_id=request.user.id)
			obj.save()
		except:
			raise
			messages.add_message(request, messages.INFO, bursery+'already exists ')
		return redirect('moe_portal:bursery_home')
	ctx = {}
	ctx['form'] = form
	ctx['main_title'] = 'Bursery'
	ctx['breadcrump'] = 'Manage '
	ctx['span_size'] = 6

	return render(request, template_name, ctx)

#update page for bursery
def bursery_update(request , pk, template_name='bursery_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('moe_portal.change_bursery'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	bursery = get_object_or_404(Bursery, pk=pk)
	form = BurseryForm(request.POST or None, instance=bursery)
	if form.is_valid():
		try:
			form.save()
		except:
			messages.add_message(request, messages.INFO, 'Cannot update,record already exists ')

		return redirect('moe_portal:bursery_home')
	ctx = {}
	ctx['form'] = form
	ctx['bursery'] = bursery
	ctx['main_title'] = 'Bursery'
	ctx['breadcrump'] = 'Manage '
	ctx['pk'] = pk
	ctx['span_size'] = 6
	return render(request, template_name, ctx)

#delete page for bursery
def bursery_delete(request, pk, template_name='bursery_confirm_delete.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('moe_portal.delete_bursery'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))

	bursery = get_object_or_404(Bursery, pk=pk)    
	if request.method=='POST':
		try:
			bursery.delete()
		except:
			messages.add_message(request, messages.INFO, 'Cannot delete '+bursery+' this record is linked to other data')

		return redirect('moe_portal:bursery_home')
	ctx = {}
	ctx['bursery'] = bursery
	ctx['main_title'] = 'Bursery'
	ctx['breadcrump'] = 'Manage '
	return render(request, template_name, ctx)

