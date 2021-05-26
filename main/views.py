from django.shortcuts import render
from django.views.generic import ListView

from .models import Product

# Create your views here.
class ProductsListView(ListView):
    model=Product
    template_name='home.html'
    context_object_name='products_list'