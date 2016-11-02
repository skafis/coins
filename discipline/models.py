from __future__ import unicode_literals

from django.db import models

from school.models import SchoolProfiles

from students.models import StudentProfiles

from django.contrib.auth.models import User

class DisciplineCases(models.Model):
	studentprofiles = models.ForeignKey(StudentProfiles)
	category = models.CharField(max_length = 10000,default='')
	blacklist = models.CharField(max_length = 10000)
	blacklistdate = models.CharField(max_length = 10000)
	whitelist = models.CharField(max_length = 10000)
	whitelistdate = models.CharField(max_length = 10000)

	class Meta:
		verbose_name_plural = 'Discipline Case'

	def __unicode__(self):
		return unicode('%s' % (self.studentprofiles,))
