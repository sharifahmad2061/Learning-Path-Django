from django.shortcuts import render

from .forms import PizzaForm


def index(request):
    return render(request, 'pizza/index.html')


def order(request):
    pizzaform = PizzaForm()
    return render(request, 'pizza/order.html', {'pizza_form': pizzaform})
