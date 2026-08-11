from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ReviewForm
from .models import Category, Product, Review, Wishlist

def home(request):
    featured=Product.objects.filter(is_active=True).select_related("category")[:8]
    categories=Category.objects.annotate(product_count=Count("products", filter=Q(products__is_active=True)))[:8]
    return render(request,"home.html",{"featured_products":featured,"categories":categories})

def product_list(request):
    products=Product.objects.filter(is_active=True).select_related("category")
    query=request.GET.get("q","").strip()
    category=request.GET.get("category","").strip()
    sort=request.GET.get("sort","-created_at")
    allowed={"-created_at","price","-price","name","-rating"}
    if query: products=products.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(category__name__icontains=query))
    if category: products=products.filter(category__id=category)
    if sort in allowed: products=products.order_by(sort)
    from django.core.paginator import Paginator
    page=Paginator(products,12).get_page(request.GET.get("page"))
    return render(request,"products/list.html",{"products":page,"page_obj":page,"categories":Category.objects.all(),"query":query,"selected_category":category,"sort":sort})

def product_detail(request,slug):
    product=get_object_or_404(Product.objects.select_related("category"),slug=slug,is_active=True)
    related=Product.objects.filter(category=product.category,is_active=True).exclude(pk=product.pk)[:4]
    reviews=product.reviews.select_related("user")
    review_form=ReviewForm()
    in_wishlist=request.user.is_authenticated and Wishlist.objects.filter(user=request.user,product=product).exists()
    can_review=False
    existing_review=None
    if request.user.is_authenticated:
        from orders.models import Order
        can_review=Order.objects.filter(user=request.user,status=Order.Status.DELIVERED,items__product=product).exists()
        existing_review=reviews.filter(user=request.user).first()
    return render(request,"products/detail.html",{"product":product,"related_products":related,"reviews":reviews,"review_form":review_form,"in_wishlist":in_wishlist,"can_review":can_review,"existing_review":existing_review})

@login_required
def toggle_wishlist(request, product_id):
    if request.method!="POST": return redirect("product_list")
    product=get_object_or_404(Product,pk=product_id,is_active=True)
    item,created=Wishlist.objects.get_or_create(user=request.user,product=product)
    if not created: item.delete(); messages.info(request,"Removed from wishlist.")
    else: messages.success(request,"Added to wishlist.")
    return redirect(request.POST.get("next") or "product_detail", slug=product.slug) if not request.POST.get("next") else redirect(request.POST.get("next"))

@login_required
def wishlist(request):
    items=Wishlist.objects.filter(user=request.user).select_related("product","product__category")
    return render(request,"products/wishlist.html",{"items":items})

@login_required
def add_review(request, product_id):
    product=get_object_or_404(Product,pk=product_id,is_active=True)
    from orders.models import Order
    eligible = Order.objects.filter(
        user=request.user, status=Order.Status.DELIVERED, items__product=product
    ).exists()
    if not eligible:
        messages.warning(request, "You can review this product after an order containing it is delivered.")
        return redirect("product_detail", slug=product.slug)
    if request.method!="POST": return redirect("product_detail",slug=product.slug)
    form=ReviewForm(request.POST)
    if form.is_valid():
        review,created=Review.objects.update_or_create(user=request.user,product=product,defaults=form.cleaned_data)
        avg=Review.objects.filter(product=product).aggregate(v=Avg("rating"))["v"] or 0
        product.rating=round(avg,2); product.save(update_fields=["rating","updated_at"])
        messages.success(request,"Your review was published." if created else "Your review was updated.")
    else: messages.error(request,"Please check the review details.")
    return redirect("product_detail",slug=product.slug)
