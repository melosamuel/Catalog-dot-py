from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def messenger(request):
    return render(request, 'messenger.html')
