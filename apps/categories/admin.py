from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Category

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    