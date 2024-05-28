
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
User = get_user_model()

# Create your views here.
def login(request):
    if request.method=="POST":
        user=authenticate(request,
        username=request.POST['username'],
        password=request.POST['password'])

        if user is not None:
            login(request, user)
            messages.success(request, 'User logged in!')
            return redirect("/")
            

        else:
            messages.error(request, 'Invalid Username or Password.')
            return redirect("/user/login")

    else:

        return render(request,"user/login.html")



def register(request):
    if request.method=="POST":
        User.objects.create_user(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password'],

        )

        return redirect("/user/login")
        



    else:
        return render(request,"user/register.html")



def logout_fn(request):

    logout(request)

    return redirect("/")