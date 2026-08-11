# System Architecture

```text
Browser
   |
   v
Django URL Router
   |
   +--> Accounts ------> Authentication / Profiles
   |
   +--> Products ------> Catalogue / Wishlist / Reviews
   |
   +--> Cart ----------> Cart and stock-aware quantities
   |
   +--> Orders --------> Checkout / Transactions / Order history
   |
   +--> Dashboard -----> Staff KPIs / Operations
   |
   +--> REST API ------> Product and Order endpoints
   |
   v
Django ORM
   |
   v
SQLite (development)
```

The application uses modular Django apps so each business capability remains independently testable and maintainable.
