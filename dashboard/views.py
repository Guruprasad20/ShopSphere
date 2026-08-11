from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum, Count
from django.shortcuts import render
from orders.models import Order
from products.models import Product, Category, Review
from accounts.models import Profile

@staff_member_required
def dashboard(request):
    orders=Order.objects.all()
    revenue=orders.exclude(status=Order.Status.CANCELLED).aggregate(v=Sum("total_amount"))["v"] or 0
    context={
      "revenue":revenue,"orders_count":orders.count(),"users_count":Profile.objects.count(),
      "products_count":Product.objects.count(),"low_stock":Product.objects.filter(stock__lte=5,is_active=True).order_by("stock")[:8],
      "recent_orders":orders.select_related("user")[:8],"top_categories":Category.objects.annotate(sales=Count("products__order_items")).order_by("-sales")[:6],
      "reviews_count":Review.objects.count(),
    }
    return render(request,"dashboard/index.html",context)

@staff_member_required
def api_docs(request):
    return render(request,"dashboard/api_docs.html")
