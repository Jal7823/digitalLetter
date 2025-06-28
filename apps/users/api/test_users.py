import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from apps.users.models import Users


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    def _create_user(username, email, name, password, role='client', is_staff=False):
        user = Users.objects.create_user(
            username=username,
            email=email,
            name=name,
            password=password
        )
        user.role = role
        user.is_staff = is_staff
        user.save()
        return user
    return _create_user

@pytest.fixture
def get_token(api_client):
    def _get_token(username, password):
        url = reverse('token_obtain_pair')
        response = api_client.post(url, {"username": username, "password": password})
        return response.data['access']
    return _get_token


# ------------------ TEST REGISTER CLIENT ------------------

@pytest.mark.django_db
def test_create_client(api_client):
    url = reverse('clients-list')
    data = {
        "username": "client1",
        "email": "client@example.com",
        "name": "Client One",
        "password": "securepass123"
    }
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert Users.objects.filter(username="client1").exists()


# ------------------ TEST REGISTER EMPLOYEE (REQUIRES STAFF) ------------------

@pytest.mark.django_db
def test_create_employe_requires_staff(api_client, create_user, get_token):
    staff = create_user("admin", "admin@example.com", "Admin", "adminpass", role='boos', is_staff=True)
    token = get_token("admin", "adminpass")
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    url = reverse('employe-list')
    data = {
        "username": "employe1",
        "email": "employe@example.com",
        "name": "Employe One",
        "password": "securepass123"
    }
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert Users.objects.filter(username="employe1", role="employe").exists()


# ------------------ TEST ME ENDPOINT ------------------

@pytest.mark.django_db
def test_me_endpoint(api_client, create_user, get_token):
    user = create_user("client2", "c2@example.com", "Client 2", "clientpass")
    token = get_token("client2", "clientpass")
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    url = reverse('me')
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['username'] == "client2"


# ------------------ TEST CHANGE PASSWORD ------------------

@pytest.mark.django_db
def test_change_password(api_client, create_user, get_token):
    user = create_user("client3", "c3@example.com", "Client 3", "oldpass")
    token = get_token("client3", "oldpass")
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    url = reverse('change-password')
    data = {
        "old_password": "oldpass",
        "new_password": "newsecure123",
        "new_password_confirm": "newsecure123"
    }
    response = api_client.post(url, data)
    assert response.status_code == 200

    # Confirm that new password works
    new_token = api_client.post(reverse('token_obtain_pair'), {
        "username": "client3",
        "password": "newsecure123"
    })
    assert new_token.status_code == 200
    assert "access" in new_token.data
