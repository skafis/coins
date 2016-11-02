from django.forms import ModelForm
import django.forms as forms

from school.models import SchoolProfiles

from students.models import StudentProfiles

class SchoolForm(ModelForm):
	merchantschname = forms.ModelChoiceField(queryset=SchoolProfiles.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))

	class Meta:
		model = SchoolProfiles
		fields = ['merchantschname',]


