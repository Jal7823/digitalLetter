from django.db import models


class Company(models.Model):
    """Model definition for Company."""

    name = models.CharField('Company', max_length=100)
    address = models.CharField('Address', max_length=200)
    image = models.ImageField('Image', upload_to='logos/', null=True, blank=True)
    email = models.EmailField('Email', max_length=100)
    phone = models.IntegerField('Phone')

    class Meta:
        """Meta definition for Company."""

        verbose_name = 'Company'
        verbose_name_plural = 'Company'

    def __str__(self):
        """Unicode representation of Company."""
        return self.name