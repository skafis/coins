from django.conf.urls import url

from bursar_portal.classes  import view

urlpatterns = [
	#url(r'^schoolregform/$', schools.schoolregform,name='schoolregform'),

	#url(r'^$', schools_view.IndexView.as_view(), name='index'),
	url(r'^$', view.index,name='index'),
	url(r'^check_balance/$', view.check_balance,name='check_balance'),
	url(r'^get_balance/$', view.get_balance,name='get_balance'),
	url(r'^deposit/$', view.deposit,name='deposit'),
	url(r'^do_deposits/$', view.do_deposits,name='do_deposits'),
	url(r'^withdraw/$', view.withdraw,name='withdraw'),
	url(r'^do_withdraw/$', view.do_withdraw,name='do_withdraw'),
	url(r'^activatecard/$', view.activatecard,name='activatecard'),
	url(r'^do_activatecard/$', view.do_activatecard,name='do_activatecard'),

	url(r'^book_create/$', view.book_create,name='book_create'),
]
