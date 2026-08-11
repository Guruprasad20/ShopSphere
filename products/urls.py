from django.urls import path
from .views import home, product_detail, product_list, toggle_wishlist, wishlist, add_review
urlpatterns=[
 path("",home,name="home"), path("shop/",product_list,name="product_list"),
 path("product/<slug:slug>/",product_detail,name="product_detail"),
 path("wishlist/",wishlist,name="wishlist"),
 path("wishlist/toggle/<int:product_id>/",toggle_wishlist,name="toggle_wishlist"),
 path("product/<int:product_id>/review/",add_review,name="add_review"),
]
