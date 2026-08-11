from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0001_initial"),
    ]
    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=12)),
                ("status", models.CharField(choices=[("PENDING", "Pending"), ("CONFIRMED", "Confirmed"), ("PROCESSING", "Processing"), ("SHIPPED", "Shipped"), ("DELIVERED", "Delivered"), ("CANCELLED", "Cancelled")], default="PENDING", max_length=20)),
                ("shipping_name", models.CharField(max_length=150)),
                ("shipping_phone", models.CharField(max_length=20)),
                ("shipping_address", models.TextField()),
                ("shipping_city", models.CharField(max_length=100)),
                ("shipping_state", models.CharField(max_length=100)),
                ("shipping_postal_code", models.CharField(max_length=20)),
                ("payment_method", models.CharField(default="Cash / Demo Payment", max_length=30)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="orders", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "ordering": ["-created_at"],
                "indexes": [
                    models.Index(fields=["user"], name="orders_ord_user_id_6e4c0e_idx"),
                    models.Index(fields=["status"], name="orders_ord_status_7d8d9a_idx"),
                    models.Index(fields=["-created_at"], name="orders_ord_created_9c0e8f_idx"),
                ],
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.PositiveIntegerField()),
                ("order", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="items", to="orders.order")),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="order_items", to="products.product")),
            ],
        ),
    ]
