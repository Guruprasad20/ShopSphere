from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from products.models import Product
from .models import Cart, CartItem

@login_required
def cart_detail(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related("product", "product__category")
    return render(request, "cart/detail.html", {"cart": cart, "items": items})

@login_required
def add_to_cart(request, product_id):
    if request.method != "POST":
        return redirect("product_list")
    product = get_object_or_404(Product, pk=product_id, is_active=True)
    quantity = max(1, int(request.POST.get("quantity", 1)))
    if product.stock < quantity:
        messages.error(request, "Requested quantity is not available in stock.")
        return redirect("product_detail", slug=product.slug)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    new_quantity = quantity if created else item.quantity + quantity
    if new_quantity > product.stock:
        messages.error(request, f"Only {product.stock} unit(s) are available.")
    else:
        item.quantity = new_quantity
        item.save()
        messages.success(request, f"{product.name} was added to your cart.")
    return redirect(request.POST.get("next") or "cart_detail")

@login_required
def update_cart(request, item_id):
    if request.method != "POST":
        return redirect("cart_detail")
    cart = get_object_or_404(Cart, user=request.user)
    item = get_object_or_404(CartItem, pk=item_id, cart=cart)
    quantity = int(request.POST.get("quantity", 1))
    if quantity <= 0:
        item.delete()
        messages.success(request, "Item removed from cart.")
    elif quantity <= item.product.stock:
        item.quantity = quantity
        item.save()
        messages.success(request, "Cart updated.")
    else:
        messages.error(request, f"Only {item.product.stock} unit(s) are available.")
    return redirect("cart_detail")

@login_required
def remove_from_cart(request, item_id):
    if request.method == "POST":
        cart = get_object_or_404(Cart, user=request.user)
        item = get_object_or_404(CartItem, pk=item_id, cart=cart)
        item.delete()
        messages.success(request, "Item removed from cart.")
    return redirect("cart_detail")
