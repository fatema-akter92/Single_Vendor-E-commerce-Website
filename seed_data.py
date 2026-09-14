import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'single_vendor_ecommerce.settings')
django.setup()

from store.models import Category, Product

def seed_database():
    print("Seeding database categories and products...")

    # Define Categories
    categories_data = [
        {'name': 'Laptops & Computing', 'slug': 'laptops', 'icon': 'bi-laptop'},
        {'name': 'Smartphones & Tablets', 'slug': 'smartphones', 'icon': 'bi-phone'},
        {'name': 'Audio & Headphones', 'slug': 'audio', 'icon': 'bi-headphones'},
        {'name': 'Accessories & Gear', 'slug': 'accessories', 'icon': 'bi-mouse'},
    ]

    categories = {}
    for cat_info in categories_data:
        cat, created = Category.objects.get_or_create(
            slug=cat_info['slug'],
            defaults={'name': cat_info['name'], 'icon': cat_info['icon']}
        )
        categories[cat_info['slug']] = cat
        print(f"Category: {cat.name} ({'Created' if created else 'Already exists'})")

    # Helper SVG graphics
    svg_laptop = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='300' viewBox='0 0 400 300' fill='%23f8fafc'><rect width='400' height='300' fill='%23e2e8f0'/><rect x='80' y='60' width='240' height='140' rx='8' fill='%231e293b'/><rect x='90' y='70' width='220' height='120' rx='4' fill='%233b82f6'/><path d='M 50 210 L 350 210 L 330 230 L 70 230 Z' fill='%2394a3b8'/><text x='200' y='140' font-family='sans-serif' font-size='20' font-weight='bold' fill='white' text-anchor='middle'>Pro Laptop</text></svg>"
    
    svg_phone = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='300' viewBox='0 0 400 300' fill='%23f8fafc'><rect width='400' height='300' fill='%23f1f5f9'/><rect x='140' y='30' width='120' height='240' rx='20' fill='%230f172a'/><rect x='148' y='42' width='104' height='216' rx='14' fill='%2310b981'/><text x='200' y='155' font-family='sans-serif' font-size='18' font-weight='bold' fill='white' text-anchor='middle'>Smartphone</text></svg>"
    
    svg_headphones = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='300' viewBox='0 0 400 300' fill='%23f8fafc'><rect width='400' height='300' fill='%23f8fafc'/><circle cx='200' cy='150' r='90' stroke='%238b5cf6' stroke-width='16' fill='none'/><rect x='110' y='130' width='30' height='60' rx='15' fill='%236d28d9'/><rect x='260' y='130' width='30' height='60' rx='15' fill='%236d28d9'/><text x='200' y='155' font-family='sans-serif' font-size='18' font-weight='bold' fill='%236d28d9' text-anchor='middle'>Pro Audio</text></svg>"
    
    svg_mouse = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='300' viewBox='0 0 400 300' fill='%23f8fafc'><rect width='400' height='300' fill='%23f1f5f9'/><ellipse cx='200' cy='150' rx='60' ry='90' fill='%23f59e0b'/><line x1='200' y1='60' x2='200' y2='130' stroke='%2378350f' stroke-width='4'/><text x='200' y='180' font-family='sans-serif' font-size='18' font-weight='bold' fill='white' text-anchor='middle'>Accessory</text></svg>"

    products_data = [
        {
            'name': 'MacBook Pro 16 M3 Max',
            'price': 2499.00,
            'discount_price': 2299.00,
            'description': 'Apple M3 Max chip with 16-core CPU, 40-core GPU, 36GB Unified Memory, 1TB SSD Storage. Liquid Retina XDR display.',
            'quantity': 15,
            'category': categories['laptops'],
            'rating': 4.9,
            'image_url': svg_laptop,
        },
        {
            'name': 'Dell XPS 15 OLED Touch Laptop',
            'price': 1899.00,
            'discount_price': 1749.00,
            'description': '13th Gen Intel Core i9, NVIDIA GeForce RTX 4070, 32GB DDR5 RAM, 1TB NVMe SSD, 3.5K OLED InfinityEdge touch screen.',
            'quantity': 8,
            'category': categories['laptops'],
            'rating': 4.7,
            'image_url': svg_laptop,
        },
        {
            'name': 'iPhone 15 Pro Max 256GB',
            'price': 1199.00,
            'discount_price': 1099.00,
            'description': 'Forged in titanium, featuring the groundbreaking A17 Pro chip, customizable Action button, and 5x Telephoto camera.',
            'quantity': 20,
            'category': categories['smartphones'],
            'rating': 4.9,
            'image_url': svg_phone,
        },
        {
            'name': 'Samsung Galaxy S24 Ultra 512GB',
            'price': 1299.00,
            'discount_price': None,
            'description': 'Galaxy AI embedded, Snapdragon 8 Gen 3 for Galaxy, 200MP Quad Telephoto Camera, Built-in S Pen, Titanium Armor frame.',
            'quantity': 12,
            'category': categories['smartphones'],
            'rating': 4.8,
            'image_url': svg_phone,
        },
        {
            'name': 'Sony WH-1000XM5 Wireless Headphones',
            'price': 399.00,
            'discount_price': 349.00,
            'description': 'Industry-leading noise canceling with 8 microphones and Auto NC Optimizer. Up to 30-hour battery life with quick charging.',
            'quantity': 25,
            'category': categories['audio'],
            'rating': 4.9,
            'image_url': svg_headphones,
        },
        {
            'name': 'Apple AirPods Pro (2nd Gen)',
            'price': 249.00,
            'discount_price': 199.00,
            'description': 'H2 chip power, 2x more active noise cancellation, Adaptive Audio, Personalized Spatial Audio with MagSafe Charging Case.',
            'quantity': 30,
            'category': categories['audio'],
            'rating': 4.8,
            'image_url': svg_headphones,
        },
        {
            'name': 'Logitech MX Master 3S Wireless Mouse',
            'price': 99.00,
            'discount_price': None,
            'description': 'An iconic ergonomic mouse remastered with 8K DPI track-on-glass sensor and Quiet Clicks technology.',
            'quantity': 40,
            'category': categories['accessories'],
            'rating': 4.9,
            'image_url': svg_mouse,
        },
        {
            'name': 'Anker 737 Power Bank 24,000mAh',
            'price': 149.00,
            'discount_price': 119.00,
            'description': '140W ultra-powerful 3-port portable charger with smart digital display for high-speed charging of laptops and phones.',
            'quantity': 18,
            'category': categories['accessories'],
            'rating': 4.7,
            'image_url': svg_mouse,
        },
    ]

    for p_info in products_data:
        p, created = Product.objects.get_or_create(
            name=p_info['name'],
            defaults={
                'price': p_info['price'],
                'discount_price': p_info['discount_price'],
                'description': p_info['description'],
                'quantity': p_info['quantity'],
                'category': p_info['category'],
                'rating': p_info['rating'],
                'image_url': p_info['image_url'],
            }
        )
        print(f"Product: {p.name} (${p.price}) - {'Created' if created else 'Already exists'}")

    print("Database seeding completed successfully!")

if __name__ == '__main__':
    seed_database()
