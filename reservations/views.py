from multiprocessing import context
from django.shortcuts import render
from .forms import ReservationsForm
from django.http import HttpResponseRedirect
# Create your views here.

def reserve(request):
    reserve_form =ReservationsForm()
    if request.method == "POST":
        reserve_form = ReservationsForm(request.POST)
        if reserve_form.is_valid:
            reserve_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        reserve_form=ReservationsForm()        
    context = {
        "form":reserve_form ,
    }
    
    return render(request,'reservations/reservation.html',context)