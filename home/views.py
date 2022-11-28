from django.shortcuts import render, redirect 
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

#password:loli1234

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    context={
        'variable1':"That's me",
        'variable2':"Suraj Gajul"
    }
    return render(request, 'index.html', context)
def about(request):
    #return HttpResponse("This is about page")
    return render(request, 'about.html')

def contact(request):
    #return HttpResponse("This is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def anime(request):
    #return HttpResponse("This is contact page")
    return render(request, 'anime.html')

def bollywood(request):
    #return HttpResponse("This is contact page")
    return render(request, 'bollywood.html')

def hollywood(request):
    #return HttpResponse("This is contact page")
    return render(request, 'hollywood.html')

def justarrived(request):
    #return HttpResponse("This is contact page")
    return render(request, 'justarrived.html')

def loginUser(request):
    #return HttpResponse("This is contact page")
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get("password")
        print(username, password)
        #check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    #return HttpResponse("This is contact page")
    return redirect("/login")


