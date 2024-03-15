from django.shortcuts import render,HttpResponse
from app1.rform import RegForm
from app1.models import RegistForm
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

# Create your views here.
def reg(request):
    if request.method=='GET':
        var=RegForm()
        return render(request,'rg.html',{'var':var})
    elif request.method=='POST':
        form=RegForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            p=form.password
            enc=make_password(p)
            form.password=enc
            form.save()
            subject='Konichiwaa'
            message=f'Hello {form.username} wassup,\n How you doing😎'
            email_from=settings.EMAIL_HOST_USER
            recipient_list =[form.email]
            send_mail(subject,message,email_from,recipient_list)
            return HttpResponse('Your data is saved and sent mail')
def read(request):
    var=RegistForm.objects.all()
    return render(request,'read.html',{'var':var})
def delete(request):
    RegistForm.objects.all().delete()
    return HttpResponse('All data is permanently cleared.')
def log(request):
    if request.method=='GET':
        var=AuthenticationForm()
        return render(request,'log.html',{'var':var})
    elif request.method=='POST':
        user=request.POST['username']
        pw=request.POST['password']
        # img=request.POST['img']
        v = authenticate(username=user,password=pw)
        if v is not None:
            return render(request,'home.html',{'var':user})
        else:
            return HttpResponse('Wrong username or password')