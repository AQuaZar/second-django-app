from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "price"]


class RawProductForm(forms.Form):
    title = forms.CharField(
        label="", widget=forms.TextInput(attrs={"placeholder": "Type your title here"})
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"class": "13123213", "id": "fsafsa", "rows": 15, "cols": 100}
        ),
    )
    price = forms.DecimalField()
