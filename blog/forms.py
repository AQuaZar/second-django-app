from django import forms

from .models import Article


class ArticleModelForm(forms.ModelForm):
    # title = forms.CharField(
    #     label="", widget=forms.TextInput(attrs={"placeholder": "Type your title here"})
    # )
    # content = forms.CharField(
    #     lable="",
    #     widget=forms.Textarea(
    #         attrs={"placeholder": "Type your content here", "rows": 30, "cols": 150}
    #     ),
    # )

    class Meta:
        model = Article
        fields = ["title", "content", "active"]
