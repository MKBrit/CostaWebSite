from django.shortcuts import render
from .models import *

# Create your views here.
def index(response):
    return render(response, 'main/index.html', {})

def home(response):
    return render(response, 'main/base.html', {})

