from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
# Create your views here.
def index(request):
   return render(request,'index.html')


def product(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request,'product.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method =="POST":
      name = request.POST.get("name")
      email = request.POST.get("email")
      phone = request.POST.get("phone")
      message = request.POST.get("msg")
      c = Contact(name = name,email = email, phone = phone, msg = message)
      c.save()
      return redirect('/contact')
    
   
    return render(request,'contact.html')

def loginView(request):
   if request.method == "POST":
      userName = request.POST.get('userName')
      password = request.POST.get('password')
      user = authenticate(username=userName, password=password)
      if user is not None:
         login(request,user)
         return redirect('/home')
      else:
         return render(request,"login.html",{'error':"Username or password is incorrect"})
    
   return render(request,"login.html")
def signupView(request):
   if request.method =="POST":
      firstName = request.POST.get('firstName')
      lastName = request.POST.get('lastName')
      userName = request.POST.get('userName')
      email = request.POST.get('email')
      password = request.POST.get('password')
      cpassword = request.POST.get('cpassword')

      user = User.objects.create_user(userName,email,password)
      user.first_name = firstName
      user.last_name = lastName
      user.save()
      return redirect('/login')
       

   return render(request,"signup.html")


def logoutView(request):
   logout(request)
   return render(request,"index.html")
