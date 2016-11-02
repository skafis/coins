from django.conf.urls import patterns, url

from discipline import views

urlpatterns = [

	#DISPLINE
  url(r'^disciplinecases_home$', views.disciplinecases_home, name='disciplinecases_home'),
  url(r'^disciplinecases_single_list/(?P<tid>\d+)$', views.disciplinecases_single_list, name='disciplinecases_single_list'),
  url(r'^new_disciplinecases$', views.disciplinecases_create, name='disciplinecases_new'),
  url(r'^edit_disciplinecases/(?P<pk>\d+)$', views.disciplinecases_update, name='disciplinecases_edit'),
  url(r'^delete_disciplinecases/(?P<pk>\d+)$', views.disciplinecases_delete, name='disciplinecases_delete'),

]
