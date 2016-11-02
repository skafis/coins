from django.shortcuts import redirect

def check_authenticated(request):
	if not request.user.is_authenticated():
		return redirect('%s?next=%s' % ('/login/signin/', request.path))

