from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):


    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase') == 'on':
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if request.GET.get('special') == 'on':
        characters.extend(list('!@#$%^&*_'))

    if request.GET.get('numbers') == 'on':
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))

    if length > 20:
        length = 12
    elif length < 8:
        length = 8

    listpassword = random.choices(characters, k=length)

    thepassword = ''

    for letters in listpassword:
        thepassword += letters

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')