from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib import messages,auth
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method== "POST":
        username = request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are logged in")
            return redirect('dashboard')
        else:
            messages.warning(request,"Invalid username or password")
            return redirect("login")
    return render(request,'accounts/login.html')




def register(request):

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cnf_password = request.POST['cnf_password']

        if password == cnf_password :
            if User.objects.filter(username=username).exists():
                messages.warning(request,"Username already exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request,"Email already exists")
                    return redirect('register')
                
                else :
                    user = User.objects.create_user(first_name = firstname ,
                                         last_name = lastname , 
                                         username = username,
                                         email=email,
                                         password=password)
                    user.save()
                    
                    return redirect('login')

        else:
            messages.warning(request,"password is not matching with confirm password")
            return redirect('register')
    return render(request,'accounts/register.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'accounts/after_login_dashboard.html')


def logout_user(request):
    logout(request)
    return redirect('login')
