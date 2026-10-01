from django.db import models

# Create your models here.
class Client(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=40)
    ccomp=models.CharField(max_length=40)
    def __str__(self):
        return self.cid

class Customer(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=40)
    cmob=models.IntegerField() 
    def __str__(self):
        return self.cname

class Order(models.Model):
    oid=models.IntegerField()
    oname=models.CharField(max_length=30)
    ono=models.IntegerField()
    ordprice=models.IntegerField()
    def __str__(self):
        return self.oname 