from django.forms import ModelForm
import django.forms as forms

from sysadmin.models import Classes,EntryYear,County,Stream,Gender,Dormitory
from school.models import SchoolProfiles,Gender as SchGender,Dormitory as SchDormitory

from django.contrib.auth.models import User

#EntryYear
class EntryYearForm(ModelForm):
	entryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	dormitoryentryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	termsentryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	classesentryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	streamentryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	subjectentryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	paperentryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	genderentryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	categoryentryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	monthentryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	houseentryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	categorytypeentryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	voteheadsentryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))

	class Meta:
		model = EntryYear

		fields = ['entryyear',]

#Gender
class GenderDropdownForm(ModelForm):
	gender = forms.ModelChoiceField(queryset=Gender.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	schgender = forms.ModelChoiceField(queryset=SchGender.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	yfgender = forms.ModelChoiceField(queryset=SchGender.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	yfgender2 = forms.ModelChoiceField(queryset=SchGender.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))

	class Meta:
		model = Gender

		fields = ['id',]

#SchoolProfiles
class SchoolDropdownForm(ModelForm):
	schoolprofiles = forms.ModelChoiceField(queryset=SchoolProfiles.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))

	class Meta:
		model = SchoolProfiles

		fields = ['id',]

#Classes
class ClassesDropdownForm(ModelForm):
	formone = forms.ModelChoiceField(queryset=Classes.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	formtwo = forms.ModelChoiceField(queryset=Classes.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	formthree = forms.ModelChoiceField(queryset=Classes.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	formfour = forms.ModelChoiceField(queryset=Classes.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	schformone = forms.ModelChoiceField(queryset=Classes.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))

	class Meta:
		model = Classes

		fields = ['id',]

#Stream
class StreamDropdownForm(ModelForm):
	schoolstream = forms.ModelChoiceField(queryset=Stream.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	secschoolstream = forms.ModelChoiceField(queryset=Stream.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	thirdschoolstream = forms.ModelChoiceField(queryset=Stream.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	fourthschoolstream = forms.ModelChoiceField(queryset=Stream.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	fifthschoolstream = forms.ModelChoiceField(queryset=Stream.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))

	class Meta:
		model = Stream

		fields = ['id',]

#County
class CountyDropdownForm(ModelForm):
	schoolcounty = forms.ModelChoiceField(queryset=County.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	studentcounty = forms.ModelChoiceField(queryset=County.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))

	class Meta:
		model = County

		fields = ['id',]

#User
class UserDropdownForm(ModelForm):
	userdrpdwn = forms.ModelChoiceField(queryset=User.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))

	class Meta:
		model = User

		fields = ['id',]

#Dormitory
class DormitoryForm(ModelForm):
	dormitory = forms.ModelChoiceField(queryset=Dormitory.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	schdormitory = forms.ModelChoiceField(queryset=SchDormitory.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))

	class Meta:
		model = Dormitory

		fields = ['id',]
