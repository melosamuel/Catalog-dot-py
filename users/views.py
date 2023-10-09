from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as login_user

def login(request):
    if request.method == "GET":
        return render(request, 'authentication/login.html')
    
    username = request.POST['username']
    password = request.POST['password']
    user = None
    
    if username != '' and password != '':
        user = authenticate(request, username=username, password=password)

    if user is None:
        err = True
        return redirect(reverse('login') + f'?err={err}')

    login_user(request, user)
    return redirect(reverse("messenger"))
