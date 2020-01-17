from django.shortcuts import render

from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
# def product_create_view(request):
#     form = RawProductForm(request.POST)

#     context = {"form": form}
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#     # context = {"title": obj.title, "description": obj.description}
#     context = {}
#     return render(request, "products/product_create.html", context)
def render_initial_data(request):
    initial_data = {}
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
    context = {"form": form}
    return render(request, "products/product_create.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    # context = {"title": obj.title, "description": obj.description}
    context = {"form": form}
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {"title": obj.title, "description": obj.description}
    context = {"object": obj}
    return render(request, "products/product_detail.html", context)
