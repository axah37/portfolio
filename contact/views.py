from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

# Create your views here.
def home(response):
	success = False
	if response.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(response.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			message_send = 'Email: {}\nMessage: {}'.format(from_email, message)
			try:
				send_mail(subject, message_send, settings.EMAIL_HOST_USER, ['abdahmed@live.ca'],fail_silently=False)
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			success = True
	return render(response, 'contact/home.html',{'active_page':'contact','title':'contact','form':form,'success':success})
