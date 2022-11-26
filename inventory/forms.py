from django.forms import ModelForm
from .models import Inventory
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddProductForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['product_name', 'cost_per_item', 'quantity_in_stock', 'quantity_sold']


class UpdateProductForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['cost_per_item', 'quantity_in_stock', 'quantity_sold']
