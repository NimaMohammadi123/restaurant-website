from django.conf import settings
from foods.models import Food

class Cart:
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart = cart
    
    
    def add(self , food , quantity = 1 , override_quantity = False):
        food_id = str(food.id)
        if food_id not in self.cart:
            self.cart[food_id] = {'quantity':0 , 'price':food.price}
        if override_quantity:
            self.cart[food_id]['quantity'] = quantity
        else:
            self.cart[food_id]['quantity'] += quantity
        
        self.save()
        
    def save(self):
        self.session.modified = True
    
    def remove (self,food):
        food_id = str(food.id)
        if food_id in self.cart:
            del self.cart[food_id]
        self.save()
    
    def __iter__(self):
        food_ids = self.cart.keys()
        foods = Food.objects.filter(id__in=food_ids)
        cart = self.cart.copy()
        
        for food in foods:
            cart[str(food.id)]['food'] = food
        
        for item in cart.values():
            item['total_price'] = item['quantity'] * item['price']
            yield item
        
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()