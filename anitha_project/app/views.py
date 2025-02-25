from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Order


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        Product.objects.create(name=name, description=description, price=price)
        return redirect('product_list')
    return render(request, 'product_create.html')

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.save()
        return redirect('product_detail', pk=pk)
    return render(request, 'product_update.html', {'product': product})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_detail.html', {'order': order})

def order_create(request):
    products = Product.objects.all()
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        customer_name = request.POST.get('customer_name')
        quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, pk=product_id)
        total_price = product.price * quantity
        payment_status = request.POST.get('payment_status')
        Order.objects.create(
            product=product,
            customer_name=customer_name,
            quantity=quantity,
            total_price=total_price,
            payment_status=payment_status
        )
        return redirect('order_list')
    return render(request, 'order_create.html', {'products': products})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    products = Product.objects.all()
    if request.method == 'POST':
        order.product_id = request.POST.get('product_id')
        order.customer_name = request.POST.get('customer_name')
        order.quantity = int(request.POST.get('quantity'))
        order.total_price = order.product.price * order.quantity
        order.payment_status = request.POST.get('payment_status')
        order.save()
        return redirect('order_detail', pk=pk)
    return render(request, 'order_update.html', {'order': order, 'products': products})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order_delete.html', {'order': order})
