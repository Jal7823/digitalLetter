
# 📄 DigitalLetter API

Bienvenido a **DigitalLetter API** — un backend RESTful construido con Django y Django REST Framework para manejar categorías, productos (platos) y usuarios con roles diferenciados.

[![codecov](https://codecov.io/gh/Jal7823/digitalLetter/branch/main/graph/badge.svg)](https://codecov.io/gh/Jal7823/digitalLetter)

[![Build Status](https://img.shields.io/badge/estado-estable-brightgreen)](https://github.com/Jal7823/digitalLetter/actions)

# 📄 DigitalLetter API

Bienvenido a **DigitalLetter API** — un backend RESTful construido con Django y Django REST Framework para manejar categorías, productos (platos) y usuarios con roles diferenciados.

---

## 🚀 Tecnologías usadas

- Python 3.11
- Django 5.2
- Django REST Framework
- Simple JWT para autenticación
- DRF Spectacular para documentación OpenAPI/Swagger
- Pytest para testing
- Docker & Docker Compose
- SQLite como base de datos por defecto
- **django-parler** para traducciones multilenguaje (solo en `categories` y `products`)

---

## 📦 Estructura principal

- `apps/categories/`: Gestión de categorías (con soporte de traducciones)
- `apps/products/`: Gestión de platos/productos, relacionados con categorías (ManyToMany, con traducciones)
- `apps/users/`: Gestión avanzada de usuarios con roles (`client`, `employe`, `boos`)
- `apps/company/`: Datos generales de la empresa (sin traducciones)
- `core/`: Configuración global del proyecto (`settings`, `urls`, `wsgi`)

---

## 🔍 Endpoints principales

| Recurso           | URL base                | Métodos          | Descripción                            |
| ----------------- | ----------------------- | ---------------- | -------------------------------------- |
| Categorías        | `/api/categories/`      | GET, POST, PUT…  | CRUD de categorías                     |
| Platos            | `/api/products/`        | GET, POST, PUT…  | CRUD de platos vinculados a categorías |
| Empleados         | `/api/employe/`         | GET, POST, PATCH | Gestión de usuarios con rol `employe`  |
| Clientes          | `/api/clients/`         | GET, POST, PATCH | Gestión de usuarios con rol `client`   |
| Autenticación     | `/api/token/`           | POST             | Login con JWT                          |
| Usuario actual    | `/api/me/`              | GET, PATCH       | Perfil del usuario autenticado         |
| Cambio contraseña | `/api/change-password/` | POST             | Cambiar contraseña del usuario         |

---

## 📁 Documentación

Generada automáticamente con **DRF Spectacular**:

- Swagger UI: [`/`](http://localhost:8000/)
- Redoc: [`/api/redoc/`](http://localhost:8000/api/redoc/)
- Esquema OpenAPI (JSON): [`/api/schema/`](http://localhost:8000/api/schema/)

---

## 🔐 Autenticación y permisos

- JWT vía SimpleJWT (`/api/token/` y `/api/token/refresh/`)
- Permisos personalizados: `IsStaff`, `IsEmploye`, `IsBoss`, `IsStaffOrEmploye`
- Algunas rutas abiertas (`AllowAny`) en desarrollo

---

## 📋 Modelos destacados

### 🧑 Users

- Hereda de `AbstractUser`
- Campos personalizados: `role`, `address`, `location`, `province`, `phone`, `image`
- Roles posibles: `client`, `employe`, `boos`
- Manejo seguro de contraseñas (`set_password`)

### 🍽 Plates (Productos)

- Campos: `name`, `description`, `price`, `stock`, `available`, `image`
- Relación ManyToMany con `Category`
- Soporte de traducciones con `django-parler` en `name` y `description`
- Serializadores separados: `ProductSerializerGet` (lectura) y `ProductSerializerPost` (escritura)
- Validación de `price` para evitar valores negativos

---

## ⚙️ Configuración del entorno

### .env

Usa un archivo `.env` para variables sensibles. Ejemplo:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_ENV=development
DEBUG=True
```

Se carga automáticamente con `python-dotenv` desde `manage.py`.

### Base de datos

- Por defecto se usa **SQLite** (ideal para desarrollo).
- Puedes cambiar a PostgreSQL modificando `core/settings/production.py`.

---

## 🐳 Docker

Este proyecto está listo para ejecutarse con Docker:

```bash
docker-compose up --build
```

Asegúrate de tener `.env` y que puertos/volúmenes estén bien configurados en `docker-compose.yml`.

---

## ✅ Testing

Usa `pytest` y `pytest-django`:

```bash
pytest
```

- Usa `pytest.mark.django_db` para pruebas que usen la base de datos
- Las pruebas cubren categorías, platos, usuarios y permisos
- Evita pruebas con imágenes si no son necesarias

---

## 🔀 Enrutamiento principal

Registrado con `DefaultRouter` para cada viewset. Ejemplo:

```python
router.register(r'categories', CategoriesView, basename='categories')
router.register(r'products', ProductsViewSetGet, basename='products')
router.register(r'employe', RegisterEmploye, basename='employe')
router.register(r'clients', RegisterClients, basename='clients')
```

---

## 🧠 Buenas prácticas aplicadas

- Separación de serializadores para lectura y escritura
- Validaciones personalizadas en `serializers.py`
- Viewsets + routers para mantener una API RESTful limpia
- Permisos granulares por rol
- Settings divididos por entorno (`DJANGO_ENV`)
- Soporte de internacionalización con `django-parler` en apps seleccionadas

---

## 📬 Contacto

¿Quieres contribuir o tienes preguntas?\
**¡Escríbeme! Estaré encantado de ayudarte.**

---

🎉 ¡Gracias por usar DigitalLetter API!

