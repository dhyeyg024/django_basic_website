import email
from unicodedata import name
from django.shortcuts import render, HttpResponse
from datetime import datetime
from MyApp.models import Contact
from MyApp.models import Component
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def search_result(request):
    if request.method == "POST":
        searched = request.POST['searched']
        components = Component.objects.filter(name__contains=searched)
        return render(request, 'search_result.html',
        {'searched':searched,
        'components':components})
    else:
        return render(request, 'search_result.html')

def index(request):
    context = {
        'variable1':'this is sent',
        'variable2':'this is also sent'
    }
    
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is Service's page")

def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mob = request.POST.get('mob')
        subject = request.POST.get('subject')
        msg = request.POST.get('msg')
        contact = Contact(name=name, email=email, mob=mob, subject=subject, msg=msg, date=datetime.today())
        contact.save()
        data = {'name' : name,
                'email' : email,
                'subject' : subject,
                'msg' : msg}
        mail = '''
            Subject: {} 
            New Message: {}

            From: {}        
        '''.format(data['subject'], data['msg'], data['email'])
        send_mail(data['subject'], mail, '', ['admin's emailID'])
        messages.success(request, 'Your message has been sent Successfully!!')
    return render(request, 'contact.html')
    # return HttpResponse("This is ContactUs page")
