from django import forms
from django_countries.fields import CountryField

PAYMENTS= (
    ('P', 'Przelew bankowy'),
    ('F', 'Szybkie płatności - PayU')
)


class CheckoutForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    company = forms.CharField(required=False, max_length=100)
    city = forms.CharField(required=True, max_length=100)
    zip_code = forms.CharField(required=True, max_length=6)
    address = forms.CharField(required=True, max_length=10)
    country = CountryField(blank_label='(select country)').formfield(required=True)
    payment = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=PAYMENTS)