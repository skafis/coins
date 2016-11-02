from django.shortcuts import render

import moe_portal.class_views.bursery as bursery
import moe_portal.class_views.tutionfunds as tutionfunds

#BURSERY
def bursery_home(request,template_name='moe_portal/bursery_county_list.html'):
 return bursery.bursery_home(request,template_name=template_name)

def bursery_school_list(request,tid, template_name='moe_portal/bursery_schools_list.html'):
	return bursery.bursery_school_list(request,tid, template_name=template_name)

def bursery_school_stud_list(request,tid, template_name='moe_portal/bursery_list.html'):
	return bursery.bursery_school_stud_list(request,tid, template_name=template_name)

def bursery_create(request, template_name='moe_portal/bursery_form.html'):
	return bursery.bursery_create(request, template_name=template_name)

def bursery_update(request , pk, template_name='moe_portal/bursery_form.html'):
	return bursery.bursery_update(request , pk, template_name=template_name)

def bursery_delete(request, pk, template_name='moe_portal/bursery_confirm_delete.html'):
	return bursery.bursery_delete(request, pk, template_name=template_name)


#TUTION FUNDS
def tutionfunds_home(request,template_name='moe_portal/tutionfunds_county_list.html'):
 return tutionfunds.tutionfunds_home(request,template_name=template_name)

def tutionfunds_school_list(request,tid, template_name='moe_portal/tutionfunds_schools_list.html'):
	return tutionfunds.tutionfunds_school_list(request,tid, template_name=template_name)

def tutionfunds_school_stud_list(request,tid, template_name='moe_portal/tutionfunds_list.html'):
	return tutionfunds.tutionfunds_school_stud_list(request,tid, template_name=template_name)

def tutionfunds_create(request, template_name='moe_portal/tutionfunds_form.html'):
	return tutionfunds.tutionfunds_create(request, template_name=template_name)

def tutionfunds_update(request , pk, template_name='moe_portal/tutionfunds_form.html'):
	return tutionfunds.tutionfunds_update(request , pk, template_name=template_name)

def tutionfunds_delete(request, pk, template_name='moe_portal/tutionfunds_confirm_delete.html'):
	return tutionfunds.tutionfunds_delete(request, pk, template_name=template_name)
