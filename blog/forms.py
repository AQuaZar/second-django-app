from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label="", widget=forms.TextInput(attrs={"placeholder": "Type your title here"})
    )
    content = forms.CharField(
        lable="",
        widget=forms.Textarea(
            attrs={"placeholder": "Type your content here", "rows": 30, "cols": 150}
        ),
    )
