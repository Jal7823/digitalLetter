# tests/test_company.py

import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.company.models import Company

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def company():
    return Company.objects.create(
        name="Test Company",
        address="123 Test Street",
        email="test@example.com",
        phone=123456789
    )

@pytest.mark.django_db
def test_list_companies(api_client, company):
    url = reverse('company-list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert any(c['id'] == company.id for c in response.json())

@pytest.mark.django_db
def test_create_company(api_client):
    url = reverse('company-list')
    data = {
        "name": "New Company",
        "address": "456 New Avenue",
        "email": "new@example.com",
        "phone": 987654321
    }
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert response.data['name'] == "New Company"

@pytest.mark.django_db
def test_retrieve_company(api_client, company):
    url = reverse('company-detail', args=[company.id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == company.id

@pytest.mark.django_db
def test_update_company(api_client, company):
    url = reverse('company-detail', args=[company.id])
    data = {
        "name": "Updated Name",
        "address": "New Address",
        "email": "updated@example.com",
        "phone": 111222333
    }
    response = api_client.put(url, data)
    assert response.status_code == 200
    assert response.data['name'] == "Updated Name"

@pytest.mark.django_db
def test_partial_update_company(api_client, company):
    url = reverse('company-detail', args=[company.id])
    data = {
        "phone": 999999999
    }
    response = api_client.patch(url, data)
    assert response.status_code == 200
    assert response.data['phone'] == 999999999

@pytest.mark.django_db
def test_delete_company(api_client, company):
    url = reverse('company-detail', args=[company.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Company.objects.filter(id=company.id).exists()
