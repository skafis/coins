from django.conf.urls import patterns, url

from students import views

urlpatterns = [

	#STUDENT PROFILES
  url(r'^studentprofiles_home$', views.studentprofiles_home, name='studentprofiles_home'),
  url(r'^new_studentprofiles$', views.studentprofiles_create, name='studentprofiles_new'),
  url(r'^edit_studentprofiles/(?P<pk>\w+)$', views.studentprofiles_update, name='studentprofiles_edit'),
  url(r'^delete_studentprofiles/(?P<pk>\w+)$', views.studentprofiles_delete, name='studentprofiles_delete'),

	#STUDENT PROFILES
  url(r'^studentcategory_home$', views.studentcategory_home, name='studentcategory_home'),
  url(r'^new_studentcategory$', views.studentcategory_create, name='studentcategory_new'),
  url(r'^edit_studentcategory/(?P<pk>\d+)$', views.studentcategory_update, name='studentcategory_edit'),
  url(r'^delete_studentcategory/(?P<pk>\d+)$', views.studentcategory_delete, name='studentcategory_delete'),

	#STUDENT PARENT
  url(r'^studentparent_home$', views.studentparent_home, name='studentparent_home'),
  url(r'^new_studentparent$', views.studentparent_create, name='studentparent_new'),
  url(r'^edit_studentparent/(?P<pk>\d+)$', views.studentparent_update, name='studentparent_edit'),
  url(r'^delete_studentparent/(?P<pk>\d+)$', views.studentparent_delete, name='studentparent_delete'),

	#STUDENT PARENT
  url(r'^parentphoneno_home$', views.parentphoneno_home, name='parentphoneno_home'),
  url(r'^new_parentphoneno$', views.parentphoneno_create, name='parentphoneno_new'),
  url(r'^edit_parentphoneno/(?P<pk>\d+)$', views.parentphoneno_update, name='parentphoneno_edit'),
  url(r'^delete_parentphoneno/(?P<pk>\d+)$', views.parentphoneno_delete, name='parentphoneno_delete'),

	#STUDENT CLASS STREAM
  url(r'^studentclassstream_home$', views.studentclassstream_home, name='studentclassstream_home'),
  url(r'^new_studentclassstream$', views.studentclassstream_create, name='studentclassstream_new'),
  url(r'^edit_studentclassstream/(?P<pk>\d+)$', views.studentclassstream_update, name='studentclassstream_edit'),
  url(r'^delete_studentclassstream/(?P<pk>\d+)$', views.studentclassstream_delete, name='studentclassstream_delete'),

	#STUDENT SUBJECT
  url(r'^studentsubject_home$', views.studentsubject_home, name='studentsubject_home'),
  url(r'^new_studentsubject$', views.studentsubject_create, name='studentsubject_new'),
  url(r'^edit_studentsubject/(?P<pk>\d+)$', views.studentsubject_update, name='studentsubject_edit'),
  url(r'^delete_studentsubject/(?P<pk>\d+)$', views.studentsubject_delete, name='studentsubject_delete'),

	#yellowform
  url(r'^yellowform_home$', views.yellowform_home, name='yellowform_home'),
  url(r'^new_yellowform$', views.yellowform_create, name='yellowform_new'),
  url(r'^edit_yellowform/(?P<pk>\d+)$', views.yellowform_update, name='yellowform_edit'),
  url(r'^delete_yellowform/(?P<pk>\d+)$', views.yellowform_delete, name='yellowform_delete'),

]
