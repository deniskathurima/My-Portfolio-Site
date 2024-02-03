from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def contact_me(request):
    return render(request, 'contact_me.html')


def educationandskills(request):
    return render(request, 'educationandskills.html')


def projects(request):
    return render(request, 'projects.html')
