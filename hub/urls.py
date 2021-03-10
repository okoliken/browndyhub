from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home, name="home"),
    path("about/", views.about, name="about"),
    path("cart/", views.cart, name="cart"),
    path("clothe/", views.clothe, name="clothe"),
    path("descrip/", views.descrip, name="descrip")
]
