from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    my_context = {"my_text": "George Milch", "my_telegram": "a_quazar"}
    return render(request, "contact.html", my_context)
