from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100)

class Food(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  description = models.TextField()
  image_url = models.URLField()


  