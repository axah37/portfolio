from django.urls import path
import jobs.views

urlpatterns = [
    path('', jobs.views.home, name='home'),
    path('jobs/<int:jobs_id>', jobs.views.detail, name='jobs_detail'),
    path('jobs/', jobs.views.summary, name='jobs_home')
]
