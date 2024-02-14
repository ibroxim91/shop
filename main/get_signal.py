from django.dispatch import receiver
from django.db.models import signals 
from .models import Product
from django.core.cache import cache


@receiver(signal=signals.post_save, sender=Product)
def update_cache(instance,**kwargs):
    products = Product.objects.all().prefetch_related( "tags" ).select_related("category").order_by('-id')[:25]
    cache.set("products", products, 86400)
    print()
    print(" Add cache ")
    print()
    # product_id = instance.id
    # print()
    # print(" Signal connect ")
    # print(product_id)
    # print()
    # if product_id:
    #     product = Product.objects.get(id=product_id)
    #     if instance.price < product.price:
    #         print("Narxi pasladi ")
    #         pass
