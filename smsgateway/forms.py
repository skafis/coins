from django.forms import ModelForm
import django.forms as forms

from smsgateway.models import PhoneBook,Sms

from django.contrib.auth.models import User,Group

#from system_settings.models import Country

from school.models import SchoolProfiles

#PHONE BOOK
class PhoneBookFilterForm(ModelForm):
	f_country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	#f_country = forms.ModelChoiceField(queryset=Country.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	f_phoneno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	f_group = forms.ModelChoiceField(queryset=Group.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))

	class Meta:
		model = PhoneBook
		fields = ['f_country','f_phoneno','f_group',]


class PhoneBookForm(ModelForm):
	country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	#country = forms.ModelChoiceField(queryset=Country.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	phoneno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	group = forms.ModelChoiceField(queryset=Group.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))

	class Meta:
		model = PhoneBook
		fields = ['country','phoneno','group',]

#SMS
class SmsFilterForm(ModelForm):
	f_reciever = forms.ModelChoiceField(queryset=PhoneBook.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	f_text = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Sms
		fields = ['f_reciever','text',]


class SmsForm(ModelForm):
	reciever = forms.ModelChoiceField(queryset=PhoneBook.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control click2edit wrapper p-md'}))

	class Meta:
		model = Sms
		fields = ['reciever','text',]


