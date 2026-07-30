# Sistema de Gestión Universitaria

API REST para gestionar alumnos, profesores, cursos y asignaciones en una universidad.

## Stack

- Python 3.14 + Django 6.0.7
- Django REST Framework 3.17.1
- drf-spectacular (documentación OpenAPI)
- django-jazzmin (admin theme)
- SQLite (desarrollo)

## Modelos

```
Profesor ──┐                   ┌── Alumno
           │  Asignaciones     │
Curso    ──┘                   └── Asignaciones
              ↑                      ↑
         (profesor + curso)    (alumno + asignacion + estado + nota)
```

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Crear un `.env` en la raíz:

```env
SECRET_KEY=tu-clave-segura-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Endpoints

### API REST (`/api/`)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET/POST | `/api/profesores/` | Listar/crear profesores |
| GET/PUT/PATCH/DELETE | `/api/profesores/{id}/` | CRUD profesor |
| GET/POST | `/api/cursos/` | Listar/crear cursos |
| GET/PUT/PATCH/DELETE | `/api/cursos/{id}/` | CRUD curso |
| GET/POST | `/api/profesores/{id}/asignaciones/` | Asignaciones por profesor |
| GET/POST | `/api/cursos/{id}/asignaciones/` | Asignaciones por curso |
| GET/POST | `/api/alumnos/` | Listar/crear alumnos |
| GET/PUT/PATCH/DELETE | `/api/alumnos/{id}/` | CRUD alumno |
| GET | `/api/alumnos/{id}/matriculas/` | Matrículas por alumno |
| GET/POST | `/api/asignaciones/{id}/matriculas/` | Matrículas por asignación |

### Documentación interactiva

- Swagger: `/api/schema/swagger-ui/`
- Redoc: `/api/schema/redoc/`
- Schema JSON: `/api/schema/`

### Admin

- `/admin/` — Interfaz administrativa Django + Jazzmin

## Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

## Producción

Antes de desplegar:

```bash
python manage.py check --deploy
```

Ajustar `.env`:

```env
DEBUG=False
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
```
