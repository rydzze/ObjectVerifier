from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'home.html', context)

def result(request):
    context = {}
    return render(request, 'result.html', context)