from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User,Group

from school.models import Classes,Streams,SchoolProfiles
#from system_settings.models import Country


class PhoneBook(models.Model):
	name = models.ForeignKey(SchoolProfiles, verbose_name =  'Name',)
	#country = models.ForeignKey(Country, verbose_name =  'Country',)
	country = models.CharField('country',max_length = 5000,)
	phoneno = models.CharField('Phone-no',max_length = 255,)
	group = models.ForeignKey(Group, verbose_name =  'Group',)
	owner = models.ForeignKey(User,verbose_name = 'Owner',)

	class Meta:
		verbose_name_plural = 'Phone Book'
	def __unicode__(self):
		return unicode('%s' % (self.phoneno))

class Sms(models.Model):
	DELIVERY_STATUS_CHOICES = (
		
		('Sent','Sent'),
		
		('Submitted','Submitted'),
		
		('Buffered','Buffered'),
		
		('Rejected','Rejected'),
		
		('Success','Success'),
		
		('Failed','Failed'),
	)

	reciever = models.ForeignKey(PhoneBook,verbose_name = 'Phone Book',)
	text = models.TextField('Text',)
	deliverystatus = models.CharField('Delivery status',max_length = 255,)
	messageid = models.CharField('Transaction id',max_length = 255,)
	cost = models.CharField('Cost',max_length = 255,)
	sendtime = models.DateTimeField('Send time',)
	deleverytime = models.DateTimeField('Delivery time',max_length = 255,)
	latency = models.IntegerField('Latency in Seconds',default = 0)
	owner = models.ForeignKey(User,verbose_name = 'Owner',)

	class Meta:
		verbose_name_plural = 'Sms'
	def __unicode__(self):
		return unicode('%s' % (self.text,))
