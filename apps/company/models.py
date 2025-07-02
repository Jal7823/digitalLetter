from django.db import models
from parler.models import TranslatableModel,TranslatedFields


class Company(TranslatableModel):
    """Model definition for Company."""
    translations = TranslatedFields(
        name = models.CharField('Company', max_length=100),
        address = models.CharField('Address', max_length=200)
    )
    image = models.ImageField('Image', upload_to='logos/', null=True, blank=True)
    email = models.EmailField('Email', max_length=100)
    phone = models.IntegerField('Phone')

    class Meta:
        """Meta definition for Company."""

        verbose_name = 'Company'
        verbose_name_plural = 'Company'

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or f"Company {self.pk}"