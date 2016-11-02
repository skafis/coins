from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages

from sysadmin.forms import EntryYearForm,ClassesDropdownForm,CountyDropdownForm,StreamDropdownForm,GenderDropdownForm,SchoolDropdownForm,UserDropdownForm,GenderDropdownForm,DormitoryForm

from school.models import SchoolProfiles,SchoolStaff,Classes,Streams,ClassStreams,SchoolType,Gender,PaymentMethods,Dormitory,House, Terms,Months,Subjects,Papers,CategoryType,Category,EntryYear

from students.models import StudentProfiles,StudentLocation,YellowForm,StudentDormitory,StudentClubs,StudentSports,HolidayJobs,StudentSupplies
#from pos_portal.models import StudentAccounts

from students.forms import StudentDropDownForm

from django.http import Http404, HttpResponse
import json

from django.db import transaction

from django.utils import timezone

from django.db import transaction

from discipline.models import DisciplineCases

from library.models import Books
from library.forms import BooksForm

def index(request):
	ctx = {}
	try:
		rows=User.objects.all()
		ctx['rows'] = rows
		ctx['main_title'] = 'sch_portal reg form'
		ctx['breadcrump'] = 'Manage sch_portal reg'
		ctx['span_size'] = 12
	except:
		#raise
		#messages.add_message(request, messages.INFO, 'Record already exists ')
		pass
	return render(request, 'sch_portal/index.html', ctx)

def register(request):
	ctx = {}

	schclassesform = ClassesDropdownForm(request.POST or None)
	countyform = CountyDropdownForm(request.POST or None)
	streamform = StreamDropdownForm(request.POST or None)
	genderform = GenderDropdownForm(request.POST or None)
	schoolform = SchoolDropdownForm(request.POST or None)
	entryyearform = EntryYearForm(request.POST or None)
	dormitoryform = DormitoryForm(request.POST or None)

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		schools = SchoolProfiles.objects.all().values('id','schname')
		studentprofiles = StudentProfiles.objects.all().values('name__schname','admno','username__username','firstname','secondname','lastname','gender__gender__gender','current_classes__classes__classes', 'current_stream__streams__stream','accountnumber','encryped_acc_no')
		yellowform = YellowForm.objects.all().values('name__schname','entryyear__entryyear','indexnumber','firstname','secondname','lastname','gender__gender__gender')

		#data = json.dumps(list(obj))
		data = {'schools': list(schools),'studentprofiles': list(studentprofiles),'yellowform': list(yellowform),}

		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'School Register'
		ctx['breadcrump'] = 'School Register'
		ctx['span_size'] = 12
		ctx['schclassesform'] = schclassesform
		ctx['countyform'] = countyform
		ctx['streamform'] = streamform
		ctx['schoolform'] = schoolform
		ctx['genderform'] = genderform
		ctx['entryyearform'] = entryyearform
		ctx['dormitoryform'] = dormitoryform

		return render(request, 'sch_portal/register.html', ctx)


def syssettings(request):
	
	ctx = {}
	form = EntryYearForm(request.POST or None)
	genderform = GenderDropdownForm(request.POST or None)
	classesform = ClassesDropdownForm(request.POST or None)
	streamform = StreamDropdownForm(request.POST or None)
	dormitoryform = DormitoryForm(request.POST or None)

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		if request.user.is_superuser:
				schentryyear = EntryYear.objects.all().values('id','entryyear__entryyear')
				schclasses = Classes.objects.all().values('id','classes__classes',)
				dormitory = Dormitory.objects.all().values('id','dormitory__dormitory',)
				paymentmethod = PaymentMethods.objects.all().values('id','paymentmethods',)
				terms = Terms.objects.all().values('id','terms',)
				schstream = Streams.objects.all().values('id','streams__stream',)
				subject = Subjects.objects.all().values('id','subject',)
				paper = Papers.objects.all().values('id','papername',)
				gender = Gender.objects.all().values('id','gender__gender',)
				category = Category.objects.all().values('id','category',)
				month = Months.objects.all().values('id','month',)
				house = House.objects.all().values('id','house',)
				schooltype = SchoolType.objects.all().values('id','schooltype',)
				categorytype = CategoryType.objects.all().values('id','categorytype',)
				#country = Country.objects.all().values('id','country',)
				#county = County.objects.all().values('id','countyname',)
				#voteheads = VoteHeads.objects.all().values('id','voteheads',)
				#grades = Grades.objects.all().values('id','grades','points',) 


				#data = json.dumps(list(obj))
				data = {'schentryyear': list(schentryyear),'schclasses': list(schclasses),'dormitory': list(dormitory),'paymentmethods': list(paymentmethod),'terms': list(terms),'schstream': list(schstream),'subject': list(subject),'paper': list(paper),'gender': list(gender), 'category': list(category), 'month': list(month), 'house': list(house), 'schooltype': list(schooltype),'categorytype': list(categorytype),  }
		else:
				ss=SchoolStaff.objects.get(owner_id=request.user.id)
				schentryyear = EntryYear.objects.filter(name_id=ss.name_id).values('id','entryyear__entryyear')
				schclasses = Classes.objects.filter(name_id=ss.name_id).values('id','classes__classes',)
				dormitory = Dormitory.objects.filter(name_id=ss.name_id).values('id','dormitory__dormitory',)
				paymentmethod = PaymentMethods.objects.filter(name_id=ss.name_id).values('id','paymentmethods',)
				terms = Terms.objects.filter(name_id=ss.name_id).values('id','terms',)
				schstream = Streams.objects.filter(name_id=ss.name_id).values('id','streams__stream',)
				subject = Subjects.objects.filter(name_id=ss.name_id).values('id','subject',)
				paper = Papers.objects.filter(name_id=ss.name_id).values('id','papername',)
				gender = Gender.objects.filter(name_id=ss.name_id).values('id','gender__gender',)
				category = Category.objects.filter(name_id=ss.name_id).values('id','category',)
				month = Months.objects.filter(name_id=ss.name_id).values('id','month',)
				house = House.objects.filter(name_id=ss.name_id).values('id','house',)
				schooltype = SchoolType.objects.filter(name_id=ss.name_id).values('id','schooltype',)
				categorytype = CategoryType.objects.filter(name_id=ss.name_id).values('id','categorytype',)
				#country = Country.objects.all().values('id','country',)
				#county = County.objects.all().values('id','countyname',)
				#voteheads = VoteHeads.objects.all().values('id','voteheads',)
				#grades = Grades.objects.all().values('id','grades','points',) 


				#data = json.dumps(list(obj))
				data = {'schentryyear': list(schentryyear),'schclasses': list(schclasses),'dormitory': list(dormitory),'paymentmethods': list(paymentmethod),'terms': list(terms),'schstream': list(schstream),'subject': list(subject),'paper': list(paper),'gender': list(gender), 'category': list(category), 'month': list(month), 'house': list(house), 'schooltype': list(schooltype),'categorytype': list(categorytype),  }

		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'System settings'
		ctx['breadcrump'] = 'System settings'
		ctx['form'] = form
		ctx['genderform'] = genderform
		ctx['classesform'] = classesform
		ctx['streamform'] = streamform
		ctx['dormitoryform'] = dormitoryform
		ctx['span_size'] = 12
		return render(request, 'sch_portal/syssettings.html', ctx)

def studentclubs(request):
	ctx = {}
	studentdropdownform = StudentDropDownForm(request.POST or None)

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		studentclubs = StudentClubs.objects.all().values('studentprofiles__admno','studentprofiles__firstname','studentprofiles__secondname','studentprofiles__lastname','club')

		#data = json.dumps(list(obj))
		data = {'studentclubs': list(studentclubs),}

		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'School Register'
		ctx['breadcrump'] = 'School Register'
		ctx['span_size'] = 12
		ctx['studentdropdownform'] = studentdropdownform

		return render(request, 'sch_portal/studentclubs.html', ctx)


def holidayjobs(request):
	ctx = {}
	studentdropdownform = StudentDropDownForm(request.POST or None)

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		holidayjobs = HolidayJobs.objects.all().values('studentprofiles__admno','studentprofiles__firstname','studentprofiles__secondname','studentprofiles__lastname','job')

		#data = json.dumps(list(obj))
		data = {'holidayjobs': list(holidayjobs),}

		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'School Register'
		ctx['breadcrump'] = 'School Register'
		ctx['span_size'] = 12
		ctx['studentdropdownform'] = studentdropdownform

		return render(request, 'sch_portal/holidayjobs.html', ctx)


def studentsports(request):
	ctx = {}
	studentdropdownform = StudentDropDownForm(request.POST or None)

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		studentsports = StudentSports.objects.all().values('studentprofiles__admno','studentprofiles__firstname','studentprofiles__secondname','studentprofiles__lastname','sport')

		#data = json.dumps(list(obj))
		data = {'studentsports': list(studentsports),}

		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'School Register'
		ctx['breadcrump'] = 'School Register'
		ctx['studentdropdownform'] = studentdropdownform
		ctx['span_size'] = 12

		return render(request, 'sch_portal/studentsports.html', ctx)


def discipline(request):
	ctx = {}
	studentdropdownform = StudentDropDownForm(request.POST or None)

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		disciplinecases = DisciplineCases.objects.all().values('studentprofiles__admno','studentprofiles__firstname','studentprofiles__secondname','studentprofiles__lastname','category', 'blacklist','blacklistdate','whitelist','whitelistdate',)

		#data = json.dumps(list(obj))
		data = {'disciplinecases': list(disciplinecases),}

		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'School Register'
		ctx['breadcrump'] = 'School Register'
		ctx['studentdropdownform'] = studentdropdownform
		ctx['span_size'] = 12

		return render(request, 'sch_portal/disciplinecases.html', ctx)

def studentsupplies(request):
	ctx = {}
	studentdropdownform = StudentDropDownForm(request.POST or None)

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		studentsupplies = StudentSupplies.objects.all().values('studentprofiles__admno','studentprofiles__firstname','studentprofiles__secondname','studentprofiles__lastname','category','supply',)

		#data = json.dumps(list(obj))
		data = {'studentsupplies': list(studentsupplies),}

		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'School Register'
		ctx['breadcrump'] = 'School Register'
		ctx['studentdropdownform'] = studentdropdownform
		ctx['span_size'] = 12

		return render(request, 'sch_portal/studentsupplies.html', ctx)


def certsofachievment(request):
	ctx = {}
	studentdropdownform = StudentDropDownForm(request.POST or None)

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		#certsofachievment = CertsOfAchievment.objects.all().values('studentprofiles__admno','studentprofiles__firstname','studentprofiles__secondname','studentprofiles__lastname','category','supply',)

		#data = json.dumps(list(obj))
		#data = {'certsofachievment': list(certsofachievment),}
		data = {'certsofachievment': 'certsofachievment',}

		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'School Register'
		ctx['breadcrump'] = 'School Register'
		ctx['studentdropdownform'] = studentdropdownform
		ctx['span_size'] = 12

		return render(request, 'sch_portal/certsofachievment.html', ctx)

def academics(request):
		ctx = {}
		ctx['main_title'] = 'School Register'
		ctx['breadcrump'] = 'School Register'
		ctx['span_size'] = 12

		return render(request, 'sch_portal/academics.html', ctx)


def library(request):
	ctx = {}
	form = BooksForm(request.POST or None)

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		books = Books.objects.all().values('name__schname','bookname','author', 'category','boughtsponsored','amount','entrydate',)

		data = {'books': books,}

		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'School Register'
		ctx['breadcrump'] = 'School Register'
		ctx['form'] = form
		ctx['span_size'] = 12

		return render(request, 'sch_portal/library.html', ctx)


def books(request):
	ctx = {}
	form = BooksForm(request.POST or None)

	if request.is_ajax():
		#todo_items = ['Mow Lawn', 'Buy Groceries','Kiss Momole']
		#data = json.dumps(todo_items)
		books = Books.objects.all().values('name__schname','bookname','author', 'category','boughtsponsored','amount',)

		data = {'books': list(books),}

		return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		ctx['main_title'] = 'School Register'
		ctx['breadcrump'] = 'School Register'
		ctx['form'] = form
		ctx['span_size'] = 12

		return render(request, 'sch_portal/books.html', ctx)

# open a transaction
@transaction.atomic
def student_create(request):
	if request.is_ajax() and request.POST:
		schoolname= request.POST.get('schoolname')
		admno= request.POST.get('admno')
		username= request.POST.get('username')
		firstname= request.POST.get('firstname')
		secondname= request.POST.get('secondname')
		lastname= request.POST.get('lastname')
		gender= request.POST.get('gender')
		currentclasses= request.POST.get('currentclasses')
		currentstream= request.POST.get('currentstream')
		dateofbirth= request.POST.get('dateofbirth')
		county= request.POST.get('county')
		division= request.POST.get('division')
		constituency= request.POST.get('constituency')
		location= request.POST.get('location')
		sublocation= request.POST.get('sublocation')
		town = request.POST.get('town')
		accountnumber = request.POST.get('accountnumber')
		encryped_acc_no = 'XXXX%sXXXX'%accountnumber[4:11]
		expirerydate = request.POST.get('expirerydate')
		dormitory = request.POST.get('dormitory')

		sid=0
		try:

			obj = User.objects.create_user(username=username, password=username)
			obj.save()
			obj.first_name=firstname
			obj.last_name=lastname
			obj.is_active=True
			#obj.email=email
			obj.is_staff=True
			obj.save()

			sid = transaction.savepoint()

			ss=SchoolStaff.objects.get(owner_id=request.user.id)
			sp=StudentProfiles(name_id=schoolname,admno=admno,username_id=obj.id,firstname=firstname,secondname=secondname,lastname=lastname,gender_id=gender,current_classes_id=currentclasses,current_stream_id=currentstream, dateofbirth=dateofbirth,accountnumber=accountnumber,encryped_acc_no=encryped_acc_no,expirerydate=expirerydate);
			sp.save()
			pkid=sp.admno
			sl=StudentLocation(studentprofiles_id=pkid,county=county,division=division,constituency=constituency,location=location,sublocation=sublocation,town=town)
			sl.save()
			sd = StudentDormitory(studentprofiles_id=pkid,dormitory_id=dormitory)
			sd.save()

			#sa=StudentAccounts(studentprofiles_id=pkid,accountnumber=accountnumber,encryped_acc_no=encryped_acc_no,expirerydate=expirerydate)
			#sa.save()
			transaction.savepoint_commit(sid)
			data = {'message': "%s Saved "%(schoolname),'id': pkid,'schoolname':schoolname}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			transaction.savepoint_rollback(sid)
			data = {'message': "%s Not saved "%(schoolname)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def entryyear_create(request):
	if request.is_ajax() and request.POST:
		#schoolname= request.POST.get('schoolname')
		entryyear= request.POST.get('entryyear')

		try:
			ss=SchoolStaff.objects.get(owner_id=request.user.id)
			sp=EntryYear(name_id=ss.name_id,entryyear_id=entryyear);
			sp.save()
			data = {'message': "%s Saved "%(schoolname),'id': pkid,}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			transaction.savepoint_rollback(sid)
			data = {'message': "%s Not saved "%(schoolname)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def gender_create(request):
	if request.is_ajax() and request.POST:
		gender = request.POST.get('gender')
		try:
			ss=SchoolStaff.objects.get(owner_id=request.user.id)
			obj=Gender(gender_id=gender,name_id=ss.name_id);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(gender),'id': pkid,'gender':gender}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(gender)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def classes_create(request):
	if request.is_ajax() and request.POST:
		classes = request.POST.get('classes')

		try:
			ss=SchoolStaff.objects.get(owner_id=request.user.id)
			obj=Classes(classes_id=classes,name_id=ss.name_id);
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

def stream_create(request):
	if request.is_ajax() and request.POST:
		stream = request.POST.get('stream')

		try:
			ss=SchoolStaff.objects.get(owner_id=request.user.id)
			obj=Streams(streams=stream,name_id=ss.name_id)
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(stream),'id': pkid,'stream':stream}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(stream)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def yellowform_create(request):
	if request.is_ajax() and request.POST:
		entryyear = request.POST.get('entryyear')
		indexnumber = request.POST.get('indexnumber')
		firstname = request.POST.get('firstname')
		secondname = request.POST.get('secondname')
		lastname = request.POST.get('lastname')
		dateofbirth = request.POST.get('dateofbirth')
		gender = request.POST.get('gender')
		birthcert = request.POST.get('birthcert')
		pupilsinclasseght = request.POST.get('pupilsinclasseght')
		lastposition = request.POST.get('lastposition')
		lastmarks = request.POST.get('lastmarks')
		cocurricularevents = request.POST.get('cocurricularevents')
		headmasterapproval = request.POST.get('headmasterapproval')
		dateofapproval = request.POST.get('dateofapproval')
		headmasterphone = request.POST.get('headmasterphone')
		fax = request.POST.get('fax')
		email = request.POST.get('email')
		parentfullnames = request.POST.get('parentfullnames')
		parentgender = request.POST.get('parentgender')
		maritalstatus = request.POST.get('maritalstatus')
		parentdead = request.POST.get('parentdead')
		nationality = request.POST.get('nationality')
		nationalid = request.POST.get('nationalid')
		employment = request.POST.get('employment')
		inbusiness = request.POST.get('inbusiness')
		hasland = request.POST.get('hasland')
		otherincomeoptions = request.POST.get('otherincomeoptions')
		physicaladdress = request.POST.get('physicaladdress')
		listallsiblings = request.POST.get('listallsiblings')
		applicationinfo = request.POST.get('applicationinfo')
		cirtifydate = request.POST.get('cirtifydate')
		cirtifysigniture = request.POST.get('cirtifysigniture')
		cirtifyname = request.POST.get('cirtifyname')
		cirtifyoccupation = request.POST.get('cirtifyoccupation')
		cirtifyfax = request.POST.get('cirtifyfax')
		cirtifyphone = request.POST.get('cirtifyphone')
		cirtifyemail = request.POST.get('cirtifyemail')
		freefullnames = request.POST.get('freefullnames')
		freesignature = request.POST.get('freesignature')
		freephoneno = request.POST.get('freephoneno')
		recomenderfullnames = request.POST.get('recomenderfullnames')
		recomendersignature = request.POST.get('recomendersignature')
		recomenderoffice = request.POST.get('recomenderoffice')
		recomenderphoneno = request.POST.get('recomenderphoneno')
		kcpemath = request.POST.get('kcpemath')
		kcpeeng = request.POST.get('kcpeeng')
		kcpess = request.POST.get('kcpess')
		kcpekisw = request.POST.get('kcpekisw')
		kcpesci = request.POST.get('kcpesci')
		kcpetotal = request.POST.get('kcpetotal')

		try:
			ss=SchoolStaff.objects.get(owner_id=request.user.id)
			obj=YellowForm(name_id=ss.name_id,entryyear_id=entryyear,indexnumber=indexnumber,firstname=firstname,secondname=secondname,lastname=lastname,dateofbirth=dateofbirth,gender_id=1, birthcert=birthcert,pupilsinclasseght=pupilsinclasseght,lastposition=lastposition,lastmarks=lastmarks,cocurricularevents=cocurricularevents,headmasterapproval=headmasterapproval, dateofapproval=dateofapproval,headmasterphone=headmasterphone,fax=fax,email=email,parentfullnames=parentfullnames,parentgender_id=1,maritalstatus=maritalstatus,parentdead=parentdead, nationality=nationality,nationalid=nationalid,employment=employment,inbusiness=inbusiness,hasland=hasland,otherincomeoptions=otherincomeoptions,physicaladdress=physicaladdress, listallsiblings=listallsiblings,applicationinfo=applicationinfo,cirtifydate=cirtifydate,cirtifysigniture=cirtifysigniture,cirtifyname=cirtifyname,cirtifyoccupation=cirtifyoccupation, cirtifyfax=cirtifyfax,cirtifyphone=cirtifyphone,cirtifyemail=cirtifyemail,freefullnames=freefullnames,freesignature=freesignature,freephoneno=freephoneno, recomenderfullnames=recomenderfullnames,recomendersignature=recomendersignature,recomenderoffice=recomenderoffice,recomenderphoneno=recomenderphoneno, kcpemath=kcpemath,kcpeeng=kcpeeng,kcpess=kcpess,kcpekisw=kcpekisw,kcpesci=kcpesci,kcpetotal=kcpetotal)
			obj.save() 
			pkid=obj.id
			data = {'message': "%s Saved "%(indexnumber),'id': pkid,'indexnumber':indexnumber}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(stream)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def dormitory_create(request):
	if request.is_ajax() and request.POST:
		dormitory = request.POST.get('dormitory')
		entryyear = request.POST.get('entryyear')

		try:
			ss=SchoolStaff.objects.get(owner_id=request.user.id)
			obj=Dormitory(dormitory=dormitory,name_id=ss.name_id);
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

def studentsports_create(request):
	if request.is_ajax() and request.POST:
		sport = request.POST.get('sport')
		studentprofiles = request.POST.get('studentprofiles')

		try:
			obj=StudentSports(sport=sport,studentprofiles_id=studentprofiles);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(sport),'id': pkid,'sport':sport}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(sport)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def studentclubs_create(request):
	if request.is_ajax() and request.POST:
		club = request.POST.get('club')
		studentprofiles = request.POST.get('studentprofiles')

		try:
			obj=StudentClubs(club=club,studentprofiles_id=studentprofiles);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(club),'id': pkid,'club':club}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(club)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def holidayjobs_create(request):
	if request.is_ajax() and request.POST:
		job = request.POST.get('job')
		studentprofiles = request.POST.get('studentprofiles')

		try:
			obj=HolidayJobs(job=job,studentprofiles_id=studentprofiles);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(job),'id': pkid,'job':job}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(job)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def disciplinecases_create(request):
	if request.is_ajax() and request.POST:
		studentprofiles = request.POST.get('studentprofiles')
		category = request.POST.get('category')
		blacklist = request.POST.get('blacklist')
		blacklistdate = request.POST.get('blacklistdate')
		whitelist = request.POST.get('whitelist')
		whitelistdate = request.POST.get('whitelistdate')

		try:
			obj=DisciplineCases(blacklist=blacklist,blacklistdate=blacklistdate,whitelist=whitelist,whitelistdate=whitelistdate,category=category,studentprofiles_id=studentprofiles);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(blacklist),'id': pkid,'blacklist':blacklist}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(blacklist)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404


def studentsupplies_create(request):
	if request.is_ajax() and request.POST:
		studentprofiles = request.POST.get('studentprofiles')
		supply = request.POST.get('supply')
		category = request.POST.get('category')

		try:
			obj=StudentSupplies(category=category,supply=supply,studentprofiles_id=studentprofiles);
			obj.save()
			pkid=obj.id
			data = {'message': "%s Saved "%(supply),'id': pkid,'supply':supply}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(supply)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404

def book_create(request):
	if request.is_ajax() and request.POST:
		bookname = request.POST.get('bookname')
		author = request.POST.get('author')
		category = request.POST.get('category')
		boughtsponsored = request.POST.get('boughtsponsored')
		amount = request.POST.get('amount')

		try:
			ss=SchoolStaff.objects.get(owner_id=request.user.id)
			#obj=Book(name_id=ss.name_id,bookname=bookname,author=author,category=category,boughtsponsored=boughtsponsored,amount=amount)
			book=Book.objects.create(name_id=ss.name_id,bookname=bookname,author=author,category=category,boughtsponsored=boughtsponsored,amount=amount)
			book.save()
			#obj.save()
			#pkid=obj.id
			pkid=book.id
			data = {'message': "%s Saved "%(bookname),'id': pkid,'bookname':bookname}
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			raise
			data = {'message': "%s Not saved "%(bookname)}
			return HttpResponse(json.dumps(data), content_type='application/json')
	else:
		raise Http404
