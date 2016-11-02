from django.forms import ModelForm
import django.forms as forms

from discipline.models import DisciplineCases

from students.models import StudentProfiles




class DisciplineCasesForm(ModelForm):
	studentprofiles = forms.ModelChoiceField(queryset=StudentProfiles.objects.all().order_by('admno'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	blacklist = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	blacklistdate = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control'}))
	whitelist = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	whitelistdate = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = DisciplineCases
		fields = ['studentprofiles','blacklist','blacklistdate','whitelist','whitelistdate',]

