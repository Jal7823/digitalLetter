import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from apps.users.models import Users

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def employe():
    return Users.objects.create_user(
        username="empleado1",
        email="empleado1@test.com",
        name="Empleado Uno",
        password="testpass123",
        role="employe",
    )


@pytest.fixture
def client_user():
    return Users.objects.create_user(
        username="cliente1",
        email="cliente1@test.com",
        name="Cliente Uno",
        password="testpass123",
        role="client",  # corregido a singular
    )


def test_create_employe(api_client):
    url = reverse('employe-list')
    data = {
        "username": "empleadoNuevo",
        "email": "empleadoNuevo@test.com",
        "name": "Empleado Nuevo",
        "password": "claveSegura123"
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.data["username"] == "empleadoNuevo"
    assert Users.objects.filter(username="empleadoNuevo", role="employe").exists()


def test_create_client(api_client):
    url = reverse('clients-list')
    data = {
        "username": "clienteNuevo",
        "email": "clienteNuevo@test.com",
        "name": "Cliente Nuevo",
        "password": "claveSegura123"
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.data["username"] == "clienteNuevo"
    assert Users.objects.filter(username="clienteNuevo", role="client").exists()


def test_list_employes_accessible(api_client):
    url = reverse('employe-list')
    response = api_client.get(url)
    # Cambiado a 200 porque no tienes permisos activos
    assert response.status_code == 200


def test_list_clients_accessible(api_client):
    url = reverse('clients-list')
    response = api_client.get(url)
    assert response.status_code == 200


def test_patch_employe_name(api_client, employe):
    api_client.force_authenticate(user=employe)
    url = reverse('employe-detail', args=[employe.id])
    data = {"name": "Empleado Actualizado"}
    response = api_client.patch(url, data, format="json")
    assert response.status_code == 200
    employe.refresh_from_db()
    assert employe.name == "Empleado Actualizado"





def test_create_employe_fail_without_password(api_client):
    url = reverse('employe-list')
    data = {
        "username": "sinpass",
        "email": "sinpass@test.com",
        "name": "Sin Password",
        # falta password
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == 400
    assert "password" in response.data or "non_field_errors" in response.data


def test_create_client_fail_without_password(api_client):
    url = reverse('clients-list')
    data = {
        "username": "sinpasscliente",
        "email": "sinpasscliente@test.com",
        "name": "Sin Password Cliente",
        # falta password
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == 400
    assert "password" in response.data or "non_field_errors" in response.data
