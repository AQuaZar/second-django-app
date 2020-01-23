from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .forms import ArticleModelForm
from .models import Article


class ArticleCreateView(CreateView):
    form_class = ArticleModelForm
    template_name = "blog/article_create.html"
    queryset = Article.objects.all()


class ArticleListView(ListView):
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()


class ArticleUpdateView(UpdateView):
    form_class = ArticleModelForm
    template_name = "blog/article_create.html"
    queryset = Article.objects.all()

    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Article, id=id_)


# Create your views here.
