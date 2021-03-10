from django.urls import path
from . import views

urlpatterns = [
    path("auto/",views.auto, name="auto"),
]