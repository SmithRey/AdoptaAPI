# 6. Tareas y planificación — solución Sprint 0

**Sprint Goal:** dejar la base técnica lista para desarrollar: solución .NET 8, EF Core, Swagger, Git y wireframes.

## Tabla del documento (sección 6)

| Sprint | IDs | Entregables clave | Duración |
|---|---|---|---|
| **Sprint 0** | T-01 a T-06 | Solución .NET 8, EF Core, Swagger, Git, wireframes Figma | 1 semana |

## Desglose de entregables (cómo se cierra cada tarea)

| ID | Entregable | Responsable | Estimación | Cómo se resuelve | Evidencia |
|---|---|---|---|---|---|
| **T-01** | Solución .NET 8 | P1 (Scrum Master) | 5 SP / 4 h | Solución `Microservicio.sln` en **net8.0**. Carpetas `Controllers`, `Models` y `Data`. Se quitó el `WeatherForecast` de plantilla. | `dotnet build` sin errores. Estructura visible en Visual Studio. |
| **T-02** | Git | P2 (Dev) | 3 SP / 2 h | `.gitignore` de .NET, `README.md` con clone/run/push, ramas `main` + `feature/t-xx`. Primer commit del Sprint 0. | Repo en GitHub/GitLab. `bin/` y `obj/` no aparecen. |
| **T-03** | EF Core | P3 (Dev) | 5 SP / 4 h | Paquetes EF Core 8. `AdoptaDbContext` mapea `USUARIO`, `FUNDACION`, `MASCOTA`, `SOLICITUD_ADOPCION`. Cadena `ConnectionStrings:AdoptaAPI`. | `GET /api/mascotas` en Swagger contra la BD. |
| **T-04** | Swagger | P4 (Product Owner) | 3 SP / 2 h | Swashbuckle con título **AdoptaAPI v1**. Al correr la API abre `/swagger`. | Captura de Swagger + prueba de `GET /api/salud`. |
| **T-05** | Wireframes Figma | Quien hizo Figma | 2 SP | Pantallas: listado de mascotas, detalle, solicitud de adopción. **Ya cerrada** en el tablero del equipo. | Link o export PDF/PNG del archivo Figma. |
| **T-06** | Script SQL + conexión | Figma (apoyo) | 3 SP / 2 h | Ejecutar `AdoptaApi.sql` (crea BD + datos de prueba). Documentar cadena en README. | BD `AdoptaAPI` con 4 tablas y datos seed. |

## Orden de trabajo (1 semana)

```
Día 1  Planning + T-01 (raíz) + T-02 en paralelo + T-05 (ya Done)
Día 2  T-01 termina → arrancan T-03 y T-04
Día 3  Daily 1. T-03 DbContext + T-06 validar SQL
Día 4  T-04 evidencia Swagger. Daily 2
Día 5  Review (demo API + tablero) + Retrospectiva
```

**Dependencias:** T-03 y T-04 esperan a T-01. T-02 no espera a nadie. T-06 acompaña a T-03.

## Ceremonias de la semana

| Día | Ceremonia | Duración |
|---|---|---|
| 1 | Sprint Planning | 45–60 min |
| 2 o 3 | Daily Scrum | 15 min |
| 4 o 5 | Daily Scrum | 15 min |
| 5 | Sprint Review + Retrospectiva | 50–70 min |

## Definition of Done (aplica a T-01 … T-06)

1. Código compilando.
2. Endpoint probado en Swagger (si la tarea toca API).
3. Commit en Git con mensaje descriptivo.
4. PR revisado si trabajan con ramas.
5. El Product Owner acepta el ítem.

## Qué quedó implementado en el repo

- **T-01:** `Controllers/` (Salud, Mascotas, Pedido), `Models/` (Usuario, Fundación, Mascota, Solicitud), `Data/AdoptaDbContext.cs`
- **T-02:** `.gitignore` + `README.md` con comandos de Git
- **T-03:** EF Core SqlServer 8 + `AdoptaDbContext` alineado a `AdoptaApi.sql`
- **T-04:** Swagger UI titulado AdoptaAPI; arranca en `/swagger`
- **T-05:** a cargo del compañero de Figma (no se toca el código)
- **T-06:** `AdoptaApi.sql` + cadena de conexión en `appsettings.json`
