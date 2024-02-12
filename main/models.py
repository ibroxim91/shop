from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(verbose_name="Nomi",max_length=100)
  

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Teg"
        verbose_name_plural = "Teglar"

class Category(models.Model):
    name = models.CharField(verbose_name="Nomi",max_length=100)
    slug = models.SlugField("Slug",  max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Katalog"
        verbose_name_plural = "Kataloglar"

class Product(models.Model):
    name = models.CharField(verbose_name="Nomi",max_length=100)
    slug = models.SlugField("Slug",  max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Tasnifi")
    price = models.DecimalField(verbose_name="Narxi",max_digits=10,decimal_places=2)
    old_price = models.DecimalField(verbose_name="Eski Narxi",blank=True,  max_digits=10,decimal_places=2)
    image = models.ImageField(verbose_name="Rasm",upload_to="products")
    tags = models.ManyToManyField(Tag, verbose_name="Teglar", null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Tovar"
        verbose_name_plural = "Tovarlar"

class Cart_detail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveBigIntegerField()
    summa = models.PositiveIntegerField()

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    total_qty = models.PositiveBigIntegerField()
    total_summa = models.PositiveIntegerField()
    products = models.ManyToManyField(Cart_detail)
    created_at = models.DateTimeField(auto_now_add=True)

class Order_detail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveBigIntegerField()
    summa = models.PositiveIntegerField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=255)
    total_qty = models.PositiveBigIntegerField()
    total_summa = models.PositiveIntegerField()
    products = models.ManyToManyField(Order_detail)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)




    