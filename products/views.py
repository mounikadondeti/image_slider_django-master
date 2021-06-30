from django.shortcuts import render
from .models import *

# Create your views here.

def Timer(request):
	return render(request, 'Timer.html')

def Excel(request):
	return render(request, 'excel.html')