from django.shortcuts import render
from django.views import View
from .models import Product
from django.db.models import Prefetch
from django.core.cache import cache

# Create your views here.

class HomePage(View):
    def get(self, request):
        if cache.get("products"):
            print(" Cache")
            products = cache.get("products")
            
        else:    
            products = Product.objects.all().prefetch_related( "tags" ).select_related("category").order_by('-id')[:25]
            print("No Cache")
            cache.set("products", products, 86400)
        # print(products)
        data = {"products": products}
        return render(request,'index.html' ,data)