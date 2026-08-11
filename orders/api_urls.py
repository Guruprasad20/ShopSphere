from django.urls import path
from .api import MyOrderListAPI

urlpatterns = [
    path("orders/", MyOrderListAPI.as_view(), name="api-orders"),
]
