from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='home')

    def __str__(self):
        return self.title


class Featured(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='featured')

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.title
