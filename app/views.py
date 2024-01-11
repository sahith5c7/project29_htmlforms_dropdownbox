from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        QLTO=Topic.objects.all()
        d={'topics':QLTO}    
        return render(request,'display_topic.html',context=d)
    return render(request,'insert_topic.html')


def display_topic(request):
    QLTO=Topic.objects.all()
    d1={'topics':QLTO}
    return render(request,'display_topic.html',context=d1)

def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}    
    if request.method=='POST':
        tn=request.POST['tn']
        n=request.POST['na']
        u=request.POST['u']
        to=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
        WO.save()
        QLWO=Webpage.objects.all()
        d={'webpages':QLWO}
        return render(request,'display_webpage.html',context=d)
    return render(request,'insert_webpage.html',context=d)

def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpage.html',context=d)


def insert_accessrecord(request):
    if request.method=='POST':
        n=request.POST['n']
        a=request.POST['a']
        d=request.POST['d']

        AO=AccessRecord.objects.get_or_create(name=n,author=a,date=d)[0]
        AO.save()
        QLAO=AccessRecord.objects.all()
        d={'accessrecords':QLAO}    
        return render(request,'display_accessrecord.html',context=d)
    return render(request,'insert_accessrecord.html')
   

def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'accessrecords':QLAO}
    return render(request,'display_accessrecord.html',context=d)


def select_multiple_webpages(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)
        d1={'webpages':QLWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'select_multiple_webpages.html',d)

def checkbox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'checkbox.html',context=d)

