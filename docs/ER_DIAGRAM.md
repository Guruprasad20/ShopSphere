# Entity Relationship Overview

```text
User 1 ---- 1 Profile
User 1 ---- 1 Cart ---- * CartItem * ---- 1 Product
User 1 ---- * Order ---- * OrderItem * ---- 1 Product
User 1 ---- * Wishlist * ---- 1 Product
User 1 ---- * Review * ---- 1 Product
Category 1 ---- * Product
```

Checkout creates an Order and OrderItems atomically and decrements Product stock inside the same database transaction.
