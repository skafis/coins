from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from school.models import SchoolProfiles

from django.db import models

from school.models import SchoolProfiles

from students.models import StudentProfiles

from django.contrib.auth.models import User

from django.utils import timezone

from django.core.cache import cache
from django.db.models import Max

import uuid

class Merchants(models.Model):
	name = models.ForeignKey(SchoolProfiles, verbose_name =  'Name',default="1")
	firstname = models.CharField(max_length = 5000,)
	secondname = models.CharField(max_length = 5000,)
	lastname = models.CharField(max_length = 5000,)
	phonenumber = models.CharField(max_length = 5000,)
	email = models.CharField(max_length = 5000,)
	balance = models.CharField(max_length = 5000,default=10300)
	username = models.ForeignKey(User,verbose_name = 'owner')



	class Meta:
		verbose_name_plural = 'Merchants'
	def __unicode__(self):
		return unicode('%s' % (self.username,))

class Pos(models.Model):
	merchant = models.ForeignKey(Merchants,default=1)
	posnumber = models.CharField(max_length = 5000,)
	accountnumber = models.CharField(max_length = 5000,)
	serialnum = models.CharField(max_length = 5000,)


	class Meta:
		verbose_name_plural = 'Pos'
	def __unicode__(self):
		return unicode('%s' % (self.posnumber,))

'''class StudentAccounts(models.Model):
	studentprofiles = models.ForeignKey(StudentProfiles)
	accountnumber = models.CharField(max_length = 10000,default="")
	encryped_acc_no = models.CharField(max_length = 10000)
	expirerydate = models.DateField('expirerydate',)

	class Meta:
		verbose_name_plural = 'StudentAccounts'

	def __unicode__(self):
		return unicode('%s' % (self.accountnumber,))'''

class StudentAccountsWallets(models.Model):
	studentprofiles = models.ForeignKey(StudentProfiles,verbose_name = 'Bank Acc',)
	walletname_name = models.CharField(max_length = 255,)
	max_amount = models.IntegerField('Max amount',)
	opendate = models.DateField('Admission Date',)
	is_locked = models.BooleanField(max_length = 255,default = False)

	class Meta:
		verbose_name_plural = 'Student Bank Acc'

	def __unicode__(self):
		return unicode('%s' % (self.walletname_name,))

class Transactions(models.Model):
	#studentaccounts  = models.ForeignKey(StudentAccounts)
	wallet  = models.ForeignKey(StudentAccountsWallets,)
	transaction_type = models.CharField(max_length = 10000)
	amount = models.CharField(max_length = 10000)
	transaction_date = models.DateField(default=timezone.now)
	trace_no = models.CharField(max_length = 10000)
	ref_no = models.CharField(max_length = 10000)
	#trace_no = models.UUIDField(default=uuid.uuid4, editable=False)
	#ref_no = models.UUIDField(default=uuid.uuid4, editable=False)
	currency = models.CharField(max_length = 10000)
	location = models.ForeignKey(SchoolProfiles, verbose_name =  'Name',default="1")
	terminal = models.ForeignKey(Pos,default=1)
	balance = models.CharField(max_length = 5000,default=100)
	reverse = models.CharField(max_length = 5000,default=100)

	def as_json(self):
		return dict(
            wallet=self.wallet, transaction_type=self.transaction_type,amount=self.amount,transaction_date=self.transaction_date.isoformat(),trace_no=self.trace_no,ref_no=self.ref_no,currency=self.currency,location=self.location,terminal=self.terminal,balance=self.balance,reverse=self.reverse,)

	def get_bal(self):
		return 'my bal'

	class Meta:
		verbose_name_plural = 'Transactions'

	def __unicode__(self):
		return unicode('%s' % (self.studentaccounts,))
