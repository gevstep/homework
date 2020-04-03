from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('my_name', views.return_my_name),
    path('my_html', views.my_html),
    path('exit_paper', views.exit_paper),
    path('test_page', views.test_page),
]
