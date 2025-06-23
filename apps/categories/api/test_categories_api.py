import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.categories.models import Category

pytestmark = pytest.mark.django_db  # para todos los tests


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def category():
    return Category.objects.create(name="TestCat", description="test")


def test_get_category_list(api_client, category):
    url = reverse("categories-list")
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "TestCat"


def test_create_category(api_client):
    url = reverse("categories-list")
    data = {
        "name": "New Category",
        "description": "New category description",
    }
    response = api_client.post(url, data, format="json")

    assert response.status_code == 201
    assert Category.objects.filter(name="New Category").exists()


def test_update_category(api_client, category):
    url = reverse("categories-detail", args=[category.id])
    data = {
        "name": "Updated Category",
        "description": "Updated description"
    }
    response = api_client.put(url, data, format="json")

    assert response.status_code == 200
    category.refresh_from_db()
    assert category.name == "Updated Category"
    assert category.description == "Updated description"


def test_delete_category(api_client, category):
    url = reverse("categories-detail", args=[category.id])
    response = api_client.delete(url)

    assert response.status_code == 204
    assert Category.objects.count() == 0
