from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from school.models import Classes,Streams,SchoolProfiles,Subjects

from students.models import StudentProfiles

class Books(models.Model):
	name = models.ForeignKey(SchoolProfiles, verbose_name =  'Name',default="1")
	bookname = models.CharField(max_length = 255,)
	author = models.CharField(max_length = 255,blank = True)
	category = models.CharField(max_length = 255,)
	boughtsponsored = models.CharField(max_length = 255,)
	amount = models.IntegerField()
	entrydate = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = 'Books'

	def __unicode__(self):
		return unicode(self.bookname)

class StudentBook(models.Model):
	studentprofiles = models.ForeignKey(StudentProfiles)
	bookname = models.ForeignKey(Books)
	lenddate = models.DateField(default=timezone.now)
	returndate = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = 'Student Books'

	def __unicode__(self):
		return unicode(self.studentprofiles)


#user = models.ForeignKey(User,verbose_name = 'Owner',related_name='students_studentparent_username')
