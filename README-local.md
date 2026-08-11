# ShopSphere — Professional Full-Stack E-Commerce Platform

ShopSphere is a portfolio-grade Django e-commerce application designed for internship evaluation, GitHub presentation and technical demonstrations.

## What is included

### Customer experience
- Responsive premium storefront
- Product catalogue with search, category filtering, sorting and pagination
- Product detail pages
- Stock-aware cart
- Checkout and order history
- Profile management
- Wishlist / saved products
- Product ratings and reviews
- Flash messages and responsive mobile navigation

### Business / admin
- Django Admin with branded administration
- Custom operations dashboard at `/dashboard/`
- Revenue and order KPIs
- Low-stock monitoring
- Recent-order monitoring
- Category and product management
- Customer and review management

### REST API
- `GET /api/products/`
- `GET /api/products/{id}/`
- `GET /api/orders/my/` (authenticated)
- Developer API documentation at `/dashboard/api-docs/`

### Engineering quality
- Django ORM with indexed fields
- Transactional checkout
- Server-side stock validation
- CSRF protection
- Password validation
- Environment-based configuration
- Secure cookie/content-type/referrer settings
- Automated tests
- Clean app separation
- GitHub-ready `.gitignore`

## Tech stack

Python · Django · Django REST Framework · SQLite · HTML5 · CSS3 · JavaScript · Pillow

## Quick start

```bash
py -m venv venv
# Windows PowerShell
.env\Scripts\Activate.ps1

pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py test
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

Admin: `http://127.0.0.1:8000/admin/`

Operations dashboard: `http://127.0.0.1:8000/dashboard/`

## Demo flow

1. Create a customer account.
2. Browse and filter products.
3. Save products to Wishlist.
4. Add an in-stock product to Cart.
5. Update quantity.
6. Complete Checkout.
7. View the generated Order.
8. Leave a Review.
9. Sign in as staff and demonstrate Dashboard/Admin.

## Production notes

The included `.env.example` is safe for source control. Never commit real secrets, payment credentials or production database credentials.

A real payment gateway is intentionally not hard-coded. It can be integrated later using environment variables and the provider's official SDK.

## Internship submission

See `SUBMISSION_CHECKLIST.md` for the recommended evidence, screenshots and final packaging sequence.
