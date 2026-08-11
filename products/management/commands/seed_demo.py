from decimal import Decimal
from pathlib import Path
from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from products.models import Category, Product

DATA = {
    "Electronics": [("NovaBook Pro 14", "Performance laptop for work, study and development.", "64999", 18, "4.80"), ("Pulse Wireless Headphones", "Comfortable wireless headphones with rich sound.", "3499", 35, "4.60"), ("Orbit Mechanical Keyboard", "Compact mechanical keyboard for productive workflows.", "2899", 24, "4.70")],
    "Grocery": [("Premium Coffee Beans", "Fresh roasted coffee beans for your daily brew.", "699", 60, "4.50"), ("Organic Green Tea", "A refreshing green tea pack.", "299", 80, "4.40"), ("Almonds 500g", "Premium quality almonds.", "499", 45, "4.60")],
    "Fashion": [("Classic Casual Shirt", "Versatile cotton casual shirt.", "1199", 30, "4.30"), ("Urban Sneakers", "Comfortable everyday sneakers.", "2499", 22, "4.55"), ("Everyday Backpack", "Durable backpack for college and work.", "1599", 27, "4.45")],
}

class Command(BaseCommand):
    help = "Create/update demo catalog and guaranteed local product images."
    def handle(self, *args, **options):
        media_dir = Path(__file__).resolve().parents[4] / "media" / "products"
        media_dir.mkdir(parents=True, exist_ok=True)
        for category_name, products in DATA.items():
            category, _ = Category.objects.get_or_create(name=category_name, defaults={"description": f"{category_name} products"})
            for name, description, price, stock, rating in products:
                product, _ = Product.objects.update_or_create(slug=slugify(name), defaults={"category": category, "name": name, "description": description, "price": Decimal(price), "stock": stock, "rating": Decimal(rating), "is_active": True})
                filename = f"{slugify(name)}.png"
                target = media_dir / filename
                if not target.exists():
                    from PIL import Image, ImageDraw
                    img = Image.new("RGB", (900, 650), "#eef2f7")
                    draw = ImageDraw.Draw(img)
                    draw.rounded_rectangle((90, 80, 810, 570), radius=36, fill="white", outline="#d5dbe5", width=5)
                    draw.text((150, 285), name[:28], fill="#172033")
                    draw.text((150, 330), f"₹{price}", fill="#334155")
                    img.save(target, "PNG")
                with target.open("rb") as fh:
                    product.image.save(filename, File(fh), save=True)
        self.stdout.write(self.style.SUCCESS("Demo catalog, images, and ratings created successfully."))
