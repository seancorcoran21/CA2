from django.urls import path
from .views import HomePageView, ProductDetailsPageView, ShoppingCartPageView

urlpatterns = [
    path('cart/', ShoppingCartPageView.as_view(), name="shoppingCart"),
    path('products/', ProductDetailsPageView.as_view(), name="productDetails"),
    path('', HomePageView.as_view(), name='home'),
]