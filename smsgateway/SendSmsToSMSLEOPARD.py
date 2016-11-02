#NOW SEND THE SMS
# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

from smsgateway.models import Sms
from smsgateway.models import PhoneBook

from django.utils import timezone

from school.models import SchoolStaff

from django.contrib import messages

class SendSmsToSMSLEOPARD():
	def __init__(self,to,message,request,modeladmin):
		# Specify your login credentials
		username = "luda";
		apikey   = "21def86928ef49f40eac01d65e69fc276283a8aa3be5f8678b24137b757d8abe";

		# Specify the numbers that you want to send to in a comma-separated list
		# Please ensure you include the country code (+254 for Kenya in this case)
		#for obj in queryset:
		#to      = str(obj.reciever);

		# And of course we want our recipients to know what we really do
		#message = str(obj.text);
		#message = request.POST['send_sms'];

		# Create a new instance of our awesome gateway class
		gateway = AfricasTalkingGateway(username, apikey)

		# Any gateway errors will be captured by our custom Exception class below, 
		# so wrap the call in a try-catch block
		try:
			# Thats it, hit send and we'll take care of the rest. 
			recipients = gateway.sendMessage(to, message)
			for recipient in recipients:
				# Note that only the Status "Success" means the message was sent

				try:
					st = SchoolStaff.objects.get(owner = request.user)
					pb = PhoneBook.objects.get(phoneno =  str(recipient['number']) )
				
					sms = Sms(name_id = st.name_id,reciever_id = str(pb.id),text = message,deliverystatus = recipient['status'],messageid = recipient['messageId'],cost = recipient['cost'],sendtime = timezone.now(),deleverytime = timezone.now(),owner = request.user)
					sms.save()

					if recipient['status'] == 'Insufficient Balance':
						modeladmin.message_user(request, "Dear,"+ str(request.user)+" Messages has not been sent due to "+recipient['status'],messages.ERROR )
				except:
					modeladmin.message_user(request, "Current user "+ str(request.user)+" has not been added to school staff",messages.ERROR )

		except AfricasTalkingGatewayException, e:
			modeladmin.message_user(request, _("Encountered an error while sending: %s") % {
	         str(e)
			 }, messages.ERROR)
