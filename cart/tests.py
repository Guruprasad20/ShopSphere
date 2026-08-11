from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from products.models import Category, Product
from .models import Cart

User = get_user_model()

class CartTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="cartuser", password="StrongPass123!")
        self.category = Category.objects.create(name="Books")
        self.product = Product.objects.create(
            category=self.category, name="Demo Book", slug="demo-book",
            description="Test", price="500.00", stock=5
        )
        self.client.login(username="cartuser", password="StrongPass123!")

    def test_add_to_cart(self):
        response = self.client.post(reverse("add_to_cart", args=[self.product.id]), {"quantity": 2})
        self.assertEqual(response.status_code, 302)
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.total_items, 2)
