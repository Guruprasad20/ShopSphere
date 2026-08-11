import os
import urllib.request

# Directory structure setup
output_dir = os.path.join("ShopSphere", "media", "products")
os.makedirs(output_dir, exist_ok=True)

# Image mapping (Direct high-quality stock URLs)
products = {
    "classic-casual-shirt.png": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=800&q=80",
    "urban-sneakers.png": "https://images.unsplash.com/photo-1552346154-21d32810aba3?w=800&q=80",
    "everyday-backpack.png": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=800&q=80",
    "wireless-headphones.png": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&q=80",
    "smart-watch.png": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&q=80",
    "organic-coffee.png": "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=800&q=80",
    "cotton-hoodie.png": "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?w=800&q=80",
    "denim-jeans.png": "https://images.unsplash.com/photo-1542272604-780c36856d61?w=800&q=80",
    "ceramic-mug.png": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=800&q=80"
}

headers = {'User-Agent': 'Mozilla/5.0'}

for filename, url in products.items():
    filepath = os.path.join(output_dir, filename)
    print(f"Downloading {filename}...")
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
        out_file.write(response.read())

print("All product images downloaded successfully!")
