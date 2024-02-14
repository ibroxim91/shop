from django.urls import path
from .views import CartAdd


urlpatterns = [
    path("add/<int:product_id>" , CartAdd.as_view() , name="add")
]