from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from .models import Product, Category, Customer, Order
from .cart import Cart
from .forms import CheckoutForm

def home(request):
    categories = Category.objects.all()
    featured_products = Product.objects.all().order_by('-created_at')[:6]
    discounted_products = Product.objects.filter(discount_price__isnull=False)[:4]
    return render(request, 'home.html', {
        'categories': categories,
        'featured_products': featured_products,
        'discounted_products': discounted_products,
    })

def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    
    selected_category_slug = request.GET.get('category')
    search_query = request.GET.get('q', '').strip()

    if selected_category_slug:
        products = products.filter(category__slug=selected_category_slug)
    
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    return render(request, 'products.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category_slug,
        'search_query': search_query,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'product_detail.html', {
        'product': product,
        'related_products': related_products,
    })

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {
        'cart': cart,
    })

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    try:
        quantity = int(request.POST.get('quantity', 1))
    except ValueError:
        quantity = 1

    if quantity > product.quantity:
        messages.warning(request, f"Only {product.quantity} units available in stock.")
        quantity = product.quantity

    if quantity > 0:
        cart.add(product=product, quantity=quantity)
        messages.success(request, f"Added {product.name} to your cart!")

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'cart_count': len(cart), 'message': f"Added {product.name} to cart!"})

    return redirect('cart_detail')

def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    action = request.POST.get('action')
    try:
        quantity = int(request.POST.get('quantity', 1))
    except ValueError:
        quantity = 1

    current_item = cart.cart.get(str(product.id), {})
    current_qty = current_item.get('quantity', 0)

    if action == 'increase':
        new_qty = current_qty + 1
    elif action == 'decrease':
        new_qty = current_qty - 1
    else:
        new_qty = quantity

    if new_qty > product.quantity:
        messages.warning(request, f"Stock limit reached. Max available: {product.quantity}")
        new_qty = product.quantity

    if new_qty <= 0:
        cart.remove(product)
        messages.info(request, f"Removed {product.name} from cart.")
    else:
        cart.add(product=product, quantity=new_qty, override_quantity=True)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'cart_count': len(cart),
            'total_price': float(cart.get_total_price()),
        })

    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.info(request, f"Removed {product.name} from cart.")
    return redirect('cart_detail')

def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, "Your shopping cart is empty. Add products before checking out!")
        return redirect('product_list')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            customer = form.save()
            orders_created = []

            for item in cart:
                product = item['product']
                qty = item['quantity']
                line_total = item['total_price']

                # Create Order entry in database
                order = Order.objects.create(
                    customer=customer,
                    product=product,
                    quantity=qty,
                    total_price=line_total,
                    status='Pending'
                )
                orders_created.append(order.id)

                # Deduct purchased quantity from Product stock
                if product.quantity >= qty:
                    product.quantity -= qty
                else:
                    product.quantity = 0
                product.save()

            # Store order ID in session & clear cart
            request.session['last_order_customer_id'] = customer.id
            cart.clear()

            first_order_id = orders_created[0] if orders_created else customer.id
            messages.success(request, "Order Placed Successfully!")
            return redirect('order_success', order_id=first_order_id)
    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {
        'form': form,
        'cart': cart,
    })

def order_success(request, order_id):
    customer_id = request.session.get('last_order_customer_id')
    if customer_id:
        customer = get_object_or_404(Customer, id=customer_id)
        orders = Order.objects.filter(customer=customer).order_by('-order_date')
    else:
        order = get_object_or_404(Order, id=order_id)
        customer = order.customer
        orders = Order.objects.filter(customer=customer)

    grand_total = sum(order.total_price for order in orders)

    return render(request, 'order_success.html', {
        'customer': customer,
        'orders': orders,
        'grand_total': grand_total,
        'primary_order_id': order_id,
    })
