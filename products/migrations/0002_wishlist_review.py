from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies=[("products","0001_initial"),("auth","0012_alter_user_first_name_max_length")]
    operations=[
      migrations.CreateModel(name="Wishlist",fields=[
        ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
        ("created_at",models.DateTimeField(auto_now_add=True)),
        ("product",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="wishlisted_by",to="products.product")),
        ("user",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="wishlist_items",to="auth.user")),
      ]),
      migrations.CreateModel(name="Review",fields=[
        ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
        ("rating",models.PositiveSmallIntegerField()),
        ("title",models.CharField(blank=True,max_length=120)),
        ("comment",models.TextField(max_length=1000)),
        ("created_at",models.DateTimeField(auto_now_add=True)),
        ("updated_at",models.DateTimeField(auto_now=True)),
        ("product",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="reviews",to="products.product")),
        ("user",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="product_reviews",to="auth.user")),
      ]),
      migrations.AddConstraint(model_name="wishlist",constraint=models.UniqueConstraint(fields=("user","product"),name="unique_wishlist_item")),
      migrations.AddConstraint(model_name="review",constraint=models.UniqueConstraint(fields=("user","product"),name="unique_product_review")),
      migrations.AddConstraint(model_name="review",constraint=models.CheckConstraint(condition=models.Q(("rating__gte",1),("rating__lte",5)),name="review_rating_1_to_5")),
    ]
