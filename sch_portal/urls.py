from django.conf.urls import url

from sch_portal.classes  import view

urlpatterns = [
	#url(r'^schoolregform/$', schools.schoolregform,name='schoolregform'),

	#url(r'^$', schools_view.IndexView.as_view(), name='index'),
	url(r'^$', view.index,name='index'),
	url(r'^register/$', view.register,name='register'),
	url(r'^student_create/$', view.student_create,name='student_create'),
	url(r'^syssettings/$', view.syssettings,name='syssettings'),
	url(r'^discipline/$', view.discipline,name='discipline'),
	url(r'^studentsports/$', view.studentsports,name='studentsports'),
	url(r'^studentclubs/$', view.studentclubs,name='studentclubs'),
	url(r'^holidayjobs/$', view.holidayjobs,name='holidayjobs'),
	url(r'^studentsupplies/$', view.studentsupplies,name='studentsupplies'),
	url(r'^certsofachievment/$', view.certsofachievment,name='certsofachievment'),
	url(r'^academics/$', view.academics,name='academics'),
	url(r'^library/$', view.library,name='library'),
	url(r'^books/$', view.books,name='books'),

	url(r'^gender_create/$', view.gender_create,name='gender_create'),
	url(r'^entryyear_create/$', view.entryyear_create,name='entryyear_create'),
	url(r'^classes_create/$', view.classes_create,name='classes_create'),
	url(r'^stream_create/$', view.stream_create,name='stream_create'),
	url(r'^yellowform_create/$', view.yellowform_create,name='yellowform_create'),
	url(r'^dormitory_create/$', view.dormitory_create,name='dormitory_create'),
	url(r'^studentsports_create/$', view.studentsports_create,name='studentsports_create'),
	url(r'^studentclubs_create/$', view.studentclubs_create,name='studentclubs_create'),
	url(r'^holidayjobs_create/$', view.holidayjobs_create,name='holidayjobs_create'),
	url(r'^disciplinecases_create/$', view.disciplinecases_create,name='disciplinecases_create'),
	url(r'^studentsupplies_create/$', view.studentsupplies_create,name='studentsupplies_create'),
	url(r'^book_create/$', view.book_create,name='book_create'),
]
