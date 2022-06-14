from django.shortcuts import render
from .cart import Cart
from foods.models import Food
from django.shortcuts import get_object_or_404 , redirect , render
from django.views.decorators.http import require_POST
from .forms import Food_Cart_Form

# Create your views here.

@require_POST
def cart_add(request,food_id):
    cart = Cart(request)
    food = get_object_or_404(Food , id=food_id)
    form = Food_Cart_Form(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(food=food , quantity=cd['quantity'] , override_quantity=cd['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request,food_id):
    cart = Cart(request)
    food = get_object_or_404(Food , id=food_id)
    cart.remove(food)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_form'] = Food_Cart_Form(initial={
            'quantity':item['quantity'],
            'override':True
        })
    return render(request , 'cart/detail.html' , {'cart':cart})