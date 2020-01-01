from django import forms
from .models import Pizza, Size


class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='Topping 1', max_length=30)
    topping2 = forms.CharField(label='Topping 2', max_length=30)
    pizza_size = forms.ChoiceField(label='Pizza Size',
                                   choices=[('small', 'Small'),
                                            ('medium', 'Medium'),
                                            ('large', 'Large')])


# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model = Pizza
#         fields = ['topping1', 'topping2', 'size']
#         labels = {
#             'topping1': 'Topping 1',
#             'topping2': 'Topping 2',
#             'size': 'Size'
#         }


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)