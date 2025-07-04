# 🏗 Arquitectura y Organización del Proyecto DigitalLetter API

Este documento describe cómo está estructurado y organizado el código del proyecto para facilitar su comprensión y mantenimiento.

---

## 📁 Estructura principal de carpetas

```
digitalLetter/
├── apps/
│ ├── categories/ # Gestión de categorías con soporte multilenguaje
│ ├── products/ # Gestión de productos (platos), con traducciones y relación ManyToMany con categorías
│ ├── users/ # Gestión avanzada de usuarios con roles y permisos
│ └── company/ # Datos generales y configuración de la empresa
├── core/
│ ├── settings/ # Configuraciones por entorno (base, dev, prod, test)
│ ├── urls.py # Enrutamiento global de la API y proyecto
│ ├── wsgi.py # Punto de entrada WSGI para producción
│ └── asgi.py # Punto de entrada ASGI (si se usa)
├── manage.py # Script principal para comandos de Django
├── requirements.txt # Dependencias del proyecto
├── Dockerfile # Configuración para contenerizar la aplicación
├── docker-compose.yml # Orquestación de contenedores (app + db + etc)
└── docs/ # Documentación del proyecto (incluye este archivo)
```
---

## ⚙️ Modularización de settings

- La configuración está dividida en varios archivos para facilitar ambientes:
  - `base.py` con configuración común.
  - `development.py` para desarrollo local.
  - `production.py` para producción.
  - `test.py` para pruebas automáticas.

- Esto se controla con la variable de entorno `DJANGO_ENV` para cargar el settings adecuado.

---

## 📦 Apps y su responsabilidad

- **Categories:** gestión de categorías, con soporte para traducciones usando `django-parler`.
- **Products:** gestión de productos/platos, con traducciones y relación ManyToMany a categorías.
- **Users:** gestión avanzada de usuarios, roles (client, employe, boss) y permisos personalizados.
- **Company:** datos generales y configuración administrativa de la empresa.

---

## 🔀 Enrutamiento y APIs

- Se utiliza `rest_framework.routers.DefaultRouter` para registrar los endpoints de cada app.
- Cada app expone un `ViewSet` o conjunto de vistas RESTful.
- Las URLs están agrupadas bajo prefijos como `/api/categories/`, `/api/products/`, `/api/employe/`, etc.
- Endpoints adicionales para autenticación y gestión de usuarios (login JWT, cambio de contraseña, perfil).

---

## 🧩 Buenas prácticas y patrones

- Separación clara entre serializadores para lectura y escritura.
- Validaciones personalizadas en serializers para reglas de negocio.
- Uso de permisos granulares basados en roles para controlar accesos.
- Uso de pruebas automatizadas con `pytest` para asegurar calidad.
- Implementación de soporte multilenguaje sólo en las apps que lo necesitan (`categories` y `products`).

---