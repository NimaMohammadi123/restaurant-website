from email.policy import default
from django import forms

FOODS_QUANTITY_CHOICES = [(i,str(i))for i in range (1,21)]

class Food_Cart_Form(forms.Form):
    quantity = forms.TypedChoiceField(choices=FOODS_QUANTITY_CHOICES , coerce=int)
    override = forms.BooleanField(required=False , initial=False , widget=forms.HiddenInput)

