from django.shortcuts import render
from pos_portal.models import Transactions,Pos
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from school.models import SchoolProfiles
from .forms import UserForm
from django.contrib import messages

# Create your views here.
@login_required
def user(request):
	if request.method == 'POST':
		form = UserForm(request.POST, instance=request.user)
		if form.is_valid():
				form.save()
            	messages.success(request, _('User was successfully created!'))
            	#return redirect('')

        else:
           	 messages.error(request, _('Please correct the error below.'))
    else:
		form = UserForm(instance=request.user)

    return render(request, 'merchant/create_user.html', {'form':form})


def profile(request,pk):
	school=SchoolProfiles.objects.get(pk=pk)
	return render(request,'school_profile.html',{'school':school})

@login_required
def view_pos(request):
	pos=Pos.objects.all()
	return render(request,'merchant/pos.html',{'pos':pos})

@login_required
def view_transactions(request):
	transactions=Transactions.objects.all()
	return render(request,'merchant/transactions.html',{'transactions':transactions})

