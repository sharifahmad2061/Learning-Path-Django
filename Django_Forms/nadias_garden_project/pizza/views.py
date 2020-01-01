from django.shortcuts import render
from django.forms import formset_factory

from .forms import PizzaForm, MultiplePizzaForm
from .models import Pizza, Size


def index(request):
    return render(request, 'pizza/index.html')


def order(request):
    multiple_pizza_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            # save pizza order to db
            pizza = Pizza()
            size = Size.objects.get(
                title=filled_form.cleaned_data['pizza_size'])
            pizza.topping1 = filled_form.cleaned_data['topping1']
            pizza.topping2 = filled_form.cleaned_data['topping2']
            pizza.size = size
            pizza.save()
            #send user response
            response = 'Your {} pizza with {} & {} toppings is on its way!'.format(
                filled_form.cleaned_data['pizza_size'],
                filled_form.cleaned_data['topping1'],
                filled_form.cleaned_data['topping2'])
            new_form = PizzaForm()
            return render(
                request, 'pizza/order.html', {
                    'pizza_form': new_form,
                    'order_response': response,
                    'multiple_pizza_form': multiple_pizza_form,
                })
    else:
        pizza_form = PizzaForm()
        return render(request, 'pizza/order.html', {
            'pizza_form': pizza_form,
            'multiple_pizza_form': multiple_pizza_form
        })


def multiple_pizzas(request):
    number = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number = filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = 'Pizzas have been ordered'
            print('hello')
        else:
            note = 'Orders have not been placed'
        return render(request, 'pizza/multiple_pizzas.html', {
            'note': note,
            'formset': formset,
        })
    elif request.method == 'GET':
        return render(request, 'pizza/multiple_pizzas.html',
                      {'formset': formset})
    else:
        PizzaFormSet = formset_factory(PizzaForm, extra=2)
        formset = PizzaFormSet()
        return render(request, 'pizza/multiple_pizzas.html', {
            'note': 'there was some error in multiple form',
            'formset': formset
        })
