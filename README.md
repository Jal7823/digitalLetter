
# 📄 DigitalLetter API
Bienvenido a **DigitalLetter API** — un backend RESTful construido con Django y Django REST Framework para manejar categorías, productos (platos) y usuarios con roles diferenciados.

[![codecov](https://codecov.io/gh/Jal7283/digitalLetter/branch/main/graph/badge.svg)](https://codecov.io/gh/Jal7283/digitalLetter)

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

---

## 📦 Estructura principal

- `apps/categories/`: Gestión de categorías  
- `apps/products/`: Gestión de platos/productos, relacionados con categorías (ManyToMany)  
- `apps/users/`: Gestión avanzada de usuarios con roles (`client`, `employe`, `boos`)  
- `apps/company/`: Datos generales de la empresa  
- `core/`: Configuración global del proyecto (`settings`, `urls`, `wsgi`)  

---

## 🔍 Endpoints principales

| Recurso    | URL base            | Métodos           | Descripción                         |
|------------|---------------------|-------------------|-------------------------------------|
| Categorías | `/api/categories/`  | GET, POST, PUT... | CRUD de categorías                  |
| Platos     | `/api/products/`    | GET, POST, PUT... | CRUD de platos vinculados a categorías |
| Empleados  | `/api/employe/`     | GET, POST, PATCH  | Gestión de usuarios con rol `employe` |
| Clientes   | `/api/clients/`     | GET, POST, PATCH  | Gestión de usuarios con rol `client` |
| Autenticación | `/api/token/`    | POST              | Login con JWT                       |
| Usuario actual | `/api/me/`      | GET, PATCH        | Perfil del usuario autenticado      |
| Cambio de contraseña | `/api/change-password/` | POST | Cambiar contraseña del usuario |

---

## 📑 Documentación

Accede a la documentación automática de la API generada con **DRF Spectacular**:

- Swagger UI: `http://localhost:8000/`  
- Redoc: `http://localhost:8000/api/redoc/`  
- Esquema OpenAPI (JSON): `http://localhost:8000/api/schema/`

---

## 🔐 Autenticación y permisos

- Autenticación JWT vía `/api/token/` (obtener token) y `/api/token/refresh/` (refrescar)
- Permisos configurados según roles (`IsStaff`, `IsEmploye`, etc.)
- Algunas rutas abiertas (`AllowAny`) durante desarrollo

---

## 📋 Modelos destacados

### 🧑 Users

- Hereda de `AbstractUser`  
- Campos adicionales: `role`, `address`, `location`, `province`, `phone`, `image`  
- Roles posibles: `client`, `employe`, `boos`  
- Manejo seguro de contraseñas con `set_password`

### 🍽 Plates (Productos)

- Campos: `name`, `description`, `price`, `stock`, `available`, `image`  
- Relación ManyToMany con `Category`  
- Serializadores separados para lectura (`ProductSerializerGet`) y escritura (`ProductSerializerPost`)  
- Validación personalizada en `price`  

---

## ⚙️ Configuración del entorno

### .env

Usa un archivo `.env` (no incluido en el repo) con tus variables sensibles, como:

> DJANGO_SECRET_KEY=your-secret-key
> DJANGO_ENV=development
> DEBUG=True


Se carga automáticamente con `python-dotenv` desde `manage.py`.

### Base de datos

Se usa SQLite por defecto. Puedes cambiar a PostgreSQL en `core/settings/production.py`.

---

## 🐳 Docker

Este proyecto incluye soporte Docker listo para usar:

```bash
docker-compose up --build
```
Asegúrate de tener .env y que los puertos/volúmenes estén bien configurados en tu docker-compose.yml.

✅ ## Testing
Usa pytest con pytest-django:

```bash 
pytest
```
Usa pytest.mark.django_db para pruebas que accedan a la base de datos.

Evita tests con imágenes si no son necesarios (multipart).

La suite cubre: categorías, platos, usuarios y lógica de permisos.

## Enrutamiento principal
Registrado con DefaultRouter para cada viewset. Ejemplo:

```
python

router.register(r'categories', CategoriesView, basename='categories')
router.register(r'products', ProductsViewSetGet, basename='products')
router.register(r'employe', RegisterEmploye, basename='employe')
router.register(r'clients', RegisterClients, basename='clients')
```
🧠 ## Buenas prácticas implementadas
- Serializadores separados para lectura y escritura cuando el formato lo requiere

- Validaciones personalizadas en los serializers

- Uso de viewsets.ModelViewSet + routers para mantener rutas limpias y RESTful

- Permisos personalizados por rol (IsStaffOrEmploye, etc.)

- División de settings por entorno usando DJANGO_ENV

📬 ## Contacto
¿Quieres contribuir o tienes preguntas? ¡Contáctame!

Gracias por usar DigitalLetter API ✨
✅ Estado del build en GitHub Actions

📊 Cobertura de pruebas (opcional, requiere configuración con codecov.io)
