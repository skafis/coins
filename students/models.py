from __future__ import unicode_literals

from __future__ import unicode_literals

#0722383015
from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

from smsgateway.models import PhoneBook
from school.models import Classes,Streams,SchoolProfiles,Category,Gender,Subjects,Dormitory
from sysadmin.models import EntryYear


import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class StudentProfiles(models.Model):
	name = models.ForeignKey(SchoolProfiles, verbose_name =  'Name',default="1")
	admno = models.CharField('ADM No',max_length = 255,primary_key=True)
	username = models.ForeignKey(User,verbose_name = 'Owner',related_name='students_studentprofiles_username')
	firstname = models.CharField('First name',max_length = 255,)
	secondname = models.CharField('Second name',max_length = 255,blank = True)
	lastname = models.CharField('Last name',max_length = 255,)
	schooltransport = models.CharField('School address',max_length = 255)
	#gender = models.CharField(max_length = 255)
	gender = models.ForeignKey(Gender,verbose_name = 'Gender',related_name='students_studentprofiles_gender4')
	specialcases = models.TextField('Special case description',blank = True,)
	#current_classes = models.CharField(max_length = 255)
	current_classes = models.ForeignKey(Classes,verbose_name = 'Current Classes',)
	#current_stream = models.CharField(max_length = 255)
	current_stream = models.ForeignKey(Streams,verbose_name = 'Current Streams',)
	#current_stream = models.CharField(max_length = 255)
	#academic_category = models.CharField(max_length = 255)
	academic_category = models.ForeignKey(Category,verbose_name = 'Academic Category',blank=True,null=True)
	photo = models.ImageField('Photo',upload_to = 'static/media/',blank = True,)
	dateofbirth = models.DateField('Date of birth',blank=True,null=True)
	admissiondate = models.DateField('Admission Date',default=timezone.now)
	residence = models.CharField('Residence/Estate',max_length = 255,)
	lastschoolattended = models.CharField('Last school attended',max_length = 255,default = 'None',)
	lastschooladdress = models.CharField('School address',max_length = 255,default = 'None',)
	schooltransport = models.CharField('School address',max_length = 255,blank=True,null=True)
	schoollunch = models.CharField('School lunch',max_length = 255,blank=True,null=True)
	isactive = models.BooleanField('Active',default = True,)
	accountnumber = models.CharField(max_length = 10000)
	encryped_acc_no = models.CharField(max_length = 10000)
	expirerydate = models.DateField('expirerydate',default="2018-01-01")

	def persons_image(self):
		return '<img src="http://localhost/timaschools/media/%s" height = "50" width = "50" />'% self.photo 
	persons_image.allow_tags = True
	persons_image.short_description = 'Passport'

	def get_admno(self):
		return str('%s' % (self.admno))

	def get_update_admno(self):
		studentprofiles = get_object_or_404(StudentProfiles, pk=pk)
		studentprofiles.delete()
		return unicode('%s' % (d[self.studentprofiles]))


	def persons_names(self):
		return unicode('%s %s %s' % (self.firstname,self.secondname,self.lastname))
	persons_names.allow_tags = True
	persons_names.short_description = 'Names'

	def get_gender(self):
		d=dict(global_vars.GENDER_CHOICES)
		return unicode('%s' % (d[self.gender]))
	get_gender.short_description = 'Gender'
 
	def get_current_classes(self):
		d=dict(global_vars.CLASSES_CHOICES)
		return unicode('%s' % (d[self.current_classes]))
	get_current_classes.short_description = 'current classes'

	def get_current_stream(self):
		d=dict(global_vars.STREAMS_CHOICES)
		return unicode('%s' % (d[self.current_stream]))
	get_current_stream.short_description = 'Streams'

	def get_academic_category(self):
		d=dict(global_vars.ACADEMIC_CATEGORY_CHOICES)
		return unicode('%s' % (d[self.academic_category]))
	get_academic_category.short_description = 'Academic category'

	class Meta:
		verbose_name_plural = 'Student profile'
		ordering=['admno']

	def __unicode__(self):
		#dcc=dict(global_vars.CLASSES_CHOICES)
		#dsc=dict(global_vars.STREAMS_CHOICES)
		return unicode('%s| %s %s %s : %s %s' % (self.admno,self.firstname,self.secondname,self.lastname,self.current_classes, self.current_stream))

class StudentLocation(models.Model):
	studentprofiles = models.ForeignKey(StudentProfiles,verbose_name = 'student Id',)
	county = models.CharField(max_length = 5000,)
	division = models.CharField(max_length = 5000,)
	constituency = models.CharField(max_length = 5000,)
	location = models.CharField(max_length = 5000,)
	sublocation = models.CharField(max_length = 5000,)
	town = models.CharField(max_length = 5000,)

	class Meta:
		verbose_name_plural = 'Student Location'

	def __unicode__(self):
		return unicode('%s' % (self.studentprofiles,))

class StudentDormitory(models.Model):
	studentprofiles = models.ForeignKey(StudentProfiles,verbose_name = 'student Id',)
	dormitory = models.ForeignKey(Dormitory,verbose_name = 'student Id',)
	entrydate = models.DateField('Admission Date',default=timezone.now)

	class Meta:
		verbose_name_plural = 'Student Location'

	def __unicode__(self):
		return unicode('%s' % (self.studentprofiles,))

class StudentClubs(models.Model):
	studentprofiles = models.ForeignKey(StudentProfiles,verbose_name = 'student Id',)
	club = models.CharField(max_length = 5000,)

	class Meta:
		verbose_name_plural = 'Student Location'

	def __unicode__(self):
		return unicode('%s' % (self.studentprofiles,))

class HolidayJobs(models.Model):
	studentprofiles = models.ForeignKey(StudentProfiles,verbose_name = 'student Id',)
	job = models.CharField(max_length = 5000,)

	class Meta:
		verbose_name_plural = 'HolidayJobs'

	def __unicode__(self):
		return unicode('%s' % (self.studentprofiles,))


class StudentSports(models.Model):
	studentprofiles = models.ForeignKey(StudentProfiles,verbose_name = 'student Id',)
	sport = models.CharField(max_length = 5000,)

	class Meta:
		verbose_name_plural = 'Student Location'

	def __unicode__(self):
		return unicode('%s' % (self.studentprofiles,))

class StudentSupplies(models.Model):
	studentprofiles = models.ForeignKey(StudentProfiles,verbose_name = 'Student Profile',)
	category = models.CharField(max_length = 5000,default='')
	supply = models.CharField(max_length = 5000,)

	class Meta:
		verbose_name_plural = 'Student Category'

	def __unicode__(self):
		return unicode('%s' % (self.supply,))

class StudentCategory(models.Model):
	studentprofiles = models.ForeignKey(StudentProfiles,verbose_name = 'Staff Id',)
	category = models.ForeignKey(Category,verbose_name = 'Category',related_name = 'category_category')
	#entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',related_name = 'category_entryyear')
	entryyear = models.CharField('Entry year',max_length = 5000,)

	class Meta:
		verbose_name_plural = 'Student Category'

	def __unicode__(self):
		return unicode('%s' % (self.category))

class StudentParent(models.Model):
	studentprofiles = models.ForeignKey(StudentProfiles,verbose_name = 'Staff Id',)
	user = models.ForeignKey(User,verbose_name = 'Owner',related_name='students_studentparent_username')
	firstname = models.CharField('First name',max_length = 255,)
	secondname = models.CharField('Second name',max_length = 255,blank = True)
	lastname = models.CharField('Last name',max_length = 255,)
	#gender = models.CharField(max_length = 255)
	gender = models.ForeignKey(Gender,verbose_name = 'Gender',related_name='students_studentprofiles_gender3')
	specialcases = models.TextField('Special case description',blank = True,)

	def get_gender(self):
		d=dict(global_vars.GENDER_CHOICES)
		return unicode('%s' % (d[self.gender]))

	class Meta:
		verbose_name_plural = 'Student Parent'

	def __unicode__(self):
		return unicode('names:%s %s %s ,for student: %s' % (self.firstname,self.secondname,self.lastname,self.studentprofiles))

class ParentPhoneNo(models.Model):
	parent = models.ForeignKey(StudentParent,verbose_name = 'Student parent',)
	phoneno = models.ForeignKey(PhoneBook,verbose_name = 'Phone-no',)

	class Meta:
		verbose_name_plural = 'Parent/Guardian Contacts'

	def __unicode__(self):
		return unicode('%s' % (self.phoneno,))

class StudentClassStream(models.Model):
	studentprofiles = models.ForeignKey(StudentProfiles,verbose_name = 'Staff Id',)
	classes = models.ForeignKey(Classes,verbose_name = 'Classes',)
	streams = models.ForeignKey(Streams,verbose_name = 'Streams',)
	#entryyear = models.CharField('Entry year',max_length = 5000,)
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',related_name = 'studentclassstream_entryyear')

	class Meta:
		verbose_name_plural = 'Student Class Stream'

	def __unicode__(self):
		return unicode('%s : %s %s' % (self.studentprofiles,self.classes,self.streams))


class StudentSubject(models.Model):
	name = models.ForeignKey(SchoolProfiles, verbose_name =  'Name',)
	studentprofiles = models.ForeignKey(StudentProfiles,verbose_name = 'Student Profile',)
	subjects = models.ForeignKey(Subjects,verbose_name = 'Subjects',)
	owner = models.ForeignKey(User,verbose_name = 'Owner',)

	class Meta:
		verbose_name_plural = 'Student Subject'

	def __unicode__(self):
		return unicode('%s' % (self.phoneno,))


class YellowForm(models.Model):
	name = models.ForeignKey(SchoolProfiles, verbose_name =  'Name',default="1")
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',related_name = 'studentclassstream_entryyear1')
	indexnumber = models.CharField(max_length = 255)
	firstname = models.CharField(max_length = 255,)
	secondname = models.CharField(max_length = 255,blank = True)
	lastname = models.CharField(max_length = 255,)
	dateofbirth = models.DateField(blank=True,null=True)
	gender = models.ForeignKey(Gender,verbose_name = 'Gender',related_name='students_studentprofiles_gender')
	birthcert = models.CharField(max_length = 255)
	#gender = models.CharField(max_length = 255)
	pupilsinclasseght = models.CharField(max_length = 255)
	lastposition = models.CharField(max_length = 255)
	lastmarks = models.CharField(max_length = 255)
	cocurricularevents = models.TextField()
	headmasterapproval = models.CharField(max_length = 255)
	dateofapproval = models.CharField(max_length = 255)
	headmasterphone = models.CharField(max_length = 255)
	fax = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	parentfullnames = models.CharField(max_length = 255)
	parentgender = models.ForeignKey(Gender,verbose_name = 'Gender',related_name='students_studentprofiles_gender1')
	maritalstatus = models.CharField(max_length = 255)
	parentdead = models.CharField(max_length = 255)
	nationality = models.CharField(max_length = 255)
	nationalid = models.CharField(max_length = 255)
	employment = models.CharField(max_length = 255)
	inbusiness = models.CharField(max_length = 255)
	hasland = models.CharField(max_length = 255)
	otherincomeoptions = models.CharField(max_length = 255)
	physicaladdress = models.CharField(max_length = 255)
	listallsiblings = models.TextField()
	applicationinfo = models.TextField()
	cirtifydate = models.CharField(max_length = 255)
	cirtifysigniture = models.CharField(max_length = 255)
	cirtifyname = models.CharField(max_length = 255)
	cirtifyoccupation = models.CharField(max_length = 255)
	cirtifyaddress = models.CharField(max_length = 255)
	cirtifyfax = models.CharField(max_length = 255)
	cirtifyphone = models.CharField(max_length = 255)
	cirtifyemail = models.CharField(max_length = 255)
	freefullnames = models.CharField(max_length = 255)
	freesignature = models.CharField(max_length = 255)
	freephoneno = models.CharField(max_length = 255)
	recomenderfullnames = models.CharField(max_length = 255)
	recomendersignature = models.CharField(max_length = 255)
	recomenderoffice = models.CharField(max_length = 255)
	recomenderphoneno = models.CharField(max_length = 255)
	kcpemath = models.CharField(max_length = 255,default='')
	kcpeeng = models.CharField(max_length = 255,default='')
	kcpess = models.CharField(max_length = 255,default='')
	kcpekisw = models.CharField(max_length = 255,default='')
	kcpesci = models.CharField(max_length = 255,default='')
	kcpetotal = models.CharField(max_length = 255,default='')

	class Meta:
		verbose_name_plural = 'YellowForm'

	def __unicode__(self):
		return unicode('%s' % (self.indexnumber,))



