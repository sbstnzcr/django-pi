from django.urls import path

from . import views

urlpatterns = [
    path("visualization/", views.visualization, name="visualization"),
]
