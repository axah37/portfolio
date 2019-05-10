from django.shortcuts import render, get_object_or_404
from jobs.models import Job

# Create your views here.

def home(request):
	jobs = Job.objects.order_by('-id')
	return render(request, 'jobs/home.html',{'jobs':jobs, 'active_page':'home','title':'Abdurahman Ahmed'})

def detail(request, jobs_id):
	job = get_object_or_404(Job, pk=jobs_id)
	return render(request, 'jobs/detail.html',{'job':job, 'active_page':'jobs','title':job.title})

def summary(request):
	jobs = Job.objects.order_by('-id')
	return render(request, 'jobs/summary.html',{'jobs':jobs, 'active_page':'jobs','title':'Abdurahman Ahmed','title':'Abdurahman\'s Projects'})