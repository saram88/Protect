from django.shortcuts import render

# Create your views here.

def index(request):
    """ Return to Index page"""
    return render(request, 'home/index.html')


def about(request):
    """ A view to return the about page """
    return render(request, 'home/about.html')


def company(request):
    """ A view to return the company page """
    return render(request, 'home/company.html')


def contact(request):
    """ A view to return the contact page """
    return render(request, 'home/contact.html')


def download(request):
    """ A view to return the download page """
    return render(request, 'home/download.html')

