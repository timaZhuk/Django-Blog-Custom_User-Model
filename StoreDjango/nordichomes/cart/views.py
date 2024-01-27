from django.shortcuts import render
from .cart import Cart

#----- method_add to cart -----------
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id) #add product with id to cart

    return render(request, 'cart/menu_cart.html')

#--------Cart view---function----created-----
def cart(request):
    return render(request,'cart/cart.html')

#--------Cart view---function----created-----
def checkout(request):
    return render(request,'cart/checkout.html')

