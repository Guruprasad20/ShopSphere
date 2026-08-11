from django.urls import path
from .views import checkout, order_detail, order_list

urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("orders/", order_list, name="order_list"),
    path("orders/<int:order_id>/", order_detail, name="order_detail"),
]
