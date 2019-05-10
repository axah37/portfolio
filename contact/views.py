from django.shortcuts import render

# Create your views here.
def home(response):
	return render(response, 'contact/home.html',{'active_page':'contact','title':'contact'})