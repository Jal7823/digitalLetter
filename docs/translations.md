# 🌍 Soporte de Traducciones (`django-parler`)

Este proyecto utiliza `django-parler` para permitir la gestión de contenido multilingüe en los modelos de **Categorías** y **Platos (Products)**.

## 📦 ¿Dónde se usa?

Actualmente, las traducciones están habilitadas solo en estas apps:

- `apps/categories/`
- `apps/products/`

No están disponibles (por ahora) en:

- `apps/users/`
- `apps/company/`

---

## ⚙️ Cómo funciona `django-parler`

`django-parler` permite traducir campos específicos de un modelo a múltiples idiomas sin duplicar toda la instancia.

### Ejemplo (modelo de Category):

```python
from parler.models import TranslatableModel, TranslatedFields

class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100),
    )
```

Este diseño permite tener una sola categoría con múltiples traducciones de `name`, dependiendo del idioma actual del sistema.

---

## 🌐 Cómo traducir contenido

### 1. En el **panel de administración de Django**

- Aparecerán pestañas para cada idioma disponible arriba del formulario.
- Puedes cambiar de idioma y rellenar los campos traducibles.

### 2. Usando la API (desde frontend o tests)

#### Crear una categoría con traducciones

```json
POST /api/categories/
{
  "translations": {
    "es": {"name": "Entrantes"},
    "en": {"name": "Starters"}
  }
}
```

#### Leer una categoría (automáticamente en el idioma activo)

```http
GET /api/categories/?lang=en
```

Devolverá:

```json
{
  "id": 1,
  "name": "Starters"
}
```

---

## 🌍 Configuración de idiomas

En `settings.py`:

```python
LANGUAGES = [
    ("es", "Español"),
    ("en", "English"),
]

PARLER_LANGUAGES = {
    None: (
        {'code': 'es'},
        {'code': 'en'},
    ),
    'default': {
        'fallbacks': ['es'],
        'hide_untranslated': False,
    }
}
```

Puedes añadir más idiomas fácilmente.

---

## 🧪 Testing de traducciones

En los tests con `pytest`, puedes establecer el idioma activo:

```python
category.set_current_language('es')
category.name = "Entrantes"
category.save()
```

---

## ❗ Notas importantes

- Si no se encuentra una traducción para un idioma, se usa el *fallback* (`es`, por defecto).
- Si `hide_untranslated = True`, se ocultarán objetos sin traducción activa.
- Puedes acceder a todos los idiomas usando `.get_available_languages()` sobre una instancia.
