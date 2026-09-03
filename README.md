# AdoptaAPI

API .NET 8 para adopción de mascotas (proyecto Profe Richi).  
**Sprint 0:** solución base, EF Core, Swagger y Git.

## Requisitos

- .NET 8 SDK
- SQL Server (local o LocalDB)
- Git

## Cómo correr la API

```bash
cd "Proyecto Api/Microservicio/ApisPedido"
dotnet restore
dotnet run
```

Swagger se abre en: `http://localhost:5052/swagger`  
Endpoint de prueba (sin base de datos): `GET /api/salud`

## Base de datos (T-03 / T-06)

1. Ejecuta `AdoptaApi.sql` en SQL Server (crea `AdoptaAPI` y datos de prueba).
2. Revisa la cadena en `appsettings.json`:

```json
"ConnectionStrings": {
  "AdoptaAPI": "Server=(localdb)\\mssqllocaldb;Database=AdoptaAPI;Trusted_Connection=True;TrustServerCertificate=True;MultipleActiveResultSets=true"
}
```

En este equipo ya se ejecutó `AdoptaApi.sql` contra **SQL Server LocalDB** (`MSSQLLocalDB`). Si usas SQL Server completo (no LocalDB), cambia `Server=` a `localhost`.

3. Primera migración (opcional si ya corriste el `.sql`):

```bash
dotnet ef migrations add InitialCreate --output-dir Data/Migrations
dotnet ef database update
```

## Endpoints Sprint 0

| Método | Ruta | Qué hace |
|---|---|---|
| GET | `/api/salud` | Health check (no necesita SQL) |
| GET | `/api/mascotas` | Lista mascotas (EF Core) |
| GET | `/api/mascotas/disponibles` | Solo estado Disponible |
| POST | `/api/pedido` | Ejemplo de pedidos (clase) |

## Git (T-02) — primer push del equipo

Desde la carpeta del proyecto (`ProyectoApi Profe Richi`):

```bash
git init
git add .
git commit -m "feat(sprint-0): solución .NET 8, EF Core, Swagger y estructura AdoptaAPI"
git branch -M main
git remote add origin https://github.com/TU-EQUIPO/AdoptaAPI.git
git push -u origin main
```

Ramas sugeridas:

- `main` — estable
- `develop` — integración
- `feature/t-01` … `feature/t-06` — una rama por tarea

El `.gitignore` ya excluye `bin/`, `obj/`, `.vs/` y secretos locales.

## Estructura

```
Proyecto Api/Microservicio/
  Microservicio.sln
  ApisPedido/
    Controllers/    Salud, Mascotas, Pedido
    Models/         Usuario, Fundacion, Mascota, SolicitudAdopcion
    Data/           AdoptaDbContext
    Program.cs      Swagger + EF Core
```

## Definition of Done (Sprint 0)

- Código compila (`dotnet build`)
- Endpoint probado en Swagger
- Commit con mensaje descriptivo
- PR revisado si hay ramas
