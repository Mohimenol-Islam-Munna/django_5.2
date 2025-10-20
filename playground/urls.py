from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.playground_hello_view, name="playground-hello"),
]