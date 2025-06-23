import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.products.models import Plates
from apps.categories.models import Category

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def category():
    return Category.objects.create(name="1")

@pytest.fixture
def another_category():
    return Category.objects.create(name="2")

@pytest.fixture
def plate(category):
    plate = Plates.objects.create(
        name="Pizza",
        description="Cheesy",
        price=12.50,
        available=True,
        stock=5
    )
    plate.categories.add(category)
    return plate
