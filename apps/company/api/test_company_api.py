import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.company.models import Company

pytestmark = pytest.mark.django_db 

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def company():
    return Company.objects.create(name="Test Company",phone=123456789)

def test_get_company_list(api_client, company):
    url = reverse("company-list")
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Test Company"
    assert response.data[0]["phone"] == 123456789

def test_create_company(api_client):
    url = reverse("company-list")
    data = {
        "name": "New Company",
        "phone": 987654321,
        "email": "updated@email.com",      # 👈 requerido
        "address": "New address", 
    }
    response = api_client.post(url, data, format="json")

    
    assert response.status_code == 201
    assert Company.objects.filter(name="New Company").exists()

def test_update_company(api_client, company):
    url = reverse("company-detail", args=[company.id])
    data = {
        "name": "Updated Company",
        "phone": 987654321,
        "email": "updated@email.com",      # 👈 requerido
        "address": "New address",           # 👈 requerido
    }
    response = api_client.put(url, data, format="json")

    assert response.status_code == 200


def test_delete_company(api_client, company):
    url = reverse("company-detail", args=[company.id])
    response = api_client.delete(url)

    assert response.status_code == 204
    assert Company.objects.count() == 0

def test_company_detail(api_client, company):
    url = reverse("company-detail", args=[company.id])
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data["name"] == company.name
    assert response.data["phone"] == company.phone

