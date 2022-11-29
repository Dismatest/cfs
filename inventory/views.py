from django.shortcuts import get_object_or_404, render, redirect
from .models import Inventory, Sale
from django.contrib.auth.decorators import login_required
from .forms import AddProductForm, UserRegisterForm, UpdateProductForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username} successfully!')
            return redirect("/inventory/")
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'inventory/register.html', context)


@login_required
def inventory_list(request):
    inventory = Inventory.objects.all()
    context = {
        'inventory': inventory
    }
    return render(request, "inventory/index.html", context=context)


@login_required
def single_product(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'inventory': inventory
    }
    return render(request, "inventory/single-product.html", context=context)


@login_required
def add_product(request):
    if request.method == "POST":
        add_form = AddProductForm(data=request.POST)
        if add_form.is_valid():
            new_product = add_form.save(commit=False)
            new_product.sales = float(add_form.data['cost_per_item']) * float(add_form.data['quantity_sold'])
            messages.success(request, f'Product has been added successfully!')
            new_product.save()
            return redirect("/inventory/")
    else:
        add_form = AddProductForm()
    context = {
        'add_form': add_form
    }
    return render(request, "inventory/add-product.html", context=context)


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Inventory, pk=pk)
    product.delete()
    messages.success(request, f'The product has been deleted successfully!')
    return redirect("/inventory/")

@login_required
def update_product(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        updateForm = UpdateProductForm(data=request.POST)
        product_id = Inventory.objects.get(id=inventory.id)
        if updateForm.is_valid():
            inventory.quantity_in_stock = int(updateForm.data['quantity_in_stock']) - int(updateForm.data['quantity_sold'])
            inventory.quantity_sold = updateForm.data['quantity_sold']
            inventory.sales = float(inventory.quantity_sold) * float(inventory.cost_per_item)
            inventory.cost_per_item = updateForm.data['cost_per_item']
            point_received = inventory.quantity_sold
            discount = float(point_received) * 0.5
            total = inventory.sales - discount
            sale = Sale.objects.create(point_received=point_received,discount=discount, total_sale=total, name=product_id)
            sale.save()
            if inventory.quantity_in_stock <= 0:
                updateForm.save(commit=False)
                messages.warning(request, f'Kindly add more stock before you can sell, Your stock is less')
            else:
                 inventory.save()
            return redirect("/inventory/dashboard")
    else:
        updateForm = UpdateProductForm(instance=inventory)
    context = {
        'form': updateForm
    }
    return render(request, 'inventory/update-product.html', context=context)


@login_required
def discount(request):
    discount = Sale.objects.all()
    context = {
        'discount': discount
    }
    return render(request, 'inventory/discount.html', context=context)


