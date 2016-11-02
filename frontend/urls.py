from django.conf.urls import  url

from frontend.classes  import frontend_view

urlpatterns = [
    url(r'^$', frontend_view.IndexView.as_view(), name='index'),
]
