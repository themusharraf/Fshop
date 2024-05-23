from django.urls import path
from .views import FeaturedView, ProductListView

urlpatterns = [
    path('', FeaturedView.as_view(), name='top_product'),
    path('product', ProductListView.as_view(), name='product_list'),
]
