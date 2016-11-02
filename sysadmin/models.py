from __future__ import unicode_literals

from django.db import models

class EntryYear(models.Model):
	entryyear = models.CharField('EntryYear',max_length = 255,)
	currentyear = models.BooleanField('Current Year',)
	class Meta:
		verbose_name_plural = 'Entry Year'

	def __unicode__(self):
		return unicode('%s' % (self.entryyear,))
#ND
class Dormitory(models.Model):
	dormitory = models.CharField('Dormitory',max_length = 255,)
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',)

	def __iter__(self):
		for field_name in self._meta.get_all_field_names():
			value = getattr(self, field_name, None)
			yield (field_name, value)

	class Meta:
		verbose_name_plural = 'Dormitories'

	def __unicode__(self):
		return unicode('%s %s' % (self.dormitory, self.entryyear))

class PaymentMethod(models.Model):
	paymentmethods = models.CharField('Payment Method',max_length = 255,)

	class Meta:
		verbose_name_plural = 'Payment Methods'

	def __unicode__(self):
		return unicode('%s' % (self.paymentmethods))

class Term(models.Model):
	term = models.CharField('Term',max_length = 255,)
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',)
	class Meta:
		verbose_name_plural = 'Term'

	def __unicode__(self):
		return unicode('%s %s' % (self.term, self.entryyear))

class Stream(models.Model):
	stream = models.CharField('Stream',max_length = 255,)
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',)

	class Meta:
		verbose_name_plural = 'stream'

	def __unicode__(self):
		return unicode('%s %s' % (self.stream, self.entryyear))

class Subject(models.Model):
	subject = models.CharField('Subject',max_length = 255,)
	subject_code = models.CharField('Subject Code',max_length = 255,unique=True)
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',)

	class Meta:
		verbose_name_plural = 'Subject'

	def __unicode__(self):
		return unicode('%s  %s' % (self.subject, self.entryyear))

class Paper(models.Model):
	paper = models.CharField('Papers',max_length = 255,)
	paper_code = models.CharField('Paper Code',max_length = 255,unique=True)
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',)

	class Meta:
		verbose_name_plural = 'Papers'

	def __unicode__(self):
		return unicode('%s  %s' % (self.paper, self.entryyear))

class Gender(models.Model):
	gender = models.CharField('Gender',max_length = 255,)
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',)

	class Meta:
		verbose_name_plural = 'Gender'

	def __unicode__(self):
		return unicode('%s %s' % (self.gender, self.entryyear))

class Category(models.Model):
	category = models.CharField('Category',max_length = 255,)
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',)

	class Meta:
		verbose_name_plural = 'Categories'

	def __unicode__(self):
		return unicode('%s %s' % (self.category, self.entryyear))

class Classes(models.Model):
	classes = models.CharField('Classes',max_length = 255,)
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',)

	class Meta:
		verbose_name_plural = 'Classes'

	def __unicode__(self):
		return unicode('%s %s ' % (self.classes, self.entryyear))


class Months(models.Model):
	month = models.CharField('Months',max_length = 255,)
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',)

	class Meta:
		verbose_name_plural = 'Months'

	def __unicode__(self):
		return unicode('%s %s' % (self.month, self.entryyear))


class House(models.Model):
	house = models.CharField('House',max_length = 255,)
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',)

	class Meta:
		verbose_name_plural = 'House'

	def __unicode__(self):
		return unicode('%s %s' % (self.house, self.entryyear))


class SchoolType(models.Model):
	schooltype = models.CharField('School Type',max_length = 255,)

	class Meta:
		verbose_name_plural = 'School Types'

	def __unicode__(self):
		return unicode('%s' % (self.schooltype,))


class CategoryType(models.Model):
	categorytype = models.CharField('Category Type',max_length = 255,)
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',)

	class Meta:
		verbose_name_plural = 'Category Type'

	def __unicode__(self):
		return unicode('%s %s' % (self.categorytype, self.entryyear))

class Country(models.Model):
	country = models.CharField('Country',max_length = 255,)

	class Meta:
		verbose_name_plural = 'Country'

	def __unicode__(self):
		return unicode('%s' % (self.country,))

class SystemConfig(models.Model):
	command_label = models.CharField('Command Label',max_length = 255,unique=True)
	command = models.CharField('command',max_length = 255,)

	class Meta:
		verbose_name_plural = 'System Config'

	def __unicode__(self):
		return unicode('%s %s' % (self.command_label, self.command))

class VoteHeads(models.Model):
	voteheads = models.CharField('Vote heads',max_length = 255,)
	entryyear = models.ForeignKey(EntryYear,verbose_name = 'Entry year',)

	class Meta:
		verbose_name_plural = 'Vote heads'

	def __unicode__(self):
		return unicode('%s %s' % (self.voteheads, self.entryyear))

class Grades(models.Model):
	grades = models.CharField('Grades',max_length = 255,)
	points = models.IntegerField('Points',default=0)

	class Meta:
		verbose_name_plural = 'Grades'

	def __unicode__(self):
		return unicode('%s : %s points' % (self.grades,self.points))

class County(models.Model):
	countyname = models.CharField('County',max_length = 255,)

	class Meta:
		verbose_name_plural = 'County'

	def __unicode__(self):
		return unicode('%s' % (self.countyname))

