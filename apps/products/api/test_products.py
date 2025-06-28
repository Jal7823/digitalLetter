# tests/test_products.py

import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.products.models import Plates
from apps.categories.models import Category

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def category():
    return Category.objects.create(name="Category A", description="Desc A")

@pytest.fixture
def plate(category):
    plate = Plates.objects.create(
        name="Test Plate",
        description="Delicious",
        price=10.00,
        available=True,
        stock=5,
    )
    plate.categories.set([category])
    return plate

@pytest.mark.django_db
def test_list_plates(api_client, plate):
    url = reverse('products-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert any(p['id'] == plate.id for p in response.json())

@pytest.mark.django_db
def test_retrieve_plate(api_client, plate):
    url = reverse('products-detail', args=[plate.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == plate.id

@pytest.mark.django_db
def test_create_plate(api_client, category):
    url = reverse('products-list')
    data = {
        "name": "New Plate",
        "description": "Tasty",
        "price": 12.00,
        "available": True,
        "stock": 10,
        "categories": [category.id]
    }
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert response.data['name'] == "New Plate"

@pytest.mark.django_db
def test_create_plate_negative_price(api_client, category):
    url = reverse('products-list')
    data = {
        "name": "Invalid Plate",
        "description": "Nope",
        "price": -5.00,
        "available": True,
        "stock": 3,
        "categories": [category.id]
    }
    response = api_client.post(url, data)
    assert response.status_code == 400
    assert "price" in response.data

@pytest.mark.django_db
def test_update_plate(api_client, plate, category):
    url = reverse('products-detail', args=[plate.id])
    data = {
        "name": "Updated Plate",
        "description": "Now with cheese",
        "price": 15.00,
        "available": False,
        "stock": 2,
        "categories": [category.id]
    }
    response = api_client.put(url, data)
    assert response.status_code == 200
    assert response.data['name'] == "Updated Plate"

@pytest.mark.django_db
def test_partial_update_plate(api_client, plate):
    url = reverse('products-detail', args=[plate.id])
    data = {
        "stock": 99
    }
    response = api_client.patch(url, data)
    assert response.status_code == 200
    assert response.data['stock'] == 99

@pytest.mark.django_db
def test_delete_plate(api_client, plate):
    url = reverse('products-detail', args=[plate.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Plates.objects.filter(id=plate.id).exists()
