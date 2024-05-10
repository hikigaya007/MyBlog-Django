from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by('-date')
    print(blogs)
    return render(request , 'blogs/home.html' , {'blogs': blogs})

def blog_page(request , slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogs/blog_page.html', {'blog': blog})
