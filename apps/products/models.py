from django.db import models
from apps.categories.models import Category

class Plates(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='plates/', blank=True, null=True)
    available = models.BooleanField(default=True)
    stock = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, related_name='plates', blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Plates"
        ordering = ['name']

