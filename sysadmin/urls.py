from django.conf.urls import url

from sysadmin.classes  import view

urlpatterns = [

	url(r'^entryyear_create/$', view.entryyear_create,name='entryyear_create'),
	url(r'^classes_create/$', view.classes_create,name='classes_create'),
	url(r'^dormitory_create/$', view.dormitory_create,name='dormitory_create'),
	url(r'^paymentmethods_create/$', view.paymentmethods_create,name='paymentmethods_create'),
	url(r'^terms_create/$', view.terms_create,name='terms_create'),
	url(r'^stream_create/$', view.stream_create,name='stream_create'),
	url(r'^subject_create/$', view.subject_create,name='subject_create'),
	url(r'^paper_create/$', view.paper_create,name='paper_create'),
	url(r'^gender_create/$', view.gender_create,name='gender_create'),
	url(r'^category_create/$', view.category_create,name='category_create'),
	url(r'^month_create/$', view.month_create,name='month_create'),
	url(r'^house_create/$', view.house_create,name='house_create'),
	url(r'^schooltype_create/$', view.schooltype_create,name='schooltype_create'),
	url(r'^categorytype_create/$', view.categorytype_create,name='categorytype_create'),
	url(r'^country_create/$', view.country_create,name='country_create'),
	url(r'^county_create/$', view.county_create,name='county_create'),
	url(r'^voteheads_create/$', view.voteheads_create,name='voteheads_create'),
	url(r'^grades_create/$', view.grades_create,name='grades_create'),
	url(r'^schstaff_create/$', view.schstaff_create,name='schstaff_create'),

	url(r'^$', view.index,name='index'),
	url(r'^syssettings/$', view.syssettings,name='syssettings'),
	url(r'^school/$', view.school,name='school'),
	url(r'^school_create/$', view.school_create,name='school_create'),
	url(r'^student/$', view.student,name='student'),
	url(r'^view_schools/(?P<pk>\d+)/$', view.view_schools,name='view_schools'),
	url(r'^view_schools_details$', view.view_schools_details,name='view_schools_details'),

]
