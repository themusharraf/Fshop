from django.urls import path
from .views import FeaturedView, ProductListView, ContactView, AboutView, LoginViews, RegisterView

urlpatterns = [
    path('', FeaturedView.as_view(), name='top_product'),
    path('product', ProductListView.as_view(), name='product_list'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('login', LoginViews.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
]
