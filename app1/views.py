from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from app1.models import *
from django.core.mail import send_mail
from django.conf import settings
def homev(request):
    return render(request,'index.html')

def loginv(request):
    if request.user.is_authenticated:
        messages.warning(request,"Your already logged! ")
        return redirect('homepage')
    #logout(request)
    if request.method=="POST":
        a=request.POST.get('ip1')
        b=request.POST.get('ip2')
        result=authenticate(request,username=a,password=b)
        if result is not None:
            print(a,b,type(result))
            login(request,result)
            messages.success(request,"Thank you for coming back ! ")
            return redirect('aboutpage')
        else:
            messages.error(request,"Login required")
            return redirect('loginpage')
    return render(request,'login.html',{'is_login_page': True})


@login_required(login_url='/admin')
def createv(request):
    if request.method=="POST":
        c=request.POST.get('cap')
        p1=request.FILES.get('img1')
        p2=request.FILES.get('img2')
        p3=request.FILES.get('img3')
        p4=request.FILES.get('img4')
        p5=request.FILES.get('img5')
        obj=eventclub(pic1=p1,pic2=p2,pic3=p3,pic4=p4,pic5=p5,cap=c)
        obj.save()
        return redirect('eventpage')
    return render(request,'create.html')

def toastmasterv(request):
    return render(request,'tm.html')


def shutterbugv(request):
    return render(request,'sb.html')

def sarov(request):
    return render(request,'saro.html')

def nssv(request):
    return render(request,'nss.html')

def nccv(request):
    return render(request,'ncc.html')


def aboutv(request):
    return render(request,'about.html')

def contactv(request):
    if request.method=="POST":
        email=request.POST.get('mail')
        name=request.POST.get('name')
        subject=request.POST.get('sub')
        msg=request.POST.get('message')
        send_mail(email,name,subject,msg,[email],fail_silently=False)
    return render(request,'contact.html')


def eventv(request):
    objs=eventclub.objects.all()[::-1]
    return render(request,'event.html',{'posts':objs})


def clubv(request):
    return render(request,'club.html')

def staffv(request):
    result=eventclub.objects.all()[::-1]
    return render(request,'staff.html',{'res':result})


def logoutV(request):
    logout(request)
    messages.info(request,"sucessfully you're logout")
    return redirect('loginpage')


@login_required(login_url='loginpage')
def delete(request,rid):
    if request.user.is_superuser:
        obj=eventclub.objects.get(id=rid)
        obj.delete()
        return redirect('staffpage')
    else:
        messages.warning(request,'This post is sucessfully deleted')
        return redirect('eventpage')
    
@login_required(login_url='loginpage')
def update(request,rid):
    if request.user.is_staff:
        if request.method=="POST":
            obj=eventclub.objects.get(id=rid)
            obj.cap=request.POST.get('cap')
            obj.pic1=request.POST.get('img1')
            obj.pic2=request.POST.get('img2')
            obj.pic3=request.POST.get('img3')
            obj.pic4=request.POST.get('img4')
            obj.pic5=request.POST.get('img5')
            #obj.pic6=request.POST.get('img6')
            obj.save()
            return redirect('staffpage')
            
        if eventclub.objects.filter(id=rid).exists():
            obj=eventclub.objects.get(id=rid)
            return render(request,'create.html',{'res':obj})
        return redirect('staffpage')
    return redirect('eventpage')

    
    
