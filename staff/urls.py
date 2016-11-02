from django.conf.urls import  url

from staff import views

urlpatterns = [

	#STAFF PROFILES
  url(r'^staffprofiles_home$', views.staffprofiles_home, name='staffprofiles_home'),
  url(r'^new_staffprofiles$', views.staffprofiles_create, name='staffprofiles_new'),
  url(r'^edit_staffprofiles/(?P<pk>\d+)$', views.staffprofiles_update, name='staffprofiles_edit'),
  url(r'^delete_staffprofiles/(?P<pk>\d+)$', views.staffprofiles_delete, name='staffprofiles_delete'),

	#STAFF PHONE
  url(r'^staffphoneno_home$', views.staffphoneno_home, name='staffphoneno_home'),
  url(r'^new_staffphoneno$', views.staffphoneno_create, name='staffphoneno_new'),
  url(r'^edit_staffphoneno/(?P<pk>\d+)$', views.staffphoneno_update, name='staffphoneno_edit'),
  url(r'^delete_staffphoneno/(?P<pk>\d+)$', views.staffphoneno_delete, name='staffphoneno_delete'),

]
