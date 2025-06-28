# tests/test_categories.py

import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.categories.models import Category
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def category():
    return Category.objects.create(
        name="Test Category",
        description="Test Description"
    )

@pytest.mark.django_db
def test_list_categories(api_client, category):
    url = reverse('categories-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert any(cat['id'] == category.id for cat in response.json())

@pytest.mark.django_db
def test_create_category(api_client):
    url = reverse('categories-list')
    image = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
    data = {
        "name": "New Category",
        "description": "New description",
    }
    response = api_client.post(url, data, format='multipart')
    assert response.status_code == 201
    assert response.data['name'] == "New Category"

@pytest.mark.django_db
def test_retrieve_category(api_client, category):
    url = reverse('categories-detail', args=[category.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == category.id
    assert response.data['name'] == category.name

@pytest.mark.django_db
def test_update_category(api_client, category):
    url = reverse('categories-detail', args=[category.id])
    data = {
        "name": "Updated Category",
        "description": "Updated Description"
    }
    response = api_client.put(url, data)
    assert response.status_code == 200
    assert response.data['name'] == "Updated Category"

@pytest.mark.django_db
def test_partial_update_category(api_client, category):
    url = reverse('categories-detail', args=[category.id])
    data = {
        "description": "Partially Updated"
    }
    response = api_client.patch(url, data)
    assert response.status_code == 200
    assert response.data['description'] == "Partially Updated"

@pytest.mark.django_db
def test_delete_category(api_client, category):
    url = reverse('categories-detail', args=[category.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Category.objects.filter(id=category.id).exists()
