from django.conf.urls import  url

from login import views

urlpatterns = [

	#LOGIN
  url(r'^login-form$', views.login_form),
  url(r'^$', views.signin, name='signin'),
  url(r'^logout/$', views.logout_view, name='logout'),

	#SIGNUP
  url(r'^register$', views.register, name='register'),

	#url(r'^search-form/$', views.search_form),
  #url(r'^search/$', views.search),

]
