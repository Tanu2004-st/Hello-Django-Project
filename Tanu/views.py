from django.shortcuts import render, HttpResponse
from datetime import datetime
from Tanu.models import Contact
from django.contrib import messages


def index(request):
    context ={
        'variable':'This is set'
    }
    return render (request,'index.html', context)
   #  return HttpResponse("Hello Tanu! This is the home page.")

def about(request):
    return render (request,'about.html')
    #return HttpResponse("This is the About page of Tanu app.")


def services(request):
    return render (request,'services.html')
    #return HttpResponse("This is the service page .")
#makemigrations - create changes  and store in a file 
#migrate- apply the pendding changes  created by makemigrations
def contact(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = Contact(name = name,email= email,phone = phone,desc= desc)
        contact.save()
        messages.success(request, "Your message has been sent.")
        return render(request, 'contact.html',{'success': True} )
    return render (request,'contact.html')
    #return HttpResponse("This is the contact page .")    

