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


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AboutView(models.Model):
    title = models.CharField(max_length=200)
    staff = models.CharField(max_length=200)
    image = models.ImageField(upload_to='about')

    def __str__(self):
        return self.title
