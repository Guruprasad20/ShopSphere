from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Category, Product, Wishlist, Review
User=get_user_model()

class ProductTests(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username="tester",password="StrongPass123!")
        self.category=Category.objects.create(name="Electronics")
        self.product=Product.objects.create(category=self.category,name="Demo Laptop",slug="demo-laptop",description="A demo product.",price="50000.00",stock=10)
    def test_catalog_page(self):
        response=self.client.get(reverse("product_list")); self.assertEqual(response.status_code,200); self.assertContains(response,"Demo Laptop")
    def test_product_detail(self):
        response=self.client.get(reverse("product_detail",args=[self.product.slug])); self.assertEqual(response.status_code,200)
    def test_wishlist_toggle(self):
        self.client.login(username="tester",password="StrongPass123!")
        self.client.post(reverse("toggle_wishlist",args=[self.product.id]),{"next":"/shop/"})
        self.assertTrue(Wishlist.objects.filter(user=self.user,product=self.product).exists())
    def test_review_updates_rating(self):
        self.client.login(username="tester",password="StrongPass123!")
        self.client.post(reverse("add_review",args=[self.product.id]),{"rating":5,"title":"Excellent","comment":"Very good demo product."})
        self.product.refresh_from_db()
        self.assertEqual(float(self.product.rating),5.0)
        self.assertEqual(Review.objects.count(),1)
