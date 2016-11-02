from django.forms import ModelForm
import django.forms as forms

from students.models import StudentProfiles,StudentCategory,StudentParent,ParentPhoneNo,StudentClassStream,StudentSubject

from school.models import Classes,Streams,Category,Gender,Subjects

from sysadmin.models import EntryYear

from smsgateway.models import PhoneBook

from django.contrib.auth.models import User

#from global_config import global_vars

#STUDENT PROFILES
class StudentProfilesForm(ModelForm):
	admno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	secondname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	gender = forms.ModelChoiceField(queryset=Gender.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),initial='2')
	#gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),choices=GENDER_CHOICES,)
	specialcases = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
	#current_classes = forms.ChoiceField(widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),choices=CLASSES_CHOICES,)
	current_classes = forms.ModelChoiceField(queryset=Classes.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),initial='6')
	current_stream = forms.ModelChoiceField(queryset=Streams.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),initial='1')
	#current_stream = forms.ChoiceField(widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),choices=STREAMS_CHOICES,)
	academic_category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),initial='2')
	#academic_category = forms.ChoiceField(widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),choices=ACADEMIC_CATEGORY_CHOICES,)
	#photo = forms.FileField()
	dateofbirth = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),initial='2000-01-01')
	#admissiondate = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	#residence = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	#lastschoolattended = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	#lastschooladdress = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	#schooltransport = forms.ChoiceField(widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),choices=TRANSPORT_CHOICES,)
	#schoollunch = forms.ChoiceField(widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),choices=LUNCH_CHOICES,)

	class Meta:
		model = StudentProfiles
		fields = ['admno','firstname','secondname','lastname','gender','specialcases','current_classes','current_stream', 'academic_category','dateofbirth',]#'residence','lastschoolattended','lastschooladdress', 'schooltransport','schoollunch',]


#STUDENT CATEGORY
class StudentCategoryForm(ModelForm):
	studentprofiles = forms.ModelChoiceField(queryset=StudentProfiles.objects.all().order_by('admno'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	entryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#entryyear = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = StudentCategory
		fields = ['studentprofiles','category','entryyear']

#STUDENT PARENT
class StudentParentForm(ModelForm):
	studentprofiles = forms.ModelChoiceField(queryset=StudentProfiles.objects.all().order_by('admno'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	username = forms.ModelChoiceField(queryset=User.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	secondname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	gender = forms.ModelChoiceField(queryset=Gender.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),choices=global_vars.GENDER_CHOICES,)
	specialcases  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = StudentParent
		fields = ['studentprofiles','username','firstname','secondname','lastname','gender','specialcases']

#PARENT PHONENO
class ParentPhoneNoForm(ModelForm):
	parent = forms.ModelChoiceField(queryset=StudentParent.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	phoneno = forms.ModelChoiceField(queryset=PhoneBook.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))

	class Meta:
		model = StudentParent
		fields = ['parent','phoneno',]

#STUDENT CLASS STREAM
class StudentClassStreamForm(ModelForm):
	studentprofiles = forms.ModelChoiceField(queryset=StudentProfiles.objects.all().order_by('admno'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	classes = forms.ModelChoiceField(queryset=Classes.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	streams = forms.ModelChoiceField(queryset=Streams.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	entryyear = forms.ModelChoiceField(queryset=EntryYear.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	#entryyear = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = StudentParent
		fields = ['studentprofiles','classes','streams','entryyear',]

#STUDENT SUBJECT
class StudentSubjectForm(ModelForm):
	studentprofiles = forms.ModelChoiceField(queryset=StudentProfiles.objects.all().order_by('admno'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))
	subjects = forms.ModelChoiceField(queryset=Subjects.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}))

	class Meta:
		model = StudentSubject
		fields = ['studentprofiles','subjects',]

#STUDENT PROFILES
class YellowFormForm(ModelForm):
	entryyear = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	indexnumber = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	secondname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	dateofbirth =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	gender = forms.ModelChoiceField(queryset=Gender.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),initial='2')
	birthcert = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	pupilsinclasseght = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	lastposition = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	lastmarks = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	cocurricularevents = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	headmasterapproval = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	dateofapproval = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	headmasterphone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	fax = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	parentfullnames = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	parentgender = forms.ModelChoiceField(queryset=Gender.objects.all().order_by('id'),widget=forms.Select(attrs={'class':'select2_demo_1 form-control'}),initial='2')
	maritalstatus = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	parentdead = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	nationality = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	nationalid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	employment = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	inbusiness = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	hasland = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	otherincomeoptions = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	physicaladdress = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	listallsiblings = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	applicationinfo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	cirtifydate = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	cirtifysigniture = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	cirtifyname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	cirtifyoccupation = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	cirtifyaddress = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	cirtifyfax = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	cirtifyphone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	cirtifyemail = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	freefullnames = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	freesignature = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	freephoneno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	recomenderfullnames = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	recomendersignature = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	recomenderoffice = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	recomenderphoneno = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = StudentProfiles
		fields = ['entryyear','indexnumber','firstname','secondname','lastname','dateofbirth','gender','birthcert','pupilsinclasseght','lastposition', 'lastmarks','cocurricularevents','headmasterapproval'
,'dateofapproval','headmasterphone','fax','email','parentfullnames','parentgender','maritalstatus','parentdead','nationality','nationalid','employment','inbusiness','hasland','otherincomeoptions', 'physicaladdress','listallsiblings','applicationinfo','cirtifydate','cirtifysigniture','cirtifyname','cirtifyoccupation','cirtifyaddress','cirtifyfax','cirtifyphone','cirtifyemail','freefullnames', 'freesignature','freephoneno','recomenderfullnames','recomendersignature','recomenderoffice','recomenderphoneno',]

#StudentProfiles
class StudentDropDownForm(ModelForm):
	studentprofiles = forms.ModelChoiceField(queryset=StudentProfiles.objects.all().order_by('admno'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	studentprofiles2 = forms.ModelChoiceField(queryset=StudentProfiles.objects.all().order_by('admno'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))
	class Meta:
		model = StudentProfiles

		fields = ['admno',]
