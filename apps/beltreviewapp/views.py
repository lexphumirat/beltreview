from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import auth




def index(request):
    return render(request , 'beltreviewapp/index.html')

def addbook(request):
    return render(request, 'beltreviewapp/books.html')
