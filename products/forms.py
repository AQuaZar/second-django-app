from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label="", widget=forms.TextInput(attrs={"placeholder": "Type your title here"})
    )
    email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={"class": "13123213", "id": "fsafsa", "rows": 15, "cols": 100}
        ),
    )
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = ["title", "description", "price"]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not valid title")
        else:
            return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not "@" in email:
            raise forms.ValidationError("This is not valid email")
        else:
            return email


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
