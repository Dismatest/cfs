
from django.urls import path
from .views import (
    inventory_list, 
    single_product, 
    add_product, 
    register, 
    delete_product, 
    update_product, 
    discount
)

urlpatterns = [
    path("", inventory_list, name="inventory-list"),
    path("single-product/<int:pk>", single_product, name="single-product"),
    path("add-product/", add_product, name="add-product"),
    path("register/", register, name="register"),
    path("delete/<int:pk>", delete_product, name="delete-product"),
    path("update/<int:pk>", update_product, name="update-product"),
    path("dashboard", discount, name="dashboard")
]
