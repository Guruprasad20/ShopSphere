from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from cart.models import Cart
from .forms import CheckoutForm
from .models import Order, OrderItem

@login_required
def checkout(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = list(cart.items.select_related("product"))
    if not items:
        messages.info(request, "Your cart is empty.")
        return redirect("product_list")
    for item in items:
        if item.quantity > item.product.stock:
            messages.error(request, f"{item.product.name} no longer has enough stock.")
            return redirect("cart_detail")
    total = sum(item.subtotal for item in items)
    form = CheckoutForm(request.POST or None, instance=Order(user=request.user, total_amount=total))
    if request.method == "POST" and form.is_valid():
        with transaction.atomic():
            order = form.save(commit=False)
            order.user = request.user
            order.total_amount = total
            order.save()
            for item in items:
                product = item.product
                product.stock -= item.quantity
                product.save(update_fields=["stock", "updated_at"])
                OrderItem.objects.create(
                    order=order, product=product,
                    price=product.price, quantity=item.quantity
                )
            cart.items.all().delete()
        messages.success(request, f"Order #{order.id} has been placed successfully.")
        return redirect("order_detail", order_id=order.id)
    return render(request, "orders/checkout.html", {"form": form, "cart": cart, "items": items, "total": total})

@login_required
def order_list(request):
    orders = request.user.orders.prefetch_related("items__product")
    return render(request, "orders/list.html", {"orders": orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(
        Order.objects.prefetch_related("items__product"),
        pk=order_id,
        user=request.user
    )
    return render(request, "orders/detail.html", {"order": order})
