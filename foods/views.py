from django.shortcuts import render
from .models import Food
from django.shortcuts import render
from cart.forms import Food_Cart_Form
# Create your views here.

def food_list(request):
    food_list =Food.objects.all()
    return render(request,'foods/list.html',{"foods":food_list})

def food_detail(request,id):
    food =Food.objects.get(id=id)
    cart_form = Food_Cart_Form()
    return render(request,'foods/detail.html',{'food':food ,'form':cart_form})
