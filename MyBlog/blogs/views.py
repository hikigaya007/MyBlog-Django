from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def home(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request , 'blogs/home.html' , {'blogs': blogs})

@login_required(login_url="/")
def blog_page(request , slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogs/blog_page.html', {'blog': blog})

@login_required(login_url="/")
def blog_new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        slug = request.POST.get('slug')
        image = request.FILES.get('image')
        
        if title:
        
            blog = Blog(title=title, body=body, slug=slug, image=image, author=request.user)
            blog.save()
            
            
            return redirect('blogs')  
        else:
            error_message = "Title is required And it must be less than 75 char"
            return render(request, 'blogs/blog_new.html', {'error_message': error_message})
    else:
        return render(request, 'blogs/blog_new.html')