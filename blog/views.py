from django.shortcuts import render, get_object_or_404
from blog.models import Blog
# Create your views here.
def home(request):
	blogs = Blog.objects.order_by('-date')
	return render(request, 'blog/home.html', {'blogs':blogs,'active_page':'blog','title':'Abdurahman\'s Blog'})
def detail(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/detail.html',{'blog':blog,'active_page':'blog','title':'Abdurahman\'s Blog'})