from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def home(request):
    return HttpResponse("Welcome to my portfolio!")

def custom_404(request, exception):
    """Custom 404 error handler"""
    return HttpResponseNotFound("Page not found")
