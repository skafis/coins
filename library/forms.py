from django.forms import ModelForm
import django.forms as forms

from library.models import Books
from school.models import SchoolProfiles

from django.contrib.auth.models import User

#Books
class BooksForm(ModelForm):
	#name = forms.ModelChoiceField(queryset=SchoolProfiles.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	bookname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	author = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	category = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	boughtsponsored = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	amount = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Books

		fields = ['bookname','author','category','boughtsponsored','amount',]


