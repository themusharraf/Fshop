from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormView
from .forms import SignupForm, LoginForm, ContactForm
from .models import Featured, Products, AboutView


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginViews(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password')
            return self.form_invalid(form)


class ProductListView(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'product.html'


class FeaturedView(ListView):
    model = Featured
    context_object_name = 'products'
    template_name = 'home.html'


class AboutView(ListView):
    model = AboutView
    context_object_name = 'abouts'
    template_name = 'about.html'


class ContactView(CreateView):
    success_url = '/'
    model = Products
    form_class = ContactForm
    template_name = 'contact.html'
