# Sprint 0 — Guía para Jira y arranque técnico

**Proyecto:** AdoptaAPI (API .NET 8 — Profe Richi)  
**Sprint:** Sprint 0 — Configuración inicial  
**Duración sugerida:** 1 semana  
**Objetivo del Sprint:** Dejar el proyecto listo para desarrollar: solución .NET 8, Git, EF Core, Swagger, tablero Scrum y Definition of Done.

Usa este documento para **copiar y pegar** en Jira. Los textos ya vienen con descripción, estimación y responsable.

---

## Estado actual del repo (qué ya está hecho)

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 Solución .NET 8 | **Lista** | `Microservicio.sln` net8.0, carpetas `Controllers`, `Models` y `Data`. Compila. |
| T-02 Git | **Lista en local** | `.gitignore` + `README.md`. Falta el `git push` del equipo a GitHub. |
| T-03 EF Core | **Lista** | `AdoptaDbContext` + paquetes EF Core 8. Mapea las 4 tablas de AdoptaAPI. |
| T-04 Swagger | **Lista** | Título **AdoptaAPI v1**. Arranca en `/swagger`. |
| T-05 Figma / wireframes | **Cerrada** | Quien hizo Figma queda libre para apoyar o tomar T-06 |
| T-06 Script SQL + conexión | **Lista** | `AdoptaApi.sql` + `ConnectionStrings:AdoptaAPI` en `appsettings.json` |

---

## 1. Crear el proyecto Scrum en Jira

1. Entra a [https://www.atlassian.com/software/jira](https://www.atlassian.com/software/jira) (plan Free).
2. **Create project** → plantilla **Scrum** (no Kanban, no “Team-managed Kanban”).
3. Nombre: `AdoptaAPI`  
   Key sugerida: `ADA`
4. Tipo: **Team-managed** (más simple para universidad) o **Company-managed** si el profesor pide reportes clásicos.
5. Confirma que aparecen:
   - **Backlog**
   - **Board** (tablero del Sprint)
   - **Reports** → Burndown chart

Eso cubre la evidencia académica: backlog + sprint + burndown.

---

## 2. Product Backlog (épicas)

Crea estas **Épicas**. Sprint 0 usa solo la primera.

### Épica 1 — Configuración inicial (Sprint 0)

> Dejar la base técnica y el proceso Scrum listos: solución .NET 8, Git, EF Core, Swagger, tablero y DoD.

### Épica 2 — Autenticación

> Registrar e iniciar sesión de usuarios (adoptantes y fundaciones).

### Épica 3 — CRUD de recursos

> CRUD de Usuario, Fundación, Mascota y Solicitud de adopción.

### Épica 4 — Documentación con Swagger

> Endpoints documentados, probados y publicados en Swagger UI.

### Historias de usuario (sprints siguientes, no Sprint 0)

Cópialas al backlog **después** de las tareas T-01…T-06, con prioridad más baja:

**ADA-US-01** — Como adoptante, quiero ver mascotas disponibles para elegir una.  
**ADA-US-02** — Como adoptante, quiero enviar una solicitud de adopción.  
**ADA-US-03** — Como fundación, quiero registrar mascotas y actualizar su estado.  
**ADA-US-04** — Como fundación, quiero aprobar o rechazar solicitudes.  
**ADA-US-05** — Como usuario, quiero autenticarme para proteger mis datos.

---

## 3. Tareas T-01 a T-06 (copiar a Jira)

En **Backlog** → **Create sprint** → nombre: `Sprint 0 - Configuración inicial`.  
Luego **Create issue** de tipo **Task** (o Sub-task si las cuelgas de la Épica 1).

### T-01 — Crear la solución .NET 8

| Campo | Valor |
|---|---|
| Tipo | Task |
| Épica | Configuración inicial |
| Sprint | Sprint 0 |
| Responsable | **P1** (Scrum Master) |
| Estimación | 5 story points / 4 horas |
| Prioridad | Highest |
| Dependencias | Ninguna (es la raíz) |

**Descripción (pegar en Jira):**

```
Objetivo
Crear la solución .NET 8 con estructura de carpetas Controllers, Models y Data.

Alcance
- Solución Visual Studio (.sln) en net8.0
- Proyecto API (ASP.NET Core Web API)
- Carpetas: Controllers, Models, Data
- Program.cs con pipeline básico
- Quitar o dejar documentado el WeatherForecast de plantilla

Criterios de aceptación
- La solución abre y compila en Visual Studio / `dotnet build`
- Existen las 3 carpetas
- Se puede ejecutar la API (`dotnet run`)

Notas
El repo ya tiene Microservicio.sln + ApisPedido (net8.0). Completar carpeta Data y dejar evidencia de build.
```

### T-02 — Configurar Git

| Campo | Valor |
|---|---|
| Tipo | Task |
| Épica | Configuración inicial |
| Sprint | Sprint 0 |
| Responsable | **P2** (Dev) |
| Estimación | 3 story points / 2 horas |
| Prioridad | High |
| Dependencias | Puede ir **en paralelo** con T-01 |

**Descripción:**

```
Objetivo
Dejar el repositorio Git listo para el equipo.

Alcance
- Repo en GitHub/GitLab (privado o el que pida el profesor)
- .gitignore de .NET (bin/, obj/, .vs/, user secrets)
- Rama main (o master) protegida
- Rama de trabajo: develop (opcional) o feature/t-xx
- README con cómo clonar, restaurar paquetes y correr la API
- Primer push

Criterios de aceptación
- git clone funciona para todos
- bin/obj/.vs no se suben
- Hay al menos 1 commit con mensaje descriptivo
```

### T-03 — Configurar EF Core

| Campo | Valor |
|---|---|
| Tipo | Task |
| Épica | Configuración inicial |
| Sprint | Sprint 0 |
| Responsable | **P3** (Dev) |
| Estimación | 5 story points / 4 horas |
| Prioridad | High |
| Dependencias | **Espera T-01** |

**Descripción:**

```
Objetivo
Conectar la API a SQL Server con Entity Framework Core.

Alcance
- Paquetes: Microsoft.EntityFrameworkCore.SqlServer y Design
- DbContext en carpeta Data
- Cadena de conexión en appsettings.json / appsettings.Development.json
  (no subir contraseñas reales)
- Primera migración alineada a AdoptaApi.sql
  (USUARIO, FUNDACION, MASCOTA, SOLICITUD_ADOPCION)
- Registrar el DbContext en Program.cs

Criterios de aceptación
- `dotnet ef migrations add InitialCreate` funciona
- La API arranca leyendo la cadena de conexión
- El modelo refleja las tablas del script SQL
```

### T-04 — Configurar Swagger

| Campo | Valor |
|---|---|
| Tipo | Task |
| Épica | Configuración inicial |
| Sprint | Sprint 0 |
| Responsable | **P4** (Product Owner) |
| Estimación | 3 story points / 2 horas |
| Prioridad | High |
| Dependencias | **Espera T-01** (puede ir casi a la vez que T-03) |

**Descripción:**

```
Objetivo
Dejar Swagger UI como evidencia de la API.

Alcance
- Swashbuckle.AspNetCore
- UseSwagger / UseSwaggerUI en Development
- Título y versión visibles (AdoptaAPI v1)
- Probar al menos un endpoint desde /swagger

Criterios de aceptación
- Al correr la API se abre /swagger
- Hay al menos 1 endpoint documentado y probado
- Captura de pantalla para la entrega

Notas
Ya está en Program.cs (AddSwaggerGen + UseSwaggerUI). Esta tarea es pulir título, probar y adjuntar evidencia.
```

### T-05 — Wireframes / Figma

| Campo | Valor |
|---|---|
| Tipo | Task |
| Épica | Configuración inicial |
| Sprint | Sprint 0 |
| Responsable | Quien hizo Figma |
| Estimación | 2 story points |
| Prioridad | Medium |
| Estado | **Done** (ya cerrada) |

**Descripción:**

```
Objetivo
Entregar wireframes de las pantallas principales (listado de mascotas, detalle, solicitud).

Estado
Cerrada. La persona queda libre para apoyar bloqueos o tomar T-06.
```

### T-06 — Script SQL y cadena de conexión

| Campo | Valor |
|---|---|
| Tipo | Task |
| Épica | Configuración inicial |
| Sprint | Sprint 0 |
| Responsable | Quien hizo Figma **o** el que termine primero |
| Estimación | 3 story points / 2 horas |
| Prioridad | Medium |
| Dependencias | Encaja con T-03 |

**Descripción:**

```
Objetivo
Dejar la base de datos AdoptaAPI lista para el equipo.

Alcance
- Ejecutar / validar AdoptaApi.sql en SQL Server
- Documentar en README: servidor, nombre de BD, usuario de desarrollo
- Cadena de conexión de ejemplo (sin secretos) para T-03
- Datos de prueba verificados (10 usuarios, fundaciones, mascotas, solicitudes)

Criterios de aceptación
- La BD AdoptaAPI existe y tiene las 4 tablas
- Un compañero puede recrearla siguiendo el README
```

**Orden de trabajo:**

```
T-05 (cerrada)
T-02  ──────────►  (en paralelo, no espera a nadie)
T-01  ──►  T-03  ──►  T-06 (si hace falta ajustar el SQL)
       └──► T-04  (casi al mismo tiempo que T-03)
```

---

## 4. Roles Scrum (Sprint 0)

| Persona | Rol | Qué hace en este Sprint | Tarea |
|---|---|---|---|
| **P1** | Scrum Master | Facilita Planning, Daily, Review y Retro. Quita bloqueos. No es el jefe. | T-01 (raíz) |
| **P2** | Developer | Construye el incremento. Daily de 15 min. | T-02 Git |
| **P3** | Developer | Igual que P2. Empieza T-03 en cuanto compile T-01. | T-03 EF Core |
| **P4** | Product Owner | Prioriza el backlog, representa al “cliente” (el profesor / usuario adoptante). Acepta o rechaza el Done. | T-04 Swagger |
| **Figma** | Developer (apoyo) | T-05 cerrada. Apoya retrasos o toma T-06. | T-06 |

En equipos chicos de universidad los roles pueden **rotar el próximo Sprint**. Anótenlo en la Retro.

Texto corto para pegar en la descripción del proyecto Jira:

```
Scrum Team — Sprint 0
- Product Owner: P4 (prioriza backlog, acepta incremento)
- Scrum Master: P1 (ceremonias e impedimentos)
- Developers: P2, P3 y quien hizo Figma
```

---

## 5. Tablero (columnas)

En el board de Jira: **Board settings** → columnas.

| Columna Jira | Estado | Para qué |
|---|---|---|
| To Do | To Do | Comprometido en el Sprint, aún no se toca |
| In Progress | In Progress | Alguien está trabajando (máx. 1–2 ítems por persona) |
| In Review | In Review | Código listo: compile + Swagger + PR / revisión de compañero |
| Done | Done | Cumple la Definition of Done |

Si el profesor pide evidencia extra, copien el mismo tablero en **Miro** o **Trello** y tomen captura al inicio, a mitad y al cierre del Sprint.

---

## 6. Definition of Done (DoD)

Una tarea **no se mueve a Done** si falta cualquiera de estos puntos:

1. El código **compila** (`dotnet build` sin errores).
2. Si hay endpoint, está **probado en Swagger** (o con `.http`).
3. Hay **commit** en Git con mensaje descriptivo (ejemplo: `feat(t-01): estructura Controllers Models Data`).
4. Si hay ramas: **PR revisado** por al menos 1 compañero.
5. Cumple lo que dice la tarjeta (criterios de aceptación).
6. No se suben secretos (contraseñas, `appsettings` con claves reales).
7. El Product Owner (P4) acepta el ítem.

Pegar esto en Jira: **Project settings → Features** o en una página Confluence / descripción del Sprint.

---

## 7. Ceremonias (evidencia del proceso)

Aunque el Sprint dure **1 semana**, agenden esto y dejen acta (captura de Meet, lista de asistencia o notas en Jira):

| Ceremonia | Cuándo | Duración | Quién | Resultado |
|---|---|---|---|---|
| **Sprint Planning** | Día 1, inicio | 45–60 min | Todo el Scrum Team | Sprint Goal + T-01…T-06 en el Sprint |
| **Daily 1** | Día 2 o 3 | 10–15 min | Developers (+ SM) | Plan de 24 h, impedimentos |
| **Daily 2** | Día 4 o 5 | 10–15 min | Developers (+ SM) | Ajuste hacia el Sprint Goal |
| **Sprint Review** | Cierre | 30–40 min | Team + “stakeholders” (profesor o un compañero de otro grupo) | Demo: API corre, Swagger, Git, tablero |
| **Retrospectiva** | Justo después de la Review | 20–30 min | Scrum Team | 1 o 2 mejoras para Sprint 1 |

**Sprint Goal (pegar en el Sprint de Jira):**

> Dejar la base técnica y el proceso Scrum operando: solución .NET 8 compilando, repositorio Git, EF Core con DbContext, Swagger visible y tablero con DoD.

### Guion corto del Planning

1. PO (P4): por qué vale este Sprint (base para el CRUD).
2. Equipo: ¿qué entra? T-01 a T-06.
3. Devs: ¿cómo? orden T-01 → T-03/T-04; T-02 en paralelo.
4. SM (P1): DoD y horarios de Daily.

### Preguntas del Daily (no es reporte al SM)

- ¿Qué hice que acerca el Sprint Goal?
- ¿Qué haré hoy?
- ¿Qué me bloquea?

---

## 8. Arranque técnico (T-01)

Con roles y tablero listos, P1 mueve **T-01 → In Progress**.

Checklist de T-01:

- [x] Solución .NET 8 (`ApisPedido.csproj` → `net8.0`)
- [x] Carpeta `Controllers`
- [x] Carpeta `Models`
- [x] Carpeta `Data` (agregada para cumplir la estructura)
- [x] Swagger ya habilitado (T-04 puede cerrarse con evidencia)
- [ ] Primer commit de equipo (T-02)
- [ ] EF Core + DbContext (T-03)
- [ ] Validar `AdoptaApi.sql` en SQL Server (T-06)

Comandos útiles:

```bash
dotnet build
dotnet run --project "Proyecto Api/Microservicio/ApisPedido"
```

Swagger: `https://localhost:<puerto>/swagger`

---

## Capturas que suelen pedir en la entrega

1. Proyecto Jira tipo **Scrum** (no Kanban).
2. Backlog con épicas + T-01…T-06.
3. Sprint 0 activo con las 6 tareas.
4. Tablero To Do / In Progress / In Review / Done.
5. Burndown (aunque sea plano al inicio).
6. DoD pegada en el Sprint o en Confluence.
7. Acta o captura de Planning, Daily, Review y Retro.
8. API corriendo + Swagger.
9. Repo Git con `.gitignore` y commits.

---

## Referencia rápida de asignación

| Persona | Rol | Tarea | ¿Puede empezar ya? |
|---|---|---|---|
| P1 | Scrum Master | T-01 solución .NET 8 | Sí (raíz) |
| P2 | Dev | T-02 Git | Sí (paralelo) |
| P3 | Dev | T-03 EF Core | Cuando compile T-01 |
| P4 | Product Owner | T-04 Swagger | Cuando compile T-01 (Swagger ya está: documentar y evidenciar) |
| Figma | Apoyo | T-06 SQL | Sí (el script ya existe; validar y documentar) |
