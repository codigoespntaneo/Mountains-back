# 🏔️ API: “Montañas del Mundo”

Una Plataforma desarrollada para una API REST completa utilizando FastAPI y una aplicación web desarrollada con HTML, CSS y JavaScript que permita documentar, visualizar y consumir la información gestionada por la API. Con la finalidad aplicar conocimientos de desarrollo backend y frontend, así como comprender el funcionamiento de las arquitecturas cliente-servidor mediante la implementación de operaciones CRUD completas.

"Una API donde registras montañas reales reimaginadas con leyendas, magia o fenómenos sobrenaturales."

### 🎯 ¿Qué vamos a construir?

Una **API CRUD de Montañas** donde podrás:

- Crear una montaña
- Listarlos todos
- Ver uno por id
- Actualizar su información
- Eliminarlos

Cada montaña tiene:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `name` | Nombre del personaje | "Monte Fuji" |
| `country` | Donde se encuentra  | "( Japón )" |
| `height` | msnm (Entero)| "3776" |
| `img` | URL de su imagen | "https://example.com/fuji.jpg" |

---

## Estructura de carpetas
```
proyecto/
│
 API-FAST-CLASS-MOUNTAINS/
  ├── .git/                          # Control de versiones
  ├── .pytest_cache/                 # Caché de pytest
  ├── __pycache__/                   # Caché de Python
  ├── venv/                          # Entorno virtual
  │
  ├── .gitignore                     # Archivos ignorados por git
  ├── conftest.py                    # Configuración de pytest
  ├── main.py                        # Punto de entrada de la aplicación
  ├── mountains.db                   # Base de datos SQLite
  ├── requirements.txt               # Dependencias del proyecto
  │
  └── src/                           # Código fuente
      ├── __init__.py
      │
      ├── shared/                    # Módulo compartido (código común)
      │   ├── application/           # Servicios/casos de uso compartidos
      │   │   └── __init__.py
      │   ├── domain/                # Entidades y reglas de dominio compartidas
      │   │   └── __init__.py
      │   ├── infraestructure/       # Implementaciones técnicas compartidas
      │   │   ├── __init__.py
      │   │   └── api.py
      │   └── test/                  # Tests del módulo shared
      │       └── infraestructure/
      │           └── test_help.py
      │
      └── mountains/                 # Módulo de montañas (dominio principal)
          ├── __init__.py
          │
          ├── application/           # Casos de uso (lógica de aplicación)
          │   ├── __init__.py
          │   ├── create_mountain.py
          │   ├── delete_mountain.py
          │   ├── get_all_mountain.py
          │   ├── get_mountain_by_id.py
          │   └── update_mountain.py
          │
          ├── domain/                # Capa de dominio
          │   ├── __init__.py
          │   ├── exception.py       # Excepciones del dominio
          │   ├── models.py          # Modelos de dominio
          │   ├── repository.py      # Interfaces de repositorio
          │   └── valid_object.py    # Objetos de valor / validaciones
          │
          ├── infraestructure/       # Capa de infraestructura
          │   ├── __init__.py
          │   ├── api.py             # Endpoints/rutas HTTP
          │   └── repository.py      # Implementación del repositorio
          │
          ├── shared/                # Sub-módulo compartido específico de mountains
          │   ├── application/
          │   │   └── __init__.py
          │   ├── domain/
          │   │   └── __init__.py
          │   ├── infraestructure/
          │   │   ├── __init__.py
          │   │   └── api.py
          │   └── test/
          │       └── infraestructure/
          │           └── test_help.py
          │
          └── test/                  # Tests del módulo mountains
              ├── application/
              │   ├── test_create_mountain.py
              │   ├── test_delete_mountain.py
              │   ├── test_get_all_mountain.py
              │   └── test_update_mountain.py
              └── infraestructure/
                  ├── api/
                  │   ├── __init__.py
                  │   ├── test_create_mountain.py
                  │   └── test_mountain_endpoints.py
                  └── repository/
                      └── test_sql_model_mountain_repository.py
|
|
└── Mountains-API/
    ├── index.html
    ├── styles.css
    └── app.js
    └── README.md

```
---

## Tecnologías utilizadas
🔙 Backend (FastAPI):
Responsable de:

- Exponer la API REST
- Gestionar datos
- Implementar CRUD
- Documentación automática

🌐 Frontend (HTML + CSS + JS):
Responsable de:

- Interfaz de usuario
- Consumo de la API
- Mostrar y manipular datos
- Interacción con formularios y botones

## Instalación en local
- Verifica que tienes Python:
  Abre una terminal y ejecuta: 
  - python3 --version, Deberías tener Python 3.9 o superior.

## Configuración del entorno
- Crea un entorno virtual:
  (Linux/macOS)
  python3 -m venv venv
  
- Activa el entorno virtual:
  Linux/macOS
  source venv/bin/activate
  
- Instala FastAPI y Uvicorn
  pip install fastapi uvicorn
  
- Crea el archivo principal
  En el archivo llamado main.py:

  from fastapi import FastAPI
  app = FastAPI()
  @app.get("/")
  def inicio():
      return {"mensaje": "Hola, FastAPI"}
  
- Ejecuta el servidor:
  uvicorn main:app --reload
  
  Donde:
   main → nombre del archivo (main.py)
   app → instancia de FastAPI()
   --reload → reinicia automáticamente cuando guardas cambios
  
- Prueba la API:
  http://127.0.0.1:8000
  
- Documentación automática:
  http://127.0.0.1:8000/docs

## Ejemplos de uso
**Crear una montaña (Everest):**
```bash
curl -X POST http://127.0.0.1:8000/mountains/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Everest",
    "country": "Nepal",
    "height": "8893",
    "img": "https://example.com/everest.jpg"
  }'
```
Respuesta:

```json
{
  "id": 1,
  "name": "Everest",
  "country": "Nepal",
  "height": "8893",
  "img": "https://example.com/everest.jpg"
}
```
**Otras montañas de ejemplo:**

```json
{
  "name": "Everest",
  "country": "Nepal",
  "height": "8893",
  "img": "https://example.com/everest.jpg"
}
```

```json
{
  "name": "Everest",
  "country": "Nepal",
  "height": "8893",
  "img": "https://example.com/everest.jpg"
}
```

```json
{
  "name": "Everest",
  "country": "Nepal",
  "height": "8893",
  "img": "https://example.com/everest.jpg"
}
```
**Listar todos los personajes:**

```bash
curl -X GET http://127.0.0.1:8000/mountains/
```

Respuesta:

```json
[
 {
   "id": 1,
   "name": "Everest",
   "country": "Nepal",
   "height": "8893",
   "img": "https://example.com/everest.jpg"
 }
]
```
**Obtener un personaje por id:**

```bash
curl -X GET http://127.0.0.1:8000/mountains/1
```

Respuesta:

```json
 {
   "id": 1,
   "name": "Everest",
   "country": "Nepal",
   "height": "8893",
   "img": "https://example.com/everest.jpg"
 }
```

Si el id no existe, devuelve `404 Not Found`:

```json
{ "detail": "Mountain not found" }
```
**Actualizar un personaje:**

```bash
curl -X PUT http://127.0.0.1:8000/mountains/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Everest",
    "country": "Nepal",
    "height": "8840",
    "img": "https://example.com/everest-v2.jpg"
  }'
```

Respuesta:

```json
{
  "id": 1,
  "name": "Everest",
  "country": "Nepal",
  "height": "dead",
  "img": "https://example.com/everest-v2.jpg"
}
```

> 💬 `PUT` reemplaza el recurso completo: hay que mandar **todos** los campos, no solo los que cambian.
**Eliminar un personaje:**

```bash
curl -X DELETE http://127.0.0.1:8000/mountains/1
```

Respuesta:

```json
{ "message": "Mountain deleted successfully" }
```

## Capturas de pantalla
<img width="2662" height="1098" alt="image" src="https://github.com/user-attachments/assets/836ce541-97a8-4b58-a1e9-0e684e1bd067" />

<img width="2622" height="1120" alt="image" src="https://github.com/user-attachments/assets/e446f4ba-6c04-4c13-bf2a-18bd265fb5b2" />

## Un diagrama de flujo de la aplicación
```
        ┌─────────┐
        │ Inicio  │
        └────┬────┘
             │
             ▼
   ┌─────────────────┐
   │ Abrir aplicación│
   └────────┬────────┘
            │
            ▼
   ┌─────────────────┐
   │ Iniciar sesión  │
   └────────┬────────┘
            │
            ▼
      ┌───────────────┐
      │¿Datos válidos?│
      └───┬──────┬────┘
         Sí      No
          │       │
          ▼       ▼
┌────────────────┐ ┌─────────────────┐
│ Mostrar menú   │ │ Mostrar error   │
└───────┬────────┘ └────────┬────────┘
        │                   │
        └──────────┬────────┘
                   ▼
        ┌─────────────────┐
        │ ¿Salir?         │
        └──────┬─────┬────┘
             No      Sí
              │       │
              ▼       ▼
        Regresa al   ┌──────┐
           menú      │ Fin  │
                     └──────┘
```

## Diagrama de arquitectura

```
                          ┌──────────────────────┐
                          │      Cliente         │
                          │ Web / Móvil / API    │
                          └──────────┬───────────┘
                                     │
                                     ▼
                      ┌────────────────────────────┐
                      │ Adaptador de Entrada       │
                      │ Controller REST            │
                      └──────────┬─────────────────┘
                                 │
                           Puerto de Entrada
                                 │
                                 ▼
                  ┌────────────────────────────────┐
                  │       DOMINIO (NÚCLEO)         │
                  │                                │
                  │  Casos de Uso (Use Cases)      │
                  │  Entidades                     │
                  │  Reglas de Negocio             │
                  │                                │
                  └──────────┬─────────────────────┘
                             │
                       Puerto de Salida
                             │
          ┌──────────────────┴──────────────────┐
          ▼                                     ▼
┌────────────────────┐              ┌────────────────────┐
│ Adaptador DB       │              │ Adaptador Externo  │
│ Repository/JPA     │              │ API, Email, etc.   │
└──────────┬─────────┘              └────────────────────┘
           │
           ▼
    ┌───────────────┐
    │ Base de Datos │
    └───────────────┘
```

## Documentación de endpoints
### Endpoints disponibles
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET    | `/` | Endpoint raíz de prueba |
| GET    | `/mountains/` | Listar todas las montañas |
| GET    | `/mountains/{id}` | Obtener una montaña por id |
| POST   | `/mountains/` | Crear una montaña |
| PUT    | `/mountains/{id}` | Actualizar una montaña |
| DELETE | `/mountains/{id}` | Eliminar una montaña |
