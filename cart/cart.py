from main.models import Cart as cr , Cart_detail, Product



class Cart(object):

    def __init__(self, request) -> None:
        if request.session.get('cart_id'):
            cart_id = request.session.get('cart_id')
            cart = cr.objects.get(id=int(cart_id))
            # cart.user = request.user
            # cart.save()
        else:
            cart = cr.objects.create(total_qty=0,total_summa=0)
            request.session['cart_id'] = cart.id
        self.cart = cart

    def add(self,product_id):
        product =Product.objects.get(id=int(product_id))
        if not self.cart.products.filter(product=product).exists():
            self.cart.products.create(product=product,qty=1, summa=product.price)
            self.cart.total_qty += 1
            self.cart.total_summa += product.price
            self.cart.save()    
            return True
        return False


# cart = Cart(request)        

