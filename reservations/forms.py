from django import forms
from .models import Reservations

class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = "__all__"