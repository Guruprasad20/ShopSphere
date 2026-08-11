from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "shipping_name", "shipping_phone", "shipping_address",
            "shipping_city", "shipping_state", "shipping_postal_code",
            "payment_method"
        )
        widgets = {
            "shipping_address": forms.Textarea(attrs={"rows": 4}),
            "payment_method": forms.Select(choices=[
                ("Cash / Demo Payment", "Cash / Demo Payment"),
                ("Pay on Delivery", "Pay on Delivery"),
            ]),
        }
