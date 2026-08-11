from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
admin.site.site_header = "ShopSphere Administration"
admin.site.site_title = "ShopSphere Admin"
admin.site.index_title = "Store Management Center"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path("", include("products.urls")),
    path("", include("cart.urls")),
    path("", include("orders.urls")),
    path("api/", include("products.api_urls")),
    path("api/", include("orders.api_urls")),
    path("dashboard/", include("dashboard.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

