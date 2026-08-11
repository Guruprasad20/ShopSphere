from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()

class AccountTests(TestCase):
    def test_registration_page(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_registration_creates_user(self):
        response = self.client.post(reverse("register"), {
            "first_name": "Demo",
            "last_name": "User",
            "username": "demouser",
            "email": "demo@example.com",
            "password1": "StrongPass123!",
            "password2": "StrongPass123!",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="demouser").exists())
