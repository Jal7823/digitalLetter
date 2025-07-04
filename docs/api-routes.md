
# 🛣️ Descripción Detallada de Endpoints y Rutas API

Este documento detalla los endpoints principales de la API DigitalLetter, los métodos HTTP disponibles, y ejemplos básicos de uso.

---

| Recurso           | URL base                | Métodos          | Descripción                           |
| ----------------- | ----------------------- | ---------------- | ------------------------------------- |
| Categorías        | `/api/categories/`      | GET, POST, PUT, PATCH, DELETE | CRUD de categorías                  |
| Platos            | `/api/products/`        | GET, POST, PUT, PATCH, DELETE | CRUD de platos, vinculados a categorías |
| Empleados         | `/api/employe/`         | GET, POST, PATCH  | Gestión de usuarios con rol `employe` |
| Clientes          | `/api/clients/`         | GET, POST, PATCH  | Gestión de usuarios con rol `client`  |
| Autenticación     | `/api/token/`           | POST             | Login con JWT                       |
| Usuario actual    | `/api/me/`              | GET, PATCH        | Perfil del usuario autenticado      |
| Cambio contraseña | `/api/change-password/` | POST             | Cambiar contraseña del usuario      |

---

## Ejemplos básicos de uso

### Obtener lista de categorías

```http
GET /api/categories/
Accept: application/json
```

Respuesta:

```json
[
  {
    "id": 1,
    "name": "Entrantes"
  },
  {
    "id": 2,
    "name": "Postres"
  }
]
```

---

### Crear una nueva categoría con traducción

```http
POST /api/categories/
Content-Type: application/json

{
  "translations": {
    "es": {"name": "Bebidas"},
    "en": {"name": "Drinks"}
  }
}
```

Respuesta:

```json
{
  "id": 3,
  "name": "Bebidas"
}
```

---

### Autenticación JWT

```http
POST /api/token/
Content-Type: application/json

{
  "username": "usuario",
  "password": "contraseña"
}
```

Respuesta:

```json
{
  "access": "token_jwt",
  "refresh": "token_refresh"
}
```

---

### Obtener perfil del usuario autenticado

```http
GET /api/me/
Authorization: Bearer token_jwt
```

Respuesta:

```json
{
  "id": 5,
  "username": "usuario",
  "email": "usuario@ejemplo.com",
  "role": "client"
}
```

---

¿Quieres que te prepare ejemplos para endpoints específicos o explicar cómo probarlos con curl o Postman?
