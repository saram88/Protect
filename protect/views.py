from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "error/404.html", status=404)


def handler500(request):
    """500 Internal Server Error handling function"""
    return render(request, 'error/500.html', status=500)