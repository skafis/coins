from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User

from login.forms import UsersForm
from django.contrib.auth import authenticate

from django.contrib import messages

from django.contrib.auth import logout,authenticate, login

from staff.forms import StaffProfilesForm
from staff.models import StaffProfiles

def login_form(request):
    return render(request, 'login/login_form.html')

#login
def signin(request,template_name='login/login_form.html'):
	if 'username' in request.POST and 'password' in request.POST:
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		ctx = {}
		if user is not None:
			# the password verified for the user
			if user.is_active:
				login(request, user)
				#messages.add_message(request, messages.INFO, 'User is valid, active and authenticated')
				#print("User is valid, active and authenticated")
				try:
						cs=StaffProfiles.objects.get(username_id=request.user.id)
						if cs.staff_code==1 or cs.staff_code==2:
								return redirect('/pos_portal/')
						else:
							if request.POST['next_url']:
								return redirect(request.POST['next_url'])#get the next page so that when a user is logged out by system it can log them back in in the same order
							else:
								return redirect('user_accounts:users_home')
				except:
					if user.is_superuser:
						return redirect('/pos_portal/')
					else:				
						messages.add_message(request, messages.INFO, 'Sorry you are not linked to any account,Kindly Contact Admin')
						return redirect('login:signin')
			else:	
				messages.add_message(request, messages.INFO, 'The credentials are valid, but the account has been disabled,Kindly contact admin for reactivation')		      
				return render(request, template_name,ctx)
		else:
			# the authentication system was unable to verify the username and password
			messages.add_message(request, messages.INFO, 'The username and password were incorrect.')		      
			print("The username and password were incorrect.")
			return render(request, template_name,ctx)
	else:
		ctx = {}
		if 'next' in request.GET:#check if url has 'next',store 'next' context so that it will be used to redirect the user later when they log back
			ctx['next_url'] = request.GET['next']
		#messages.add_message(request, messages.INFO, 'Please fill in all fields.....')		      
		return render(request, template_name,ctx)

def logout_view(request,template_name='login/login_form.html'):
	try:
		cs=StaffProfiles.objects.get(username_id=request.user.id)
		cs.status=0
		cs.save()
	except:
			pass

	logout(request)
	return render(request, template_name)


#create page for customerprofile
def register(request):
	form = StaffProfilesForm(request.POST or None,request.FILES)
	ctx = {}
	ctx['form'] = form

	if request.method == 'POST':
			if form.is_valid():
				try:
					user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],password= request.POST['username'])
					user.save()
					user.is_superuser=True
					user.save()

					#obj=StaffProfiles(username_id=user.id,firstname=request.POST['firstname'],lastname=request.POST['lastname'],gender=request.POST['gender'],email=request.POST['email'],group_id='1',photo=request.POST['photo'],regdate=datetime.date.today)
					#obj.save()
					form.save()
			
					cp=StaffProfiles.objects.get(email=request.POST['email'])
					cp.username_id=user.id
					cp.group_id=1
					cp.save()

				except:
					raise
					messages.add_message(request, messages.INFO, 'Record already exists ')
				return redirect('customers:customerprofile_home')
			ctx = {}
			ctx['form'] = form
			ctx['main_title'] = 'StaffProfiles'
			ctx['breadcrump'] = 'Manage StaffProfiles'
			ctx['span_size'] = 6

			return render(request, 'login/register.html', ctx)
	else:
		return render(request, 'login/register.html',ctx)

