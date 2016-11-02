import students.class_views.studentprofiles as studentprofiles
import students.class_views.studentcategory as studentcategory
import students.class_views.studentparent as studentparent
import students.class_views.parentphoneno as parentphoneno
import students.class_views.studentclassstream as studentclassstream
import students.class_views.studentsubject as studentsubject
import students.class_views.yellowform as yellowform

#STUDENT PROFILES
def studentprofiles_home(request,template_name='students/studentprofiles_list.html'):
 return studentprofiles.studentprofiles_home(request,template_name='students/studentprofiles_list.html')

def studentprofiles_create(request, template_name='students/studentprofiles_form.html'):
	return studentprofiles.studentprofiles_create(request, template_name='students/studentprofiles_form.html')

def studentprofiles_update(request , pk, template_name='students/studentprofiles_form.html'):
	return studentprofiles.studentprofiles_update(request , pk, template_name='students/studentprofiles_form.html')

def studentprofiles_delete(request, pk, template_name='students/studentprofiles_confirm_delete.html'):
	return studentprofiles.studentprofiles_delete(request, pk, template_name='students/studentprofiles_confirm_delete.html')

#STUDENT CATEGORY
def studentcategory_home(request,template_name='students/studentcategory_list.html'):
 return studentcategory.studentcategory_home(request,template_name='students/studentcategory_list.html')

def studentcategory_create(request, template_name='students/studentcategory_form.html'):
	return studentcategory.studentcategory_create(request, template_name='students/studentcategory_form.html')

def studentcategory_update(request , pk, template_name='students/studentcategory_form.html'):
	return studentcategory.studentcategory_update(request , pk, template_name='students/studentcategory_form.html')

def studentcategory_delete(request, pk, template_name='students/studentcategory_confirm_delete.html'):
	return studentcategory.studentcategory_delete(request, pk, template_name='students/studentcategory_confirm_delete.html')

#STUDENT PARENT
def studentparent_home(request,template_name='students/studentparent_list.html'):
 return studentparent.studentparent_home(request,template_name='students/studentparent_list.html')

def studentparent_create(request, template_name='students/studentparent_form.html'):
	return studentparent.studentparent_create(request, template_name='students/studentparent_form.html')

def studentparent_update(request , pk, template_name='students/studentparent_form.html'):
	return studentparent.studentparent_update(request , pk, template_name='students/studentparent_form.html')

def studentparent_delete(request, pk, template_name='students/studentparent_confirm_delete.html'):
	return studentparent.studentparent_delete(request, pk, template_name='students/studentparent_confirm_delete.html')

#PARENT PHONENO
def parentphoneno_home(request,template_name='students/parentphoneno_list.html'):
 return parentphoneno.parentphoneno_home(request,template_name='students/parentphoneno_list.html')

def parentphoneno_create(request, template_name='students/parentphoneno_form.html'):
	return parentphoneno.parentphoneno_create(request, template_name='students/parentphoneno_form.html')

def parentphoneno_update(request , pk, template_name='students/parentphoneno_form.html'):
	return parentphoneno.parentphoneno_update(request , pk, template_name='students/parentphoneno_form.html')

def parentphoneno_delete(request, pk, template_name='students/parentphoneno_confirm_delete.html'):
	return parentphoneno.parentphoneno_delete(request, pk, template_name='students/parentphoneno_confirm_delete.html')

#STUDENT CLASS STREAM
def studentclassstream_home(request,template_name='students/studentclassstream_list.html'):
 return studentclassstream.studentclassstream_home(request,template_name='students/studentclassstream_list.html')

def studentclassstream_create(request, template_name='students/studentclassstream_form.html'):
	return studentclassstream.studentclassstream_create(request, template_name='students/studentclassstream_form.html')

def studentclassstream_update(request , pk, template_name='students/studentclassstream_form.html'):
	return studentclassstream.studentclassstream_update(request , pk, template_name='students/studentclassstream_form.html')

def studentclassstream_delete(request, pk, template_name='students/studentclassstream_confirm_delete.html'):
	return studentclassstream.studentclassstream_delete(request, pk, template_name='students/studentclassstream_confirm_delete.html')

#STUDENT CLASS STREAM
def studentsubject_home(request,template_name='students/studentsubject_list.html'):
 return studentsubject.studentsubject_home(request,template_name='students/studentsubject_list.html')

def studentsubject_create(request, template_name='students/studentsubject_form.html'):
	return studentsubject.studentsubject_create(request, template_name='students/studentsubject_form.html')

def studentsubject_update(request , pk, template_name='students/studentsubject_form.html'):
	return studentsubject.studentsubject_update(request , pk, template_name='students/studentsubject_form.html')

def studentsubject_delete(request, pk, template_name='students/studentsubject_confirm_delete.html'):
	return studentsubject.studentsubject_delete(request, pk, template_name='students/studentsubject_confirm_delete.html')

#yellowform
def yellowform_home(request,template_name='students/yellowform_list.html'):
 return yellowform.yellowform_home(request,template_name='students/yellowform.html')

def yellowform_create(request, template_name='students/yellowform_form.html'):
	return yellowform.yellowform_create(request, template_name='students/yellowform_.html')

def yellowform_update(request , pk, template_name='students/yellowform_form.html'):
	return yellowform.yellowform_update(request , pk, template_name='students/yellowform.html')

def yellowform_delete(request, pk, template_name='students/yellowform_confirm_delete.html'):
	return yellowform.yellowform_delete(request, pk, template_name='students/yellowform.html')
