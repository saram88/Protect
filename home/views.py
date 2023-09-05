from django.shortcuts import render

# Create your views here.

def index(request):
    """  Return to Index page"""
    return render(request, 'home/index.html')