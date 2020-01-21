from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm, RawProductForm


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    # context = {"title": obj.title, "description": obj.description}
    context = {"form": form}
    return render(request, "products/product_create.html", context)


def product_detail_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id=my_id)
    context = {"object": obj}
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    # post request
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect("../../../")
    context = {"object": obj}
    return render(request, "products/product_delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {"object_list": queryset}
    return render(request, "products/product_list.html", context)
