from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import registerform
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def loginuser(request):
   if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         return redirect('home')
      else:
         return render(request,'authenticate/login.html',{})
   else:
      return render(request,'authenticate/login.html',{})

def  logoutuser(request):
   logout(request)
   return redirect('home')

def registeruser(request):
   if request.method == "POST":
      form = registerform(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data['username']
         password = form.cleaned_data['password1']
         user = authenticate(username=username, password=password)
         login(request,user)
         messages.success(request,("Registration success")) 
         return redirect('home')
   else:
        form = registerform()      
   return render(request,'authenticate/registration.html',{'form':form,})

