from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='Title custom', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                            attrs={
                                "class": "new-class-name two",
                                "id": "idk",
                                "placeholder": "Your description",
                                "cols": 120,
                                "rows": 30,
                                }
                        )
                    )
    price = forms.DecimalField(initial = 99.99)
    image = forms.ImageField(label='Picture')
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'image',
        ]

    #validation inputs
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            raise forms.ValidationError("Not a valid title")
        if "news" in title:
            raise forms.ValidationError("Not a valid title")
        else:
            return title
