from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, SRF
from django.urls import reverse
import joblib
def home(request):
    res = render(request, 'home.html')
    return res
def register(request):
    return render(request, 'registration.html')
# Save registration details
def saveuser(request):
    user1 = User()
    u = User.objects.filter(
        username=request.POST['username'])
    if not u:
        user1.username = request.POST['username']
        user1.password = request.POST['password']
        user1.name = request.POST['name']
        user1.email = request.POST['email']
        user1.save()
        return HttpResponseRedirect(
            reverse('login')
        )
    else:
        return render(
            request,
            'registration.html',
            {
                'errormessage': 'Username is Already Exists'
            })
def login(request):
    return render(request, 'login.html')
def loginvalidation(request):
    try:
        user1 = User.objects.get(
            username=request.POST['username'],
            password=request.POST['password'])
        return HttpResponseRedirect(
            reverse('spp')
        )
    except User.DoesNotExist:
        return render(
            request,
            'login.html',
            {
                'erg': 'Invalid username or password'
            })
def srf(request):
    if request.method == "POST":
        s_id = request.POST['s_id']
        s_name = request.POST['s_name']
        email = request.POST['email']
        password = request.POST['password']
        s_branch = request.POST['s_branch']
        student = SRF(s_id=s_id,s_name=s_name,email=email,password=password,s_branch=s_branch )
        student.save()
        return render(
            request,
            'result.html',
            {
                'message': 'Your record is saved successfully'
            })
    return render(
        request,
        'registration.html'
    )
# SPP / ML Prediction page
def spp(request):
    res = render(
        request,
        'spp.html'
    )
    return res
def result(request):
    scaler = joblib.load(
        'Scalermodel (1).pkl'
    )
    mlmodel = joblib.load(
        'mlmodel (1).pkl'
    )
    lis = []
    lis.append(
        float(request.GET['cgpa'])
    )
    lis.append(
        float(request.GET['iq'])
    )
    lis.append(
        float(request.GET['profile_score'])
    )
    scaled_input = scaler.transform([lis])
    ans = mlmodel.predict(scaled_input)[0]
    res = render(
        request,
        'result.html',
        {
            'ans': int(ans),
            'lis': lis
        }
    )
    return res
