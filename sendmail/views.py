from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core import mail
from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
from smtplib import SMTPConnectError
# Create your views here.

def index(request):
	send_mail('test mail', 'test message', settings.EMAIL_HOST_USER, ['arkaghosh024@gmail.com'], fail_silently=False)
	"""
	try:
		
	except SMTPConnectError as e:
		return HttpResponse(e)
	
	with mail.get_connection() as connection:
		mail.EmailMessage('test mail', 'test message', settings.EMAIL_HOST_USER, ['arka98787ghosh@gmail.com'], connection=connection).send()
	
	with mail.get_connection(
	    host=settings.EMAIL_HOST, 
	    port=settings.EMAIL_PORT, 
	    username=settings.EMAIL_HOST_USER, 
	    password=settings.EMAIL_HOST_PASSWORD, 
	    user_tls=settings.EMAIL_USE_TLS,
	) as mail.connection:
	    EmailMessage('test mail', 'test message', settings.EMAIL_HOST_USER, ['arka98787ghosh@gmail.com'], connection=connection).send()
	   #server = smtplib.SMTP(SERVER)
	   
	return HttpResponse('reaching here')
	

def index(request):
	import smtplib
	gmail_user = settings.EMAIL_HOST_USER
	gmail_pwd = settings.EMAIL_HOST_PASSWORD
	FROM = settings.EMAIL_HOST_USER
	TO = ['arka98787ghosh@gmail.com'] #must be a list
	SUBJECT = "Testing sending using gmail"
	TEXT = "Testing sending mail using gmail servers"
	message = "alsdkjfl"
	try :
		server = smtplib.SMTP("smtp.gmail.com:587") #or port 465 doesn't seem to work!
		server.ehlo()
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		server.sendmail(FROM, TO, message)
		server.quit()
		server.close()
		return HttpResponse ('successfully sent the mail')
	except Exception as detail:
		return HttpResponse (detail)
	return HttpResponse('reaching here')
	"""