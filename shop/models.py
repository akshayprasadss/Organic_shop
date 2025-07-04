from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    photo = models.ImageField(upload_to='reviews/', blank=True, null=True)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)  # ✅ auto-fills on creation

    def __str__(self):
        return self.name
