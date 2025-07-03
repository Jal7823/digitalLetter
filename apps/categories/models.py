from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField('Name', max_length=100),
        description=models.TextField('Description', blank=True, null=True)
    )
    image = models.ImageField(upload_to="categories/", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or f"Category {self.pk}"