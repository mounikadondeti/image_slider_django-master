from django.shortcuts import render
from .models import *

# Create your views here.

def Timer(request):
	return render(request, 'Timer.html')