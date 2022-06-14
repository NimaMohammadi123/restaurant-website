from django.db import models

class Food(models.Model):
    FOOD_TYPE =[
        ("dinner" , "شام"),
        ("lunch" , "ناهار"),
        ("drinks" , "نوشیدنی")
    ]
    
    name =models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    rate = models.IntegerField(default = 0)
    price = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    time =models.IntegerField()
    photo = models.ImageField(upload_to='foods/')
    type_food = models.CharField(max_length=10 , choices=FOOD_TYPE , default="dinner")
    
    def __str__(self):
        return self.name
        