from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReservationForm


def hello_world(request):
    return HttpResponse("Hello World")


def home(request):
    form = ReservationForm()
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Reservation successful")
    return render(request, 'index.html', {'form': form} )