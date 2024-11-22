from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class ProductDetailsPageView(TemplateView):
    template_name = 'product_details.html'

class ShoppingCartPageView(TemplateView):
    template_name = 'shopping_cart.html'