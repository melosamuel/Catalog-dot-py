from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/auth/login')
def messenger(request):
    return render(request, 'messenger.html')
