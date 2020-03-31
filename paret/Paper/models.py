from django.db import models

# Create your models here.

class User_input(models.Model):
    today_date = models.CharField(max_length=2)
    user_name = models.CharField(max_length=150)
    exit_time = models.CharField(max_length=10)
    exit_address = models.CharField(max_length=150)
    visit_address = models.CharField(max_length=150)
    visit_purpose = models.CharField(max_length=100)
    return_time = models.CharField(max_length=10)
