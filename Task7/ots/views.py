from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, TestHistory
from django.urls import reverse


# Home Page
def home(request):
    res = render(request, 'home.html')
    return res


# Signup Page
def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User(username=username,email=email,password=password)
        user.save()
        url = reverse('login')
        return HttpResponseRedirect(url)
    res = render(request, 'signup.html')
    return res


# Login Page
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username,password=password)
        if user:
            request.session['username'] = username
            url = reverse('dashboard')
            return HttpResponseRedirect(url)
        else:
            res = render(request, 'login.html')
            return res
    res = render(request, 'login.html')
    return res


# Dashboard
def dashboard(request):
    res = render(request, 'dashboard.html')
    return res


# Test 1
def test1(request):
    if request.method == "POST":
        answer = request.POST['answer']
        score = 0
        if answer == "Python":
            score = 1
        username = request.session['username']
        test = TestHistory(username=username,test_name="Test 1",total_questions=1,score=score)
        test.save()
        res = render(request, 'result.html', {'score': score, 'total': 1})
        return res
    res = render(request, 'test1.html')
    return res


# Test 3
def test3(request):
    if request.method == "POST":
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        score = 0
        if q1 == "Python":
            score = score + 1
        if q2 == "p":
            score = score + 1
        if q3 == "#":
            score = score + 1
        username = request.session['username']
        test = TestHistory(username=username,test_name="Test 3",total_questions=3,score=score )
        test.save()
        res = render(request, 'result.html', {
            'score': score,
            'total': 3
        })
        return res
    res = render(request, 'test3.html')
    return res


# Test 5
def test5(request):
    if request.method == "POST":
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        q4 = request.POST['q4']
        q5 = request.POST['q5']

        score = 0

        if q1 == "Python":
            score = score + 1

        if q2 == "p":
            score = score + 1

        if q3 == "#":
            score = score + 1

        if q4 == "def":
            score = score + 1

        if q5 == "a":
            score = score + 1

        username = request.session['username']

        test = TestHistory(username=username,test_name="Test 5",total_questions=5,score=score)
        test.save()
        res = render(request, 'result.html', {
            'score': score,
            'total': 5
        })

        return res

    res = render(request, 'test5.html')
    return res


# Test History
def history(request):

    username = request.session['username']

    tests = TestHistory.objects.filter(
        username=username
    )

    total_score = 0
    total_questions = 0

    for test in tests:
        total_score = total_score + test.score
        total_questions = total_questions + test.total_questions
    res = render(request, 'history.html', {'tests': tests,'total_score': total_score,'total_questions': total_questions })
    return res
