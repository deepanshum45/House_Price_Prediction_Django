from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def testpaper(request):
    que="who developed python?"
    a="dennis ritchie" 
    b="guide ven rossum"
    c="harsh patel"
    d="harsh suryawanshi"
    context={
        'que':que,
        'a':a,
        'b':b,
        'c':c,
        'd':d
}
    template=loader.get_template('testpaper.html')
    res=template.render(context,request)
    return HttpResponse(res)


def info(request):
    Name="Deepanshu Mehra"
    Department="AIDS"
    age="21"
    context={
        'Name':Name,
        'Department':Department,
        'age':age
}
    template=loader.get_template('testpaper.html')
    res=template.render(context,request)
    return HttpResponse(res)


def sum(request):
    a="2"
    b="5"
    c="6"
    total= int(a)+int(b)+int(c)
    context={
        'a':a,
        'b':b,
        'c':c,
        'sum':total
}
    template=loader.get_template('add.html')
    res=template.render(context,request)
    return HttpResponse(res)

def result(request):
    context={
            'name':"Deepanshu Mehra",
            'marks':82
    }
    return render(request,'result.html',context)

def voting(request):
    context={
            'name':"Deepanshu Mehra",
            'Country':"India",
            'age':21
    }
    return render(request,'voting.html',context)



def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
