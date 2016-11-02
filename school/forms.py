from django.forms import ModelForm
import django.forms as forms

from school.models import SchoolProfiles,SchoolStaff,Classes,Streams,ClassStreams,SchoolType,Gender,PaymentMethods,Dormitory,House, Terms,Months,Subjects,Papers,CategoryType,Category

from sysadmin.models import EntryYear,Dormitory as s_dormitory,PaymentMethod as s_paymentmethod,Term,Stream as s_streams,Gender as s_gender,Category,Classes as s_classes,Months as s_months,House as s_house,SchoolType as s_schooltype,Country,Term as s_terms,Subject as s_subjects,Paper as s_papers,CategoryType as s_categorytype,Category as s_category,County

from django.contrib.auth.models import User


#SCHOOL PROFILES
class SchoolProfilesForm(ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	motto = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	mission = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	vision = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	county = forms.ModelChoiceField(queryset=County.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))

	class Meta:
		model = SchoolProfiles
		fields = ['name','motto','mission','vision','county',]

#SCHOOL STAFF
class SchoolStaffFilterForm(ModelForm):
	f_owner = forms.ModelChoiceField(queryset=User.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))

	class Meta:
		model = SchoolStaff
		fields = ['f_owner',]


class SchoolStaffForm(ModelForm):
	owner = forms.ModelChoiceField(queryset=User.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))

	class Meta:
		model = SchoolStaff
		fields = ['owner',]

#SCHOOL CLASSES
class ClassesForm(ModelForm):
	classes = forms.ModelChoiceField(queryset=s_classes.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#classes = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Classes
		fields = ['classes',]


#SCHOOL STREAMS
class StreamsForm(ModelForm):
	streams = forms.ModelChoiceField(queryset=s_streams.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#streams = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Streams
		fields = ['streams',]


#SCHOOL CLASS STREAMS
class ClassStreamsForm(ModelForm):
	classes = forms.ModelChoiceField(queryset=Classes.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	streams = forms.ModelChoiceField(queryset=Streams.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))

	class Meta:
		model = ClassStreams
		fields = ['classes','streams',]


#SCHOOL TYPE
class SchoolTypeForm(ModelForm):
	schooltype = forms.ModelChoiceField(queryset=s_schooltype.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#schooltype = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = SchoolType
		fields = ['schooltype',]

#GENDER
class GenderForm(ModelForm):
	gender = forms.ModelChoiceField(queryset=s_gender.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#gender = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Gender
		fields = ['gender',]


#PAYMENT METHODS
class PaymentMethodsForm(ModelForm):
	paymentmethods = forms.ModelChoiceField(queryset=s_paymentmethod.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#paymentmethods = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = PaymentMethods
		fields = ['paymentmethods',]

#DORMITORY
class DormitoryForm(ModelForm):
	dormitory = forms.ModelChoiceField(queryset=s_dormitory.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#dormitory = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Dormitory
		fields = ['dormitory',]

#HOUSE
class HouseForm(ModelForm):
	house = forms.ModelChoiceField(queryset=s_house.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#house = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = House
		fields = ['house',]

#TERMS
class TermsForm(ModelForm):
	terms = forms.ModelChoiceField(queryset=s_terms.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#terms = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	startdate = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	enddate = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Terms
		fields = ['terms','startdate','enddate',]

#MONTHS
class MonthsForm(ModelForm):
	month = forms.ModelChoiceField(queryset=s_months.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#month = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Months
		fields = ['month',]


#SUBJECTS
class SubjectsForm(ModelForm):
	subject = forms.ModelChoiceField(queryset=s_subjects.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Subjects
		fields = ['subject',]

#PAPERS
class PapersForm(ModelForm):
	paper = forms.ModelChoiceField(queryset=s_papers.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#paper = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Papers
		fields = ['paper',]

#CATEGORY TYPE
class CategoryTypeForm(ModelForm):
	categorytype = forms.ModelChoiceField(queryset=s_categorytype.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#categorytype = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = CategoryType
		fields = ['categorytype',]

#CATEGORY
class CategoryForm(ModelForm):
	categorytype = forms.ModelChoiceField(queryset=CategoryType.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	category = forms.ModelChoiceField(queryset=s_category.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#category = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Category
		fields = ['categorytype','category',]

