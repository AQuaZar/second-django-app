from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "George Milch",
        "my_telegram": "a_quazar",
        "my_favorite_food": ["pasta", "pizza", "ramen"],
    }
    return render(request, "about.html", my_context)
