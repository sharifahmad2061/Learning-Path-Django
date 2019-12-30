from django import forms


class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='Topping 1', max_length=30)
    topping2 = forms.CharField(label='Topping 2', max_length=30)
    pizza_size = forms.ChoiceField(label='Pizza Size',
                                   options=[('Small', 'small'),
                                            ('Medium', 'medium'),
                                            ('Large', 'large')])
