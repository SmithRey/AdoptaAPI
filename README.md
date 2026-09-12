# AdoptaAPI

API .NET 8 para adopción de mascotas (proyecto Profe Richi).  
**Sprint 0:** solución base, EF Core, Swagger y Git.

Repo público: https://github.com/SmithRey/AdoptaAPI

## Requisitos

- .NET 8 SDK
- SQL Server (local o LocalDB)
- Git

## Cómo correr la API

Desde la raíz de este repositorio:

```bash
dotnet restore AdoptaAPI.sln
dotnet run --project src/AdoptaAPI.csproj
```

Swagger: `http://localhost:5052/swagger`  
Con HTTPS: `https://localhost:7133/swagger`  
Endpoint de prueba (sin base de datos): `GET /api/salud`

## Base de datos (T-03 / T-06)

1. Ejecuta `AdoptaApi.sql` en SQL Server (crea la base `AdoptaAPI` y datos de prueba).
2. Revisa la cadena en `src/appsettings.json`:

```json
"ConnectionStrings": {
  "AdoptaAPI": "Server=(localdb)\\mssqllocaldb;Database=AdoptaAPI;Trusted_Connection=True;TrustServerCertificate=True;MultipleActiveResultSets=true"
}
```

Si usas SQL Server completo (no LocalDB), cambia `Server=` a `localhost`.

3. Primera migración (opcional si ya corriste el `.sql`):

```bash
cd src
dotnet ef migrations add InitialCreate --output-dir Data/Migrations
dotnet ef database update
```

## Endpoints Sprint 0

| Método | Ruta | Qué hace |
|---|---|---|
| GET | `/api/salud` | Health check (no necesita SQL) |
| GET | `/api/mascotas` | Lista mascotas (EF Core) |
| GET | `/api/mascotas/disponibles` | Solo estado Disponible |
| POST | `/api/pedido` | Crea una solicitud de adopción |

## Estructura

```
AdoptaAPI/
  AdoptaAPI.sln
  AdoptaApi.sql
  src/
    Controllers/    Salud, Mascotas, Pedido (solicitud de adopción)
    Models/         Usuario, Fundacion, Mascota, SolicitudAdopcion, PedidoAdopcion
    Data/           AdoptaDbContext + migraciones
    Program.cs      Swagger + EF Core
  docs/
    evidencias/     Capturas Sprint 0
    informe/        Documentos del proyecto
```

## Evidencias Sprint 0

Las capturas públicas están en [docs/evidencias](docs/evidencias/README.md).
