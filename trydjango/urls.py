"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from pages.views import home_view, about_view
from products.views import (
    product_detail_view,
    product_create_view,
    render_initial_data,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view,
)

urlpatterns = [
    url("admin/", admin.site.urls),
    url("create/init/", render_initial_data),
    url("create/", product_create_view, name="create product"),
    path("product/<int:my_id>/", dynamic_lookup_view),
    path("product/<int:my_id>/delete/", product_delete_view),
    url("product/", product_list_view, name="products list"),
    url("about/", about_view, name="about"),
    url("", home_view, name="home"),
]
