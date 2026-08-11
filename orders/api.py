from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ("id", "product", "product_name", "price", "quantity", "subtotal")

    def get_subtotal(self, obj):
        return obj.subtotal

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ("id", "total_amount", "status", "shipping_name", "shipping_city", "shipping_state", "payment_method", "created_at", "items")

class MyOrderListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = request.user.orders.prefetch_related("items__product")
        return Response(OrderSerializer(orders, many=True).data)
