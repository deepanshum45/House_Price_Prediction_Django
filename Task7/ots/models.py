from django.db import models
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
class TestHistory(models.Model):
    username = models.CharField(max_length=50)
    test_name = models.CharField(max_length=50)
    total_questions = models.IntegerField()
    score = models.IntegerField()
