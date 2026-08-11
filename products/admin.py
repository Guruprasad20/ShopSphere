from django.contrib import admin
from .models import Category, Product, Wishlist, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("name","product_count","created_at")
    search_fields=("name",)
    def product_count(self,obj): return obj.products.count()

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("name","category","price","stock","rating","is_active","created_at")
    list_filter=("category","is_active")
    search_fields=("name","description")
    prepopulated_fields={"slug":("name",)}
    list_editable=("price","stock","is_active")
    readonly_fields=("rating","created_at","updated_at")

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display=("user","product","created_at")
    search_fields=("user__username","product__name")

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=("product","user","rating","created_at")
    list_filter=("rating",)
    search_fields=("product__name","user__username","comment")
