from django.db import models


# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.username

class SRF(models.Model):
    s_id=models.CharField(max_length=50,primary_key=True)
    s_name=models.CharField(max_length=50)
    s_branch=models.CharField(max_length=50)
    def __str__(self):
        return self.s_name