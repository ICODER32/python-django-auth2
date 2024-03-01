from django.shortcuts import render,redirect

# from .form import UserForm
from .forms import UserForm,LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import auth

from django.contrib.auth import authenticate,logout

def home(request):
    return render(request,'app/index.html')


def signup(request):
    userForm=UserForm()
    if request.method=='POST':
        userForm=UserForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            return redirect('login')
        else:
            context={'userForm':userForm}
            return render(request,'app/signup.html',context)    
    context={'userForm':userForm}   
    return render(request,'app/signup.html',context)


def login(request):
    form=LoginForm()

    if request.method=='POST':
        form=LoginForm(request,request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)
            print(user)
            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
            else:
                return redirect('login')
            
    context={'form':form}
    return render(request,'app/login.html',context)

@login_required(login_url='login')
def dashboard(request):
    return render(request,'app/dashboard.html')


def logout(request):
    auth.logout(request)
    return redirect('login')