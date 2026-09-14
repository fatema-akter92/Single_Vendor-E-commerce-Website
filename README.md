# TechMart - Single Vendor E-Commerce Website

A responsive single-vendor e-commerce web application built using **Django**, **HTML5**, **CSS3**, **JavaScript**, **Bootstrap 5**, and **SQLite**.

---

## 🚀 Features

### Core Required Features
1. **Home Page )**:
   - Shop Name & Brand Logo 
   - Navigation Bar with dynamic Cart Item Counter.
   - Interactive Bootstrap Banner / Carousel showcasing featured items.
   - Category grid & Featured Products preview.
   - Responsive Footer.
2. **Products Page **:
   - Full product listing loaded dynamically from SQLite database.
   - Product Card displaying Image, Name, Price, Discount price, Short description, "View Details", and "Add to Cart" buttons.
   - **Category Filtering & Real-time Product Search**.
3. **Product Details Page **:
   - High-res Product Image, Name, Price, Rating, and Detailed description.
   - Stock availability status indicator.
   - Interactive Quantity selector.
   - "Add to Cart" form.
   - Related products section.
4. **Shopping Cart **:
   - Interactive session-based shopping cart.
   - Live item quantity update .
   - Remove product option.
   - Instant Subtotal and Total Price calculations.
5. **Checkout Page **:
   - Checkout Form collecting **Customer Name**, **Phone Number**, and **Delivery Address** (with client-side & server-side validation).
   - Order Summary breakdown.
   - Saves `Customer` and `Order` entries in the Django database upon order placement.
6. **Order Success Page **:
   - Confirmation notification: **"Order Placed Successfully!"**.
   - Complete breakdown of customer information, ordered products, quantities, total price, and order status.
7. **Django Admin Panel **:
   - Full admin interface for managing `Product`, `Category`, `Customer`, and `Order` models.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.12, Django 5.1.4
- **Frontend**: HTML5, CSS3, JavaScript (ES6), Bootstrap 5.3, Bootstrap Icons
- **Database**: SQLite3
- **Image Handling**: Pillow 12.3, Inline Vector SVGs

---


Open your browser and visit: https://light-moments-share.loca.lt/

---



## License & Acknowledgements

Created as part of the Single Vendor E-commerce Django Assignment.
