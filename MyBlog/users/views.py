from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('blogs')
        else:
            error_message = "Invalid username or password"
            return render(request, 'users/login.html', {'error_message': error_message})
    else:
        return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            error_message = "Passwords do not match"
            return render(request, 'users/register.html', {'error_message': error_message})
        
        if User.objects.filter(username=username).exists():
            error_message = "Username already exists"
            return render(request, 'users/register.html', {'error_message': error_message})
        
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        
        return redirect('/')  
    else:
        return render(request, 'users/register.html')

def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')