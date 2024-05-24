from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, CreateView
from .models import Featured, Products
from .forms import ContactForm


class ProductListView(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'product.html'


class FeaturedView(ListView):
    model = Featured
    context_object_name = 'products'
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(CreateView):
    success_url = '/'
    model = Products
    form_class = ContactForm
    template_name = 'contact.html'
