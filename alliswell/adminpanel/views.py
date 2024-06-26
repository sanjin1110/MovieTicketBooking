from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def adminlogin(request):
    if (request.method=="POST"):
        em=request.POST['em']
        
        ps=request.POST['ps']
        
        user=authenticate(request,username=em,password=ps)

        if user is not None:
            if user.is_superuser == 1:
                login(request,user)
                return redirect('/admin/home')
            else:
                messages.error(request,"Username and Password Don't Match, Please Try Again !")
                return redirect('/admin')
        else:
            messages.error(request,"Username and Password Don't Match, Please Try Again !")
            return redirect('/admin')

    else:
        return render(request, 'admin/adminlogin.html')