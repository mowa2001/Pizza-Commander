from django.shortcuts import render, redirect
from .models import Pizza, Order, OrderItem

# Create your views here.
def index(request):
    return render (request, 'food/index.html')

# Vue pour afficher le menu des pizzas
def menu(request):
    pizzas = Pizza.objects.all()
    return render(request, 'food/menu.html', {'pizzas': pizzas})

# Vue pour ajouter une pizza au panier
def add_to_cart(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    quantity = int(request.POST.get('quantity', 1)) 
    cart = request.session.get('cart', {})
    if pizza_id in cart:
        cart[pizza_id] += quantity
    else:
        cart[pizza_id] = quantity
    request.session['cart'] = cart
    return redirect('menu')



# Vue pour afficher le panier
def cart(request):
    cart = request.session.get('cart', {})
    pizzas_in_cart = []
    total_price = 0
    for pizza_id, quantity in cart.items():
        pizza = Pizza.objects.get(id=pizza_id)
        pizzas_in_cart.append({'pizza': pizza, 'quantity': quantity})
        total_price += pizza.price * quantity
    return render(request, 'food/cart.html', {'pizzas_in_cart': pizzas_in_cart, 'total_price': total_price})

# Vue pour passer commande
def checkout(request):
    if request.method == 'POST':
        customer_name = request.POST.get('name')
        customer_address = request.POST.get('address')
        customer_phone = request.POST.get('phone')
        cart = request.session.get('cart', {})

        order = Order.objects.create(
            customer_name=customer_name,
            customer_address=customer_address,
            customer_phone=customer_phone,
            total_price=0
        )

        total_price = 0
        for pizza_id, quantity in cart.items():
            pizza = Pizza.objects.get(id=pizza_id)
            OrderItem.objects.create(order=order, pizza=pizza, quantity=quantity)
            total_price += pizza.price * quantity
        
        order.total_price = total_price
        order.save()

        # Vider le panier après la commande
        request.session['cart'] = {}

        return render(request, 'food/confirmation.html', {'order': order})
    return render(request, 'food/checkout.html')
