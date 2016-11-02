from django.conf.urls import  url

from smsgateway import views

urlpatterns = [

	#PHONE BOOK
  url(r'^phonebook_home$', views.phonebook_home, name='phonebook_home'),
  url(r'^new_phonebook$', views.phonebook_create, name='phonebook_new'),
  url(r'^edit_phonebook/(?P<pk>\d+)$', views.phonebook_update, name='phonebook_edit'),
  url(r'^delete_phonebook/(?P<pk>\d+)$', views.phonebook_delete, name='phonebook_delete'),

	#SCHOOL STAFF
  url(r'^sms_home$', views.sms_home, name='sms_home'),
  url(r'^new_sms$', views.sms_create, name='sms_new'),
  url(r'^edit_sms/(?P<pk>\d+)$', views.sms_update, name='sms_edit'),
  url(r'^delete_sms/(?P<pk>\d+)$', views.sms_delete, name='sms_delete'),

]
