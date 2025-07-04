import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.products.models import Plates
from apps.categories.models import Category


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_create_product_with_translations_and_categories(api_client):
    # Primero crea categorías
    cat1 = Category.objects.create()
    cat1.set_current_language('es')
    cat1.name = "Categoría ES"
    cat1.save()
    cat1.set_current_language('en')
    cat1.name = "Category EN"
    cat1.save()

    url = reverse('products-list')
    payload = {
        "translations": {
            "es": {
                "name": "Producto ES",
                "description": "Descripción ES"
            },
            "en": {
                "name": "Product EN",
                "description": "Description EN"
            }
        },
        "price": "10.00",
        "stock": 50,
        "available": True,
        "categories": [cat1.pk],
        "image": None
    }
    response = api_client.post(url, payload, format='json')
    assert response.status_code == 201
    data = response.json()
    assert 'translations' in data
    assert data['translations']['es']['name'] == "Producto ES"
    assert data['categories'] == [cat1.pk]


@pytest.mark.django_db
def test_list_products_only_available(api_client):
    # Producto disponible
    plate1 = Plates.objects.create(price=5, stock=10, available=True)
    plate1.set_current_language('es')
    plate1.name = "Disponible ES"
    plate1.save()
    # Producto no disponible
    plate2 = Plates.objects.create(price=5, stock=10, available=False)
    plate2.set_current_language('es')
    plate2.name = "No disponible ES"
    plate2.save()

    url = reverse('products-list')
    response = api_client.get(url)
    assert response.status_code == 200
    data = response.json()
    names = [item['translations']['es']['name'] for item in data]
    assert "Disponible ES" in names
    assert "No disponible ES" not in names


@pytest.mark.django_db
def test_retrieve_product(api_client):
    plate = Plates.objects.create(price=20, stock=5, available=True)
    plate.set_current_language('es')
    plate.name = "Plato ES"
    plate.description = "Desc ES"
    plate.save()

    url = reverse('products-detail', args=[plate.pk])
    response = api_client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data['translations']['es']['name'] == "Plato ES"


@pytest.mark.django_db
def test_update_product(api_client):
    plate = Plates.objects.create(price=30, stock=20, available=True)
    plate.set_current_language('es')
    plate.name = "Plato ES"
    plate.description = "Desc ES"
    plate.save()

    cat = Category.objects.create()
    cat.set_current_language('es')
    cat.name = "Categoria ES"
    cat.save()

    url = reverse('products-detail', args=[plate.pk])
    payload = {
        "translations": {
            "es": {
                "name": "Plato Editado ES",
                "description": "Desc editada ES"
            },
            "en": {
                "name": "Edited Plate EN",
                "description": "Edited desc EN"
            }
        },
        "price": "50.00",
        "stock": 100,
        "available": True,
        "categories": [cat.pk],
        "image": None
    }
    response = api_client.put(url, payload, format='json')
    assert response.status_code == 200
    data = response.json()
    assert data['translations']['es']['name'] == "Plato Editado ES"
    assert data['categories'] == [cat.pk]


@pytest.mark.django_db
def test_partial_update_product(api_client):
    plate = Plates.objects.create(price=15, stock=30, available=True)
    plate.set_current_language('es')
    plate.name = "Plato ES"
    plate.description = "Desc ES"
    plate.save()

    url = reverse('products-detail', args=[plate.pk])
    payload = {
        "translations": {
            "es": {
                "name": "Plato Parcial"
            }
        }
    }
    response = api_client.patch(url, payload, format='json')
    assert response.status_code == 200
    data = response.json()
    assert data['translations']['es']['name'] == "Plato Parcial"


@pytest.mark.django_db
def test_delete_product(api_client):
    plate = Plates.objects.create(price=10, stock=10, available=True)
    plate.set_current_language('es')
    plate.name = "Plato ES"
    plate.save()

    url = reverse('products-detail', args=[plate.pk])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert Plates.objects.filter(pk=plate.pk).count() == 0


#TODO revisar test en todos los modelos de la app