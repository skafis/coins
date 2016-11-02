from django.views import generic
from django.contrib.auth.models import User

class IndexView(generic.ListView):
	template_name = 'frontend/index.html'

	context_object_name = 'latest_poll_list'

	def get_queryset(self):
		"""
			Return the last five published polls (not including those set to be
			published in the future).
		"""
		return User.objects.all()
