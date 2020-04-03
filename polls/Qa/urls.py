from django.urls import path
from .  import views

urlpatterns = [
    path('<int:quastion_id>/', views.detail),
]
