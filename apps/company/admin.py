from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Company

@admin.register(Company)
class CompanyAdmin(TranslatableAdmin):
    list_display = ('name', 'email', 'phone')