# 📄 DigitalLetter API

Bienvenido a **DigitalLetter API** — un backend RESTful construido con Django y Django REST Framework para manejar categorías, productos (platos), y usuarios con roles diferenciados.

---

## 🚀 Tecnologías usadas

- Python 3.11  
- Django 5.2  
- Django REST Framework  
- Pytest para testing  
- DRF Spectacular para documentación OpenAPI/Swagger  
- Base de datos SQLite (por defecto)  

---

## 📦 Estructura principal

- **apps/categories/**: Gestión de categorías  
- **apps/products/**: Gestión de platos y productos, con relación ManyToMany a categorías  
- **apps/users/**: Gestión avanzada de usuarios con roles (`client`, `employe`, `boos`)  
- **core/**: Configuración global del proyecto  

---

## 🔍 Endpoints principales

| Recurso    | URL base          | Métodos          | Descripción                         |
|------------|-------------------|------------------|-----------------------------------|
| Categorías | `/api/categories/`| GET, POST, PUT...| CRUD de categorías                 |
| Platos     | `/api/products/`  | GET, POST, PUT...| CRUD de platos con categorías     |
| Empleados  | `/api/employe/`   | GET, POST, PATCH | Gestión usuarios con rol `employe`|
| Clientes   | `/api/clients/`   | GET, POST, PATCH | Gestión usuarios con rol `client` |

---

## 🔐 Autenticación y permisos

- Por ahora, los permisos están abiertos (`AllowAny`) para facilitar el desarrollo.  
- En producción, se recomienda añadir autenticación y permisos para proteger los endpoints.  

---

## 📋 Modelos destacados

### Users

- Hereda de `AbstractUser` con campos personalizados como `role`, `address`, `location`, `phone`.  
- Roles: `client`, `employe`, `boos`.  
- Manejo de contraseña seguro con `set_password`.  

### Plates (Productos)

- Campos como `name`, `description`, `price`, `stock`, `available`.  
- Relación ManyToMany con categorías.  
- Serializadores separados para lectura (`ProductSerializerGet`) y escritura (`ProductSerializerPost`).  

---

## 🐳 Docker

Este proyecto puede ejecutarse dentro de contenedores Docker usando `Dockerfile` y `docker-compose.yml`.

Para iniciar:
> Asegúrate de tener Docker y Docker Compose instalados previamente.
```bash
docker-compose up --build

```


Esto permite instalar correctamente las dependencias de requirements.txt que incluyen mysqlclient.

## 🧪 Cómo ejecutar los tests
Para correr los tests con pytest:

```bash
pytest
```
## 📂 Rutas principales (routers)
Se definen usando DefaultRouter para cada app:
```
```python
router.register(r'categories', CategoriesView, basename='categories')
router.register(r'products', ProductsViewSetGet, basename='products')
router.register(r'employe', RegisterEmploye, basename='employe')
router.register(r'clients', RegisterClients, basename='clients')
```

## ⚙️ Configuración

Usa `.env` para variables sensibles (no incluido en el repo).

La base de datos por defecto es **SQLite**, que no requiere configuración adicional.

Si en el futuro quieres cambiar a PostgreSQL u otro motor, puedes modificar `DATABASES` en `core/settings.py`.

Configura almacenamiento para imágenes (`MEDIA_ROOT` y `MEDIA_URL`).


## 💡 Buenas prácticas
Usa serializers separados para lectura y escritura si necesitas formatos diferentes.

Valida datos en los serializers (por ejemplo, precio no negativo).

Usa fixtures y pytest.mark.django_db para tests que interactúan con la base de datos.

Mantén rutas RESTful con viewsets y routers para claridad y escalabilidad.

## 📬 Contacto
Si quieres contribuir o tienes dudas, ¡escríbeme!

Gracias por usar DigitalLetter API ✨







