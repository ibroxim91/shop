from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .cart import Cart
from django.contrib.messages import add_message
from django.contrib import messages
# Create your views here.


class CartAdd(View):
    def get(self, request,product_id):
        cart = Cart(request)
        res = cart.add( product_id )
        if res == True:
            return JsonResponse({"status": "success","detail":"Product  added to cart successfully"})
        else:    
            return JsonResponse({"status": "error","detail":"Product not  added to cart"})




