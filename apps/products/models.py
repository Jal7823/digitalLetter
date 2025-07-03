from django.db import models
from parler.models import TranslatableModel,TranslatedFields
from apps.categories.models import Category

class Plates(TranslatableModel):
    '''Model definition for Plates.'''
    translations = TranslatedFields(
        name = models.CharField(max_length=100),
        description = models.TextField(blank=True, null=True),
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='plates/', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='plates', blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or f"Plates {self.pk}"

    class Meta:
        verbose_name_plural = "Plates"



