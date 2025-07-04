from django.shortcuts import render, redirect
from .models import Product, Review
from .forms import ReviewForm
CATEGORIES = ['Fruits', 'Vegetables', 'Bread', 'Meat']
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact

# --------------------
# Static Page Views
# --------------------

def cart_view(request):
    return render(request, 'cart/cart.html')

def checkout_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    subtotal = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        total = product.price * quantity
        subtotal += total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': total,
        })

    grand_total = subtotal + 3  # flat shipping

    if request.method == 'POST':
        # Here you can later save order details if needed
        request.session['cart'] = {}  # clear cart after order
        return render(request, 'checkout/thank_you.html')

    return render(request, 'checkout/checkout.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'grand_total': grand_total,
    })

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # or show thank you
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
# --------------------
# Homepage View
# --------------------

def homepage(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')  
    else:
        form = ReviewForm()

    products = Product.objects.all()[:8]  # Only top 8
    reviews = Review.objects.all().order_by('-id')

    return render(request, 'homepage/homepage.html', {
        'form': form,
        'products': products,
        'reviews': reviews,
    })

# --------------------
# Common Function to Get Products by Category
# --------------------

def get_categorized_products():
    return {
        'vegetables': Product.objects.filter(category='Vegetables'),
        'fruits': Product.objects.filter(category='Fruits'),
        'meat': Product.objects.filter(category='Meat'),
        'bread': Product.objects.filter(category='Bread'),
    }

# --------------------
# Shop View
# --------------------

def shop_view(request):
    products = Product.objects.all()
    return render(request, 'shop/shop.html', {
        'products': products,
        'categories': CATEGORIES,
        'selected_category': None,
    })

# --------------------
# More Products View
# --------------------

def more_products_view(request):
    context = get_categorized_products()
    return render(request, 'more_products/moreproducts.html', context)

def products_by_category(request, category_name):
    if category_name in CATEGORIES:
        products = Product.objects.filter(category__iexact=category_name)
    else:
        products = Product.objects.all()

    return render(request, 'shop/shop.html', {
        'products': products,
        'categories': CATEGORIES,
        'selected_category': category_name,
    })

# --------------------
# Search View
# --------------------

def search_view(request):
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(name__icontains=query)
        return render(request, 'more_products/moreproducts.html', {
            'results': results,
            'query': query,
        })
    else:
        # If no query, show all categorized products
        context = get_categorized_products()
        return render(request, 'more_products/moreproducts.html', context)
    

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    subtotal = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        total = product.price * quantity
        subtotal += total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': total,
        })

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'grand_total': subtotal + 3,  # Flat shipping
    }
    return render(request, 'cart/cart.html', context)

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart

    return redirect('cart')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    # Convert product_id to string because session keys must be strings
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session['cart'] = cart
    return redirect('cart') 
def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
        request.session['cart'] = cart

    return redirect('cart')

def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]  # Optional: remove item if qty becomes 0
        request.session['cart'] = cart

    return redirect('cart')
def clear_cart(request):
    request.session['cart'] = {}
    return redirect('cart')

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', 'shop'))