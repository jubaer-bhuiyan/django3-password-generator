from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': 'JubaerBhuiyan12'})

def password(request):
    return render(request, 'generator/password.html')