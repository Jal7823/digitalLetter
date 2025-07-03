import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.company.models import Company


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_create_company_with_translations(api_client):
    url = reverse('company-list')
    payload = {
        "translations": {
            "es": {
                "name": "Empresa prueba",
                "address": "Calle Falsa 123"
            },
            "en": {
                "name": "Test Company",
                "address": "123 Fake Street"
            }
        },
        "email": "test@example.com",
        "phone": 1234567890,
        "image": None
    }
    response = api_client.post(url, payload, format='json')
    assert response.status_code == 201
    data = response.json()
    assert 'translations' in data
    assert data['translations']['es']['name'] == "Empresa prueba"
    assert data['email'] == "test@example.com"


@pytest.mark.django_db
def test_list_companies(api_client):
    company = Company.objects.create(email='a@a.com', phone=111111111)
    company.set_current_language('es')
    company.name = "Empresa ES"
    company.address = "Direccion ES"
    company.save()
    company.set_current_language('en')
    company.name = "Company EN"
    company.address = "Address EN"
    company.save()

    url = reverse('company-list')
    response = api_client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert 'translations' in data[0]
    assert 'es' in data[0]['translations']


@pytest.mark.django_db
def test_retrieve_company(api_client):
    company = Company.objects.create(email='a@a.com', phone=222222222)
    company.set_current_language('es')
    company.name = "Empresa ES"
    company.address = "Direccion ES"
    company.save()

    url = reverse('company-detail', args=[company.pk])
    response = api_client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data['translations']['es']['name'] == "Empresa ES"


@pytest.mark.django_db
def test_update_company(api_client):
    company = Company.objects.create(email='a@a.com', phone=333333333)
    company.set_current_language('es')
    company.name = "Empresa ES"
    company.address = "Direccion ES"
    company.save()

    url = reverse('company-detail', args=[company.pk])
    payload = {
        "translations": {
            "es": {
                "name": "Empresa editada",
                "address": "Direccion editada"
            },
            "en": {
                "name": "Edited Company",
                "address": "Edited Address"
            }
        },
        "email": "edited@example.com",
        "phone": 444444444,
        "image": None
    }
    response = api_client.put(url, payload, format='json')
    assert response.status_code == 200
    data = response.json()
    assert data['translations']['es']['name'] == "Empresa editada"
    assert data['email'] == "edited@example.com"


@pytest.mark.django_db
def test_partial_update_company(api_client):
    company = Company.objects.create(email='a@a.com', phone=555555555)
    company.set_current_language('es')
    company.name = "Empresa ES"
    company.address = "Direccion ES"
    company.save()

    url = reverse('company-detail', args=[company.pk])
    payload = {
        "translations": {
            "es": {
                "name": "Empresa parcial"
            }
        }
    }
    response = api_client.patch(url, payload, format='json')
    assert response.status_code == 200
    data = response.json()
    assert data['translations']['es']['name'] == "Empresa parcial"


@pytest.mark.django_db
def test_delete_company(api_client):
    company = Company.objects.create(email='a@a.com', phone=666666666)
    company.set_current_language('es')
    company.name = "Empresa ES"
    company.address = "Direccion ES"
    company.save()

    url = reverse('company-detail', args=[company.pk])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert Company.objects.filter(pk=company.pk).count() == 0
