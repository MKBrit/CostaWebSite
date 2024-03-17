from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    categories = Category.objects.all()

    # Create a dictionary to hold products for each category
    listaProdutos = {}

    # Iterate over each category
    for category in categories:
        # Filter products belonging to the current category
        products = Product.objects.filter(category=category)
        # Add the filtered products to the dictionary
        listaProdutos[category] = products

    return render(request, 'main/index.html', {'listaProdutos': listaProdutos})