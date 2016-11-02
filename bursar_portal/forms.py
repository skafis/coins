from django.forms import ModelForm
import django.forms as forms

from students.models import StudentProfiles,StudentCategory,StudentParent,ParentPhoneNo,StudentClassStream,StudentSubject

from school.models import Classes,Streams,Category,Gender,Subjects

from sysadmin.models import EntryYear

from smsgateway.models import PhoneBook

from django.contrib.auth.models import User

#from global_config import global_vars



class StudentBalanceForm(ModelForm):
	WALLETNAME_CHOICES= (
		('School Fees','School Fees'),
		('Pocket Money','Pocket Money'),
		('Savings','Savings'),
	)
	walletname_name = forms.ChoiceField(widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),choices=WALLETNAME_CHOICES,)
	studentprofiles = forms.ModelChoiceField(queryset=StudentProfiles.objects.all().order_by('admno'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))

	class Meta:
		model = StudentCategory
		fields = ['id']

#Deposit
class DepositForm(ModelForm):
	WALLETNAME_CHOICES= (
		('1','School Fees'),
		('2','Pocket Money'),
		('3','Savings'),
	)
	walletname_name = forms.ChoiceField(widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),choices=WALLETNAME_CHOICES,)
	studentprofiles = forms.ModelChoiceField(queryset=StudentProfiles.objects.all().order_by('admno'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	amount = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = StudentCategory
		fields = ['id']

#Deposit
class WithdrawForm(ModelForm):
	#walletname_name = forms.ChoiceField(widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),choices=WALLETNAME_CHOICES,)
	studentprofiles = forms.ModelChoiceField(queryset=StudentProfiles.objects.all().order_by('admno'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	amount = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = StudentCategory
		fields = ['id']


class ActivateCardForm(ModelForm):
	WALLETNAME_CHOICES= (
		('School Fees','School Fees'),
		('Pocket Money','Pocket Money'),
		('Savings','Savings'),
	)
	walletname_name = forms.ChoiceField(widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),choices=WALLETNAME_CHOICES,)
	studentprofiles = forms.ModelChoiceField(queryset=StudentProfiles.objects.all().order_by('admno'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	is_locked = forms.BooleanField()
	
	class Meta:
		model = StudentCategory
		fields = ['id']