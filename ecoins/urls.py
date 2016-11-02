"""ecoins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from django.http import HttpResponseRedirect
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#import system_settings.urls
import frontend.urls
import login.urls
import staff.urls
import smsgateway.urls
import pos_portal.urls
import students.urls
import sysadmin.urls
import moe_portal.urls
import sch_portal.urls
import ecoins_portal.urls
import discipline.urls
import fileuploader.urls
import bursar_portal.urls
import merchant_portal.urls

urlpatterns = [
    #url(r'^system_settings/', include(system_settings.urls, namespace='system_settings')),
    #url(r'^', include(frontend.urls, namespace='frontend')),
    url(r'^', include(login.urls, namespace='login')),
    url(r'^staff/', include(staff.urls, namespace='staff')),
    url(r'^smsgateway/', include(smsgateway.urls, namespace='smsgateway')),
    url(r'^pos_portal/', include(pos_portal.urls, namespace='pos_portal')),
    url(r'^students/', include(students.urls, namespace='students')),
    url(r'^sysadmin/', include(sysadmin.urls, namespace='sysadmin')),
    url(r'^moe_portal/', include(moe_portal.urls, namespace='moe_portal')),
    url(r'^sch_portal/', include(sch_portal.urls, namespace='sch_portal')),
    url(r'^ecoins_portal/', include(ecoins_portal.urls, namespace='ecoins_portal')),
    url(r'^discipline/', include(discipline.urls, namespace='discipline')),
    url(r'^fileuploader/', include(fileuploader.urls, namespace='fileuploader')),
    url(r'^bursar_portal/', include(bursar_portal.urls, namespace='bursar_portal')),
    #url(r'^merchant_portal/', include(merchant_portal.urls, namespace='merchant_portal')),

    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
