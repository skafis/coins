from django.conf.urls import patterns, url

from moe_portal import views
from moe_portal.classes import view

urlpatterns = [

	url(r'^$', view.index,name='index'),
	url(r'^moe/$', view.moe,name='moe'),

	#BURSERY
  url(r'^bursery_home$', views.bursery_home, name='bursery_home'),
  url(r'^bursery_school_list/(?P<tid>\d+)$', views.bursery_school_list, name='bursery_school_list'),
  url(r'^bursery_school_stud_list/(?P<tid>\d+)$', views.bursery_school_stud_list, name='bursery_school_stud_list'),
  url(r'^new_bursery$', views.bursery_create, name='bursery_new'),
  url(r'^edit_bursery/(?P<pk>\d+)$', views.bursery_update, name='bursery_edit'),
  url(r'^delete_bursery/(?P<pk>\d+)$', views.bursery_delete, name='bursery_delete'),

	#TUTION FUNDS
  url(r'^tutionfunds_home$', views.tutionfunds_home, name='tutionfunds_home'),
  url(r'^tutionfunds_school_list/(?P<tid>\d+)$', views.tutionfunds_school_list, name='tutionfunds_school_list'),
  url(r'^new_tutionfunds$', views.tutionfunds_create, name='tutionfunds_new'),
  url(r'^edit_tutionfunds/(?P<pk>\d+)$', views.tutionfunds_update, name='tutionfunds_edit'),
  url(r'^delete_tutionfunds/(?P<pk>\d+)$', views.tutionfunds_delete, name='tutionfunds_delete'),

]
