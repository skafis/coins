from __future__ import unicode_literals

from django.db import models

from django.db import models

from django.contrib.auth.models import User

from sysadmin.models import Dormitory as SysDormitory,PaymentMethod as SysPaymentMethod,Term as SysTerm,Stream as SysStream,Subject as SysSubject,Paper as SysPaper,Gender as SysGender,Category as SysCategory,Classes as SysClasses,Months as SysMonth,House as SysHouse,SchoolType as SysSchoolType,CategoryType as SysCategoryType,County,EntryYear as SysEntryYear


class SchoolProfiles(models.Model):
	schname = models.CharField(max_length = 255,)
	motto = models.CharField(max_length = 5000,)
	mission = models.CharField(max_length = 5000,)
	vision = models.CharField(max_length = 5000,)
	county = models.ForeignKey(County,default=1)
	accountnumber = models.CharField(max_length = 10000,default='21234567890987')
	encryped_acc_no = models.CharField(max_length = 10000,default='XXXX456789XXXX')
	expirerydate = models.DateField('expirerydate',default="2018-01-01")
	county = models.CharField(max_length = 5000,default='',)
	division = models.CharField(max_length = 5000,default='',)
	constituency = models.CharField(max_length = 5000,default='',)
	location = models.CharField(max_length = 5000,default='',)
	sublocation = models.CharField(max_length = 5000,default='',)
	town = models.CharField(max_length = 5000,default='',)
	phonenumber = models.CharField(max_length = 5000,default='',)
	email = models.CharField(max_length = 5000,default='',)
	noofmerchants = models.CharField(max_length = 5000,default='1',)
	schfeesbalance = models.CharField(max_length = 5000,default='1',)
	pocketmoneybalance = models.CharField(max_length = 5000,default='1',)
	savingsbalance = models.CharField(max_length = 5000,default='1',)
	#owner = models.ForeignKey(User,verbose_name = 'owner')

	class Meta:
		verbose_name_plural = 'School profiles'
		#unique_together = ('name','owner',)
	def __unicode__(self):
		return unicode('%s' % (self.schname,))

class SchoolStaff(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	owner = models.ForeignKey(User,verbose_name = 'Owner',)

	class Meta:
		verbose_name_plural = 'School staff'
	def __unicode__(self):
		return '%s' % (self.owner)

'''class SchoolAccounts(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	#accname = models.CharField(max_length = 255,default="")
	accountnumber = models.CharField(max_length = 5000,)


	class Meta:
		verbose_name_plural = 'School Accounts'
		unique_together = ('name','accountnumber',)

	def __unicode__(self):
		return unicode('%s' % (self.accountnumber,))

class SchoolPhone(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	phonenumber = models.CharField(max_length = 5000,)

	class Meta:
		verbose_name_plural = 'School Phone'
		unique_together = ('name','phonenumber',)

	def __unicode__(self):
		return unicode('%s' % (self.phonenumber,))

class SchoolEmails(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	email = models.CharField(max_length = 5000,)

	class Meta:
		verbose_name_plural = 'School Emails'
		unique_together = ('name','email',)

	def __unicode__(self):
		return unicode('%s' % (self.email,))'''


'''class SchoolLocation(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	county = models.CharField(max_length = 5000,)
	division = models.CharField(max_length = 5000,)
	constituency = models.CharField(max_length = 5000,)
	location = models.CharField(max_length = 5000,)
	sublocation = models.CharField(max_length = 5000,)
	town = models.CharField(max_length = 5000,)

	class Meta:
		verbose_name_plural = 'School Location'

	def __unicode__(self):
		return unicode('%s' % (self.email,))'''

class EntryYear(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	#classes = models.CharField('Classes',max_length = 5000,)
	entryyear = models.ForeignKey(SysEntryYear,verbose_name = 'EntryYear',related_name='entryyear_entryyear')
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'EntryYear'
		unique_together = ('name','entryyear',)

	def __unicode__(self):
		return unicode('%s' % (self.entryyear,))

class Classes(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	#classes = models.CharField('Classes',max_length = 5000,)
	classes = models.ForeignKey(SysClasses,verbose_name = 'Classes',related_name='school_classes')
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'Classes'
		unique_together = ('name','classes',)

	def __unicode__(self):
		return unicode('%s' % (self.classes,))

class Streams(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	#streams = models.CharField('Classes',max_length = 5000,)
	streams = models.ForeignKey(SysStream,verbose_name = 'Stream',related_name='school_streams')
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'Streams'
		#unique_together = ('name','streams',)

	def __unicode__(self):
		return unicode('%s' % (self.streams,))

class ClassStreams(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	classes = models.ForeignKey(Classes,verbose_name = 'Classes',related_name='school_classstreams')
	streams = models.ForeignKey(Streams,verbose_name = 'Streams',)
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'Class streams(Click \'Save & Continue Editing\' first for dropdowns to be populated)'

	def __unicode__(self):
		return unicode('%s' % (self.streams,))

class SchoolType(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	#schooltype = models.CharField('School type',max_length = 5000,)
	schooltype = models.ForeignKey(SysSchoolType,verbose_name = 'School type',related_name='school_schooltype')
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'School Type'
		unique_together = ('name','schooltype',)

	def __unicode__(self):
		return unicode('%s' % (self.schooltype,))

class Gender(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	#gender = models.CharField('Gender',max_length = 5000,)
	gender = models.ForeignKey(SysGender,verbose_name = 'Gender',related_name='school_gender')
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'Gender'
		unique_together = ('name','gender',)

	def __unicode__(self):
		return unicode('%s' % (self.gender,))

class PaymentMethods(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	#paymentmethods = models.CharField('Payment methods',max_length = 5000,)
	paymentmethods = models.ForeignKey(SysPaymentMethod,verbose_name = 'Payment methods',related_name='school_paymentmethod')
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'Payment methods'
		unique_together = ('name','paymentmethods',)

	def __unicode__(self):
		return unicode('%s' % (self.paymentmethods,))

class Dormitory(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	#dormitory = models.CharField('Dormitory',max_length = 5000,)
	dormitory = models.ForeignKey(SysDormitory,verbose_name = 'Dormitory',related_name='school_dormitory')
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'Dormitory'
		unique_together = ('name','dormitory',)

	def __unicode__(self):
		return unicode('%s' % (self.dormitory,))

class House(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	#house = models.CharField('House',max_length = 5000,)
	house = models.ForeignKey(SysHouse,verbose_name = 'House',related_name='school_house')
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'House'
		unique_together = ('name','house',)

	def __unicode__(self):
		return unicode('%s' % (self.house,))

class Terms(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	#terms = models.CharField('Terms',max_length = 5000,)
	terms = models.ForeignKey(SysTerm,verbose_name = 'Terms',related_name='school_terms')
	startdate = models.DateTimeField('Start Date')
	enddate = models.DateTimeField('End Date')
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'Terms'
		unique_together = ('name','terms','startdate','enddate',)

	def __unicode__(self):
		return unicode('%s' % (self.terms,))

class Months(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	#month = models.CharField('Month',max_length = 5000,)
	month = models.ForeignKey(SysMonth,verbose_name = 'Month',related_name='school_month')
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'Months'
		unique_together = ('name','month',)

	def __unicode__(self):
		return unicode('%s' % (self.month,))

class Subjects(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	#subject = models.CharField('Subject',max_length = 5000,)
	subject = models.ForeignKey(SysSubject,verbose_name = 'Subject',related_name='school_subject')
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'Subjects'
		unique_together = ('name','subject',)

	def __unicode__(self):
		return unicode('%s' % (self.subject,))

class Papers(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',related_name='papers_name')
	#papername = models.CharField('Paper name',max_length = 5000,)
	papername = models.ForeignKey(SysPaper,verbose_name = 'Paper',related_name='school_paper')
	#owner = models.ForeignKey(User,verbose_name = 'owner',related_name='papers_owner')

	class Meta:
		verbose_name_plural = 'Papers'
		unique_together = ('name','papername',)

	def __unicode__(self):
		return unicode('%s' % (self.papername,))


class CategoryType(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	#categorytype = models.CharField('Category type',max_length = 5000,)
	categorytype = models.ForeignKey(SysCategoryType,verbose_name = 'Category Type',related_name='school_categorytype')
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'Category type'
		unique_together = ('name','categorytype',)

	def __unicode__(self):
		return unicode('%s' % (self.categorytype,))

class Category(models.Model):
	name = models.ForeignKey(SchoolProfiles,verbose_name = 'Name',)
	categorytype = models.ForeignKey(CategoryType,verbose_name = 'Category Type',related_name='school_category')
	#category = models.CharField('Category',max_length = 5000,)
	category = models.ForeignKey(SysCategory,verbose_name = 'Category',related_name='school_category')
	#owner = models.ForeignKey(User,verbose_name = 'owner',)

	class Meta:
		verbose_name_plural = 'Categories'
		unique_together = ('name','categorytype','category',)

	def __unicode__(self):
		return unicode('%s' % (self.category,))

class SystemConfig(models.Model):
	command_label = models.CharField('Command Label',max_length = 255,unique=True)
	command = models.CharField('command',max_length = 255,)

	class Meta:
		verbose_name_plural = 'System Config'

	def __unicode__(self):
		return unicode('%s %s' % (self.command_label, self.command))

