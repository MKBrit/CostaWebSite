from django.shortcuts import render
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(response):
    return render(response, 'main/index.html', {})

def home(response):
    return render(response, 'main/base.html', {})

def create(response):
    form = CreateNewList()
    return render(response, 'main/create.html', {"form":form})
    
