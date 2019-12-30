from django.shortcuts import render

from .forms import PizzaForm


def index(request):
    return render(request, 'pizza/index.html')


def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            response = 'Your {} pizza with {} & {} toppings is on its way!'.format(
                filled_form.cleaned_data['pizza_size'],
                filled_form.cleaned_data['topping1'],
                filled_form.cleaned_data['topping2'])
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {
                'pizza_form': new_form,
                'order_response': response
            })
    else:
        pizza_form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizza_form': pizza_form})
