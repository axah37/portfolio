from django.urls import path
import contact.views

urlpatterns = [
    path('', contact.views.home, name='contact_home'),
]
