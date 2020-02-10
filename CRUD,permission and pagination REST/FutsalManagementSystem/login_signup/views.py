from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseForbidden
from django.template import Template,Context
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# view function for sign up 
def view_signup(request):
    if request.method =="GET":
        return render(request,'signup.html')
    else:
        user = User.objects.create_user(username=request.POST['username'],password=request.POST['pwd'],email=request.POST['email'])
        user.save()
        return HttpResponse("Signup Successful")

# for log in
def view_login_user(request):
    if request.method =="GET":
        return render (request,'login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['username'],password=request.POST['pwd'])
        print(user)
        if user is not None:
            login(request,user)
            return redirect('../../events/viewevent')
        else:
            return HttpResponse("Authentication Failed")

# for logout
def view_logout(request):
    logout(request)
    return redirect('../login')
