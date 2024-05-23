from django.views.generic import ListView, TemplateView
from .models import Featured,Products


class ProductListView(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'product.html'


class FeaturedView(ListView):
    model = Featured
    context_object_name = 'products'
    template_name = 'home.html'
