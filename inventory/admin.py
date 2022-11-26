from django.contrib import admin
from .models import Inventory
from .models import Sale

admin.site.register(Inventory)
admin.site.register(Sale)