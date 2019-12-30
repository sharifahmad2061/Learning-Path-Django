from django.db import models


class Size(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Pizza(models.Model):
    topping1 = models.CharField(max_length=30)
    topping2 = models.CharField(max_length=30)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)