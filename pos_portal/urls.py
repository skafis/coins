from django.conf.urls import url

from pos_portal.classes  import view
app_name='pos_portal'

urlpatterns = [
	url(r'^$', view.index,name='index'),
	url(r'^pos/$', view.pos,name='pos'),
	url(r'^student/$', view.student,name='student'),
	url(r'^pos_by_schools/$', view.pos_by_schools,name='pos_by_schools'),
	url(r'^pos_by_posname/(?P<pk>\d+)/$', view.pos_by_posname,name='pos_by_posname'),
	url(r'^pos_create/$', view.pos_create,name='pos_create'),
	url(r'^merchant_create/$', view.merchant_create,name='merchant_create'),
	url(r'^pos_transactions/(?P<pk>\d+)/$', view.pos_transactions,name='pos_transactions'),
	url(r'^merchant/$', view.merchant,name='merchant'),

	url(r'^transactions/$', view.transactions,name='transactions'),
	url(r'^pos_transactions/$', view.pos_transactions,name='pos_transactions')
]
