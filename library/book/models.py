from django.db import models

# Create your models here.
class book(models.Model):
    book_name = models.CharField(max_length=50)
    public_year = models.DateField()
    publisher_name = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)
