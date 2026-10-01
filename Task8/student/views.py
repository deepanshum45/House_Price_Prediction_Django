from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from student.models import User,SRF
from django.urls import reverse


def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')


def saveuser(request):

    user1 = User()

    u = User.objects.filter(
        username=request.POST['username']
    )

    if not u:

        user1.username = request.POST['username']
        user1.password = request.POST['password']
        user1.name = request.POST['name']

        user1.save()

        return HttpResponseRedirect(reverse('login'))

    else:

        return render(
            request,
            'signup.html',
            {'errormessage': 'Username is Already Exists'}
        )


def login(request):
    return render(request, 'login.html')


def loginvalidation(request):

    try:

        user1 = User.objects.get(
            username=request.POST['username'],
            password=request.POST['password']
        )
          #--------------------Session Create-----------------
        request.session['username']=user1.username
        request.session['name']=user1.name
        return HttpResponseRedirect(reverse('srf'))


    except User.DoesNotExist:

        return render(
            request,
            'login.html',
            {'erg': 'Invalid username or password'}
        )


def srf(request):
    if request.method == "POST":
        s_id = request.POST['s_id']
        s_name = request.POST['s_name']
        s_branch = request.POST['s_branch']

        student = SRF(
            s_id=s_id,
            s_name=s_name,
            s_branch=s_branch
        )

        student.save()

        return render(request, 'registrationspage.html', {
            'message': 'Your record is saved successfully'
        })

    return render(request, 'registrationspage.html')


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('login'))