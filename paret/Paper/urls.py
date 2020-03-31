from django.urls import path
from . import views

urlpatterns = [
    path('first_paper', views.paret_paper),
]
