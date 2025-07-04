import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.categories.models import Category


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_create_category_with_translations(api_client):
    url = reverse('categories-list')
    payload = {
        "translations": {
            "es": {
                "name": "pruebas",
                "description": "esta es la descripcion"
            },
            "en": {
                "name": "test",
                "description": "this is a description"
            }
        },
        "image": None
    }
    response = api_client.post(url, payload, format='json')
    assert response.status_code == 201
    data = response.json()
    assert 'translations' in data
    assert 'es' in data['translations']
    assert data['translations']['es']['name'] == "pruebas"
    assert data['translations']['en']['name'] == "test"


@pytest.mark.django_db
def test_list_categories(api_client):
    category = Category.objects.create()
    category.create_translation('es', name='Prueba ES', description='Descripción en español')
    category.create_translation('en', name='Test EN', description='English description')
    category.save()
    category.refresh_from_db()

    url = reverse('categories-list')
    response = api_client.get(url, HTTP_ACCEPT_LANGUAGE='es')
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert 'translations' in data[0]
    assert 'es' in data[0]['translations']




@pytest.mark.django_db
def test_retrieve_category(api_client):
    category = Category.objects.create()
    category.create_translation('es', name='Prueba ES', description='Descripción en español')
    category.create_translation('en', name='Test EN', description='English description')
    category.save()
    category.refresh_from_db()  # <-- Esto fuerza que el objeto tenga las traducciones cargadas

    url = reverse('categories-detail', args=[category.pk])
    response = api_client.get(url, HTTP_ACCEPT_LANGUAGE='es')
    assert response.status_code == 200
    data = response.json()
    assert 'es' in data['translations']
    assert data['translations']['es']['name'] == 'Prueba ES'




@pytest.mark.django_db
def test_update_category(api_client):
    category = Category.objects.create()
    category.set_current_language('es')
    category.name = 'Prueba ES'
    category.description = 'Descripción en español'
    category.save()

    url = reverse('categories-detail', args=[category.pk])
    payload = {
        "translations": {
            "es": {
                "name": "pruebas editado",
                "description": "descripcion editada"
            },
            "en": {
                "name": "test edited",
                "description": "edited description"
            }
        },
        "image": None
    }
    response = api_client.put(url, payload, format='json')
    assert response.status_code == 200
    data = response.json()
    assert data['translations']['es']['name'] == "pruebas editado"


@pytest.mark.django_db
def test_partial_update_category(api_client):
    category = Category.objects.create()
    category.set_current_language('es')
    category.name = 'Prueba ES'
    category.description = 'Descripción en español'
    category.save()

    url = reverse('categories-detail', args=[category.pk])
    payload = {
        "translations": {
            "es": {
                "name": "prueba parcial"
            }
        }
    }
    response = api_client.patch(url, payload, format='json')
    assert response.status_code == 200
    data = response.json()
    assert data['translations']['es']['name'] == "prueba parcial"


@pytest.mark.django_db
def test_delete_category(api_client):
    category = Category.objects.create()
    category.set_current_language('es')
    category.name = 'Prueba ES'
    category.description = 'Descripción en español'
    category.save()

    url = reverse('categories-detail', args=[category.pk])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert Category.objects.filter(pk=category.pk).count() == 0
