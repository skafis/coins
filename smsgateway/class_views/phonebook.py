from django.shortcuts import render, redirect, get_object_or_404

from smsgateway.models import PhoneBook
from school.models import SchoolProfiles

from smsgateway.forms import PhoneBookForm

from smsgateway.forms import PhoneBookFilterForm

from django.contrib import messages

from django.contrib.auth.models import User

#phonebook_home page for phonebook
def phonebook_home(request,template_name='phonebook_list.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('smsgateway.view_phonebook'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/', request.path))

	form = PhoneBookFilterForm(request.POST or None)
	try:
		rows = PhoneBook.objects.all()
		ctx = {}
		ctx['form'] = form
		ctx['rows'] = rows
		ctx['modelfields'] = PhoneBook._meta.get_fields()
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'Manage '
		ctx['span_size'] = 10

	except:
		rows =  PhoneBook.objects.all()
		ctx = {}
		ctx['rows'] = rows
	return render(request, template_name, ctx)

#create page for phonebook
def phonebook_create(request, template_name='phonebook_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('smsgateway.add_phonebook'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/', request.path))

	form = PhoneBookForm(request.POST or None)

	if form.is_valid():
		country = request.POST['country']
		phoneno = request.POST['phoneno']
		group = request.POST['group']

		try:
			name = SchoolProfiles.objects.get(owner_id=request.user.id)
			obj=PhoneBook(name_id=name.id,country=country,phoneno=phoneno,group_id=group,owner_id=request.user.id)
			obj.save()
		except:
			raise
			messages.add_message(request, messages.INFO, phonebook+'already exists ')
		return redirect('smsgateway:phonebook_home')
	ctx = {}
	ctx['form'] = form
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['span_size'] = 6

	return render(request, template_name, ctx)

#update page for phonebook
def phonebook_update(request , pk, template_name='phonebook_form.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('smsgateway.change_phonebook'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/', request.path))

	phonebook = get_object_or_404(PhoneBook, pk=pk)
	form = PhoneBookForm(request.POST or None, instance=phonebook)
	if form.is_valid():
		try:
			form.save()
		except:
			messages.add_message(request, messages.INFO, 'Cannot update,record already exists ')

		return redirect('smsgateway:phonebook_home')
	ctx = {}
	ctx['form'] = form
	ctx['phonebook'] = phonebook
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['pk'] = pk
	ctx['span_size'] = 6
	return render(request, template_name, ctx)

#delete page for phonebook
def phonebook_delete(request, pk, template_name='phonebook_confirm_delete.html'):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('smsgateway.delete_phonebook'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/', request.path))

	phonebook = get_object_or_404(PhoneBook, pk=pk)    
	if request.method=='POST':
		try:
			phonebook.delete()
		except:
			messages.add_message(request, messages.INFO, 'Cannot delete '+phonebook+' this record is linked to other data')

		return redirect('smsgateway:phonebook_home')
	ctx = {}
	ctx['phonebook'] = phonebook
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	return render(request, template_name, ctx)

