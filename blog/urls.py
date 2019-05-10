from django.urls import path
import blog.views
urlpatterns = [
    path('', blog.views.home, name='blog_home'),
    path('<int:blog_id>',blog.views.detail,name='blog_detail'),
]
