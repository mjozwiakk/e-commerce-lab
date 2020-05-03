from django import forms

PAYMENTS= (
    ('P', 'Przelew bankowy'),
    ('O', 'Płatnośc przy odbiorze')
)


class CheckoutForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    company = forms.CharField(required=False, max_length=100)
    city = forms.CharField(required=True, max_length=100)
    zip_code = forms.CharField(required=True, max_length=6)
    address = forms.CharField(required=True, max_length=10)
    payment = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=PAYMENTS)


class ConfirmOrderForm(forms.Form):
    shop_rules = forms.BooleanField(required=True)