from django.db import models

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=40)
    pprice=models.IntegerField()
    poffer=models.FloatField()
    def __str__(self):
        return self.pname