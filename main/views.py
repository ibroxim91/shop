from django.shortcuts import render
from django.views import View
from .models import Product

# Create your views here.

class HomePage(View):
    def get(self, request):
        products = Product.objects.all().order_by('-id')[:25]
        # print(products)
        data = {"products": products}
        return render(request,'index.html' ,data)