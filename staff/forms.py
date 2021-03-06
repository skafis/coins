from django.forms import ModelForm
import django.forms as forms

from staff.models import StaffProfiles,StaffPhoneNo

from django.contrib.auth.models import User,Group

from school.models import SchoolProfiles

from smsgateway.models import PhoneBook

from sysadmin.models import Gender

class StaffProfilesForm(ModelForm):
	nationalid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	staff_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	secondname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	gender = forms.ModelChoiceField(queryset=Gender.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),choices=global_vars.GENDER_CHOICES,)
	specialcases = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	group = forms.ModelChoiceField(queryset=Group.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#photo = forms.FileField()

	class Meta:
		model = StaffProfiles
		fields = ['nationalid','firstname','secondname','lastname','gender','specialcases','group']#,'photo',]

class StaffProfilesEditForm(ModelForm):
	nationalid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	staff_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	secondname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	gender = forms.ModelChoiceField(queryset=Gender.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),choices=global_vars.GENDER_CHOICES,)
	specialcases = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	group = forms.ModelChoiceField(queryset=Group.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#photo = forms.FileField()

	class Meta:
		model = StaffProfiles
		fields = ['nationalid','firstname','secondname','lastname','gender','specialcases','group','staff_code']#,'photo',]

class StaffPhoneNoForm(ModelForm):
	staffprofiles = forms.ModelChoiceField(queryset=StaffProfiles.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	phoneno = forms.ModelChoiceField(queryset=PhoneBook.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))

	class Meta:
		model = StaffPhoneNo
		fields = ['staffprofiles','phoneno',]

