from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from products.models import Category, Product
from cart.models import Cart, CartItem
from .models import Order

User = get_user_model()

class OrderTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="orderuser", password="StrongPass123!")
        self.category = Category.objects.create(name="Accessories")
        self.product = Product.objects.create(
            category=self.category, name="Demo Headphones", slug="demo-headphones",
            description="Test", price="1500.00", stock=10
        )
        self.client.login(username="orderuser", password="StrongPass123!")
        cart = Cart.objects.create(user=self.user)
        CartItem.objects.create(cart=cart, product=self.product, quantity=2)

    def test_checkout_creates_order_and_reduces_stock(self):
        response = self.client.post(reverse("checkout"), {
            "shipping_name": "Demo User",
            "shipping_phone": "9999999999",
            "shipping_address": "Demo Street",
            "shipping_city": "Gadag",
            "shipping_state": "Karnataka",
            "shipping_postal_code": "582101",
            "payment_method": "Cash / Demo Payment",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.filter(user=self.user).count(), 1)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 8)
