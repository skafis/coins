
from django.forms import ModelForm
import django.forms as forms

from django.contrib.auth.models import User

#USERS

class UsersForm(ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ['username','password',]



