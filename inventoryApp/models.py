from django.db import models

class CreateBook(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    publication_date=models.DateField()
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

