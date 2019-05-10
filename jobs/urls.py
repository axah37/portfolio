from django.urls import path
import jobs.views

urlpatterns = [
	path('jobs/', jobs.views.summary, name='jobs_home'),
    path('<int:jobs_id>', jobs.views.detail, name='jobs_detail'),
]
