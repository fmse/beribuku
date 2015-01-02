from django.shortcuts import render, redirect
from urllib.request import Request

# Create your views here.

def program(request):
    data = {}
    return render(request, '', data)

def createProgram(request):
    data = {}
    return render(request, '', data)

def editProgram(request):
    data = {}
    return render(request, '', data)