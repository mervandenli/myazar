from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext as _

# Create your views here.
def switch_lang(request):
    return render(request, 'pages/index.html')
    
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def method(request):
    return render(request, 'pages/method.html')

def rates(request):
    return render(request, 'pages/rates.html')