from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


def home(request):
    return render(request, 'index.html')


def prices(request):
    return render(request, 'prices.html')
