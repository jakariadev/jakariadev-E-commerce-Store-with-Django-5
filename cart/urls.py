
from django.urls import path

from . import views

urlpatterns = [
    path("", views.cart_summary, name="cart_summary"),
    path("add/", views.cart_add, name="cart_add"),
    path("update/", views.cart_update, name="cart_update"),
    path("delete/", views.cart_delete, name="cart_delete"),
    # path("product/<slug:product_slug>/", views.product_info, name="product_info"),
    # path("search/<slug:category_slug>/", views.category_info, name="list_category"),
]





