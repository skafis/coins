from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
import json
from django.http import Http404, HttpResponse

from django.db import transaction


from school.models import SchoolProfiles,Classes,Streams,SchoolStaff
from students.models import StudentProfiles


from sysadmin.models import EntryYear,Classes as SysClasses,Dormitory as SysDormitory,PaymentMethod as SysPaymentMethod,PaymentMethod as SysPaymentMethod,Term as SysTerm,Stream as SysStream,Subject as SysSubject,Paper as SysPaper, Gender as SysGender, Category as SysCategory, Months as SysMonths, House as SysHouse, SchoolType as SysSchoolType,CategoryType as SysCategoryType, Country as SysCountry, County as SysCounty, VoteHeads as SysVoteHeads, Grades as SysGrades

from sysadmin.forms import EntryYearForm,ClassesDropdownForm,CountyDropdownForm,StreamDropdownForm,UserDropdownForm,SchoolDropdownForm,UserDropdownForm,GenderDropdownForm

def index(request):
	ctx = {}
	try:
		rows=User.objects.all()
		ctx['rows'] = rows
		ctx['main_title'] = 'System Settings'
		ctx['breadcrump'] = 'System Settings'
		ctx['span_size'] = 12
	except:
		#raise
		#messages.add_message(request, messages.INFO, 'Record already exists ')
		pass
	return render(request, 'sysadmin/index.html', ctx)

def syssettings(request):
	
	ctx = {}
	form = EntryYearForm(request.POST or None)
	userform = UserDropdownForm(request.POST or None)
	schclassesform = SchoolDropdownForm(request.POST or None)

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)

		entryyear = EntryYear.objects.all().values('id','entryyear')
		classes = SysClasses.objects.all().values('id','entryyear','classes',)
		dormitory = SysDormitory.objects.all().values('id','entryyear','dormitory',)
		paymentmethod = SysPaymentMethod.objects.all().values('id','paymentmethods',)
		terms = SysTerm.objects.all().values('id','term','entryyear',)
		stream = SysStream.objects.all().values('id','stream','entryyear',)
		subject = SysSubject.objects.all().values('id','subject','entryyear',)
		paper = SysPaper.objects.all().values('id','paper','entryyear',)
		gender = SysGender.objects.all().values('id','gender','entryyear',)
		category = SysCategory.objects.all().values('id','category','entryyear',)
		month = SysMonths.objects.all().values('id','month','entryyear',)
		house = SysHouse.objects.all().values('id','house','entryyear',)
		schooltype = SysSchoolType.objects.all().values('id','schooltype',)
		categorytype = SysCategoryType.objects.all().values('id','categorytype','entryyear',)
		country = SysCountry.objects.all().values('id','country',)
		county = SysCounty.objects.all().values('id','countyname',)
		voteheads = SysVoteHeads.objects.all().values('id','voteheads',)
		grades = SysGrades.objects.all().values('id','grades','points',) 
		schoolstaff = SchoolStaff.objects.all().values('id','name__schname','owner__username',) 

		#data = json.dumps(list(obj))
		data = {'entryyear': list(entryyear),'classes': list(classes),'dormitory': list(dormitory),'paymentmethods': list(paymentmethod),'terms': list(terms),'stream': list(stream),'subject': list(subject),'paper': list(paper),'gender': list(gender), 'category': list(category), 'month': list(month), 'house': list(house), 'schooltype': list(schooltype),'categorytype': list(categorytype), 'country': list(country), 'county': list(county), 'voteheads': list(voteheads), 'grades': list(grades),'schoolstaff': list(schoolstaff),}
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'System settings'
		ctx['breadcrump'] = 'System settings'
		ctx['form'] = form
		ctx['userform'] = userform
		ctx['schclassesform'] = schclassesform
		ctx['span_size'] = 12
		return render(request, 'sysadmin/syssettings.html', ctx)

def school(request):
	ctx = {}

	schclassesform = ClassesDropdownForm(request.POST or None)
	countyform = CountyDropdownForm(request.POST or None)
	streamform = StreamDropdownForm(request.POST or None)

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		sysadminsch = SchoolProfiles.objects.all().values('id','schname','location','noofmerchants','phonenumber','encryped_acc_no','schfeesbalance','pocketmoneybalance','savingsbalance',)
		#data = json.dumps(list(obj))
		data = {'sysadminsch': list(sysadminsch),}
		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'School Register'
		ctx['breadcrump'] = 'School Register'
		ctx['span_size'] = 12
		ctx['schclassesform'] = schclassesform
		ctx['countyform'] = countyform
		ctx['streamform'] = streamform
		return render(request, 'sysadmin/schools.html', ctx)


def entryyear_create(request):
	if request.is_ajax() and request.POST:
		entryyear = request.POST.get('entryyear')
		currentyear = request.POST.get('currentyear')

		try:
			obj=EntryYear(entryyear=entryyear,currentyear='t');
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(entryyear),'id': pkid,'entryyear':entryyear,'currentyear':currentyear}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(entryyear)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def classes_create(request):
	if request.is_ajax() and request.POST:
		classes = request.POST.get('classes')
		entryyear = request.POST.get('entryyear')

		try:
			obj=SysClasses(entryyear_id=entryyear,classes=classes);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(classes),'id': pkid,'entryyear':entryyear,'classes':classes}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(classes)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def dormitory_create(request):
	if request.is_ajax() and request.POST:
		dormitory = request.POST.get('dormitory')
		entryyear = request.POST.get('entryyear')

		try:
			obj=SysDormitory(entryyear_id=entryyear,dormitory=dormitory);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(dormitory),'id': pkid,'entryyear':entryyear,'dormitory':dormitory}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(dormitory)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def paymentmethods_create(request):
	if request.is_ajax() and request.POST:
		paymentmethods = request.POST.get('paymentmethods')

		try:
			obj=SysPaymentMethod(paymentmethods=paymentmethods);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(paymentmethods),'id': pkid,'paymentmethods':paymentmethods}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(paymentmethods)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def terms_create(request):
	if request.is_ajax() and request.POST:
		terms = request.POST.get('terms')
		entryyear = request.POST.get('entryyear')

		try:
			obj=SysTerm(entryyear_id=entryyear,term=terms)
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(terms),'id': pkid,'entryyear':entryyear,'terms':terms}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(terms)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def stream_create(request):
	if request.is_ajax() and request.POST:
		stream = request.POST.get('stream')
		entryyear = request.POST.get('entryyear')

		try:
			obj=SysStream(entryyear_id=entryyear,stream=stream)
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(stream),'id': pkid,'entryyear':entryyear,'stream':stream}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(stream)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def subject_create(request):
	if request.is_ajax() and request.POST:
		subject = request.POST.get('subject')
		subject_code = request.POST.get('subject_code')
		entryyear = request.POST.get('entryyear')

		try:
			obj=SysSubject(entryyear_id=entryyear,subject=subject,subject_code=subject_code)
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(subject),'id': pkid,'entryyear':entryyear,'subject':subject,'subject_code':subject_code}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(subject)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def paper_create(request):
	if request.is_ajax() and request.POST:
		paper = request.POST.get('paper')
		paper_code = request.POST.get('paper_code')
		entryyear = request.POST.get('entryyear')

		try:
			obj=SysPaper(entryyear_id=entryyear,paper=paper,paper_code=paper_code)
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(paper),'id': pkid,'entryyear':entryyear,'paper':paper,'paper_code':paper_code}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(paper)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def gender_create(request):
	if request.is_ajax() and request.POST:
		gender = request.POST.get('gender')
		entryyear = request.POST.get('entryyear')

		try:
			obj=SysGender(entryyear_id=entryyear,gender=gender);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(gender),'id': pkid,'entryyear':entryyear,'gender':gender}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(gender)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def category_create(request):
	if request.is_ajax() and request.POST:
		category = request.POST.get('category')
		entryyear = request.POST.get('entryyear')

		try:
			obj=SysCategory(entryyear_id=entryyear,category=category);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(category),'id': pkid,'entryyear':entryyear,'category':category}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(category)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def month_create(request):
	if request.is_ajax() and request.POST:
		month = request.POST.get('month')
		entryyear = request.POST.get('entryyear')

		try:
			obj=SysMonths(entryyear_id=entryyear,month=month);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(month),'id': pkid,'entryyear':entryyear,'month':month}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(category)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def house_create(request):
	if request.is_ajax() and request.POST:
		house = request.POST.get('house')
		entryyear = request.POST.get('entryyear')

		try:
			obj=SysHouse(entryyear_id=entryyear,house=house);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(house),'id': pkid,'entryyear':entryyear,'house':house}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(house)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def schooltype_create(request):
	if request.is_ajax() and request.POST:
		schooltype = request.POST.get('schooltype')

		try:
			obj=SysSchoolType(schooltype=schooltype);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(schooltype),'id': pkid,'schooltype':schooltype}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(schooltype)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def categorytype_create(request):
	if request.is_ajax() and request.POST:
		categorytype = request.POST.get('categorytype')
		entryyear = request.POST.get('entryyear')

		try:
			obj=SysCategoryType(entryyear_id=entryyear,categorytype=categorytype);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(categorytype),'id': pkid,'entryyear':entryyear,'categorytype':categorytype}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(categorytype)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def country_create(request):
	if request.is_ajax() and request.POST:
		country = request.POST.get('country')

		try:
			obj=SysCountry(country=country);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(country),'id': pkid,'country':country}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(country)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404


def county_create(request):
	if request.is_ajax() and request.POST:
		countyname = request.POST.get('countyname')

		try:
			obj=SysCounty(countyname=countyname);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(countyname),'id': pkid,'countyname':countyname}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(countyname)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def voteheads_create(request):
	if request.is_ajax() and request.POST:
		voteheads = request.POST.get('voteheads')
		entryyear = request.POST.get('entryyear')

		try:
			obj=SysVoteHeads(entryyear_id=entryyear,voteheads=voteheads);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(voteheads),'id': pkid,'entryyear':entryyear,'voteheads':voteheads}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(voteheads)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def grades_create(request):
	if request.is_ajax() and request.POST:
		grades = request.POST.get('grades')
		points = request.POST.get('points')

		try:
			obj=SysGrades(grades=grades,points=points)
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(grades),'id': pkid,'grades':grades,'points':points,}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(grades)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

# open a transaction
@transaction.atomic
def school_create(request):
	if request.is_ajax() and request.POST:

		schoolname= request.POST.get('schoolname')
		schoolaccname= request.POST.get('schoolaccname')
		secschoolaccname= request.POST.get('secschoolaccname')
		schoolphone= request.POST.get('schoolphone')
		schoolemail= request.POST.get('schoolemail')
		schoolcounty= request.POST.get('schoolcounty')
		schooldivision= request.POST.get('schooldivision')
		schoolconstituency= request.POST.get('schoolconstituency')
		schoollocation= request.POST.get('schoollocation')
		schoolsublocation= request.POST.get('schoolsublocation')
		schooltown= request.POST.get('schooltown')
		formone= request.POST.get('formone')
		formtwo= request.POST.get('formtwo')
		formthree= request.POST.get('formthree')
		formfour= request.POST.get('formfour')
		schoolstream= request.POST.get('schoolstream')
		secschoolstream= request.POST.get('secschoolstream')
		thirdschoolstream= request.POST.get('thirdschoolstream')
		fourthschoolstream= request.POST.get('fourthschoolstream')
		schoolstream= request.POST.get('schoolstream')
		schoolstream= request.POST.get('schoolstream')
		secschoolaccname= request.POST.get('secschoolaccname')
		thirdschoolaccname= request.POST.get('thirdschoolaccname')
		fourthschoolaccname= request.POST.get('fourthschoolaccname')

		sp=SchoolProfiles(schname=schoolname,motto="",mission="",vision="",accountnumber=schoolaccname,county=schoolcounty, division=schooldivision,constituency=schoolconstituency,location=schoollocation,sublocation=schoolsublocation, 
town=schooltown,phonenumber=schoolphone,email=schoolemail);
		sp.save()
		try:
			sid = transaction.savepoint()
			pkid=sp.id
			'''sa=SchoolAccounts(name_id=pkid,accountnumber=schoolaccname)
			sa.save()
			sa=SchoolAccounts(name_id=pkid,accountnumber=secschoolaccname)
			sa.save()
			sp=SchoolPhone(name_id=pkid,phonenumber=schoolphone)
			sp.save()
			se=SchoolEmails(name_id=pkid,email=schoolemail)
			se.save()
			sl=SchoolLocation(name_id=pkid,county=schoolcounty,division=schooldivision,constituency=schoolconstituency,location=schoollocation,sublocation=schoolsublocation,town=schooltown)
			sl.save()'''
			c = Classes(name_id=pkid,classes_id=formone)
			c.save()
			c = Classes(name_id=pkid,classes_id=formtwo)
			c.save()
			c = Classes(name_id=pkid,classes_id=formthree)
			c.save()
			c = Classes(name_id=pkid,classes_id=formfour)
			c.save()
			s=Streams(name_id=pkid,streams_id=schoolstream)
			s.save()
			s=Streams(name_id=pkid,streams_id=secschoolstream)
			s.save()
			s=Streams(name_id=pkid,streams_id=thirdschoolstream)
			s.save()
			s=Streams(name_id=pkid,streams_id=fourthschoolstream)
			s.save()
			transaction.savepoint_commit(sid)
			data = {'message': "%s Saved "%(schoolname),'id': pkid,'schoolname':schoolname}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			transaction.savepoint_rollback(sid)
			raise
			data = {'message': "%s Not saved "%(schoolname)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def student(request):
	ctx = {}

	schclassesform = ClassesDropdownForm(request.POST or None)
	countyform = CountyDropdownForm(request.POST or None)
	streamform = StreamDropdownForm(request.POST or None)
	genderform = GenderDropdownForm(request.POST or None)
	schoolform = SchoolDropdownForm(request.POST or None)

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		schools = SchoolProfiles.objects.all().values('id','schname')
		studentprofiles = StudentProfiles.objects.all().values('name__schname','admno','username__username','firstname','secondname','lastname','gender__gender__gender','current_classes__classes__classes', 'current_stream__streams__stream','accountnumber','encryped_acc_no')

		#data = json.dumps(list(obj))
		data = {'schools': list(schools),'studentprofiles': list(studentprofiles),}

		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'School student'
		ctx['breadcrump'] = 'School student'
		ctx['span_size'] = 12
		ctx['schclassesform'] = schclassesform
		ctx['countyform'] = countyform
		ctx['streamform'] = streamform
		ctx['schoolform'] = schoolform
		ctx['genderform'] = genderform

		return render(request, 'sch_portal/students.html', ctx)



def view_schools(request,pk):
	ctx = {}
	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		sp = SchoolProfiles.objects.get(pk=pk)
		obj = SchoolProfiles.objects.filter(pk=pk).values('id','name')
		sa=SchoolAccounts.objects.filter(name_id=sp.id)
		data = json.dumps(list(obj))
		return HttpResponse(data, content_type='application/json')
	else:
		ctx['main_title'] = 'School View'
		ctx['breadcrump'] = 'School View'
		ctx['span_size'] = 12
		return render(request, 'sysadmin/view_schools.html', ctx)

def view_schools_details(request,pk):
	rows = SchoolProfiles.objects.get(pk=pk)
	ctx = {}
	ctx['rows'] = rows
	ctx['main_title'] = 'System Settings'
	ctx['breadcrump'] = 'Manage '
	ctx['pk'] = pk
	ctx['span_size'] = 6
	return render(request, 'sysadmin/view_schools.html', ctx)


def schstaff_create(request):
	if request.is_ajax() and request.POST:
		schoolname= request.POST.get('schoolname')
		userdrpdwn= request.POST.get('userdrpdwn')

		try:
			sp=SchoolStaff(name_id=schoolname,owner_id=userdrpdwn);
			sp.save()
			data = {'message': "%s Saved "%(schoolname),'id': sp.id,'schoolname':schoolname}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			transaction.savepoint_rollback(sid)
			data = {'message': "%s Not saved "%(schoolname)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def check_auth():
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))
	else:
		user = User.objects.get(pk=request.user.id)
		if not user.has_perm('school.add_schoolprofiles'):
			messages.add_message(request, messages.INFO, 'Your credentials are Ok,but all permissions are revoked from you,kindly contact admin')
			return redirect('%s?next=%s' % ('/login/signin/', request.path))
