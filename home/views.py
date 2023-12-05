from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm


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
    """ A view to display the contact form"""

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect(reverse('contact'))

        else:
            form = ContactForm()
            messages.warning(request, 'Message not sent. Please try again.')

    else:
        form = ContactForm()
#        if 'submitted' in request.GET:
#            form = ContactForm()

#    form = ContactForm()
    template = 'home/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def download(request):
    """ A view to return the download page """
    return render(request, 'home/download.html')
