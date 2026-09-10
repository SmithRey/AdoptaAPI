# -*- coding: utf-8 -*-
"""Genera AdoptaAPI_Documento_Diseno.docx"""
import os
import sys

try:
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.style import WD_STYLE_TYPE
except ImportError:
    os.system(f'"{sys.executable}" -m pip install python-docx -q')
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.style import WD_STYLE_TYPE

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "AdoptaAPI_Documento_Diseno.docx")

doc = Document()

# Estilos
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)

def add_title(text):
    p = doc.add_heading(text, level=0)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return p

def add_h1(text):
    doc.add_heading(text, level=1)

def add_h2(text):
    doc.add_heading(text, level=2)

def add_h3(text):
    doc.add_heading(text, level=3)

def add_p(text, bold=False):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = bold
    return p

def add_bullet(text, level=0):
    doc.add_paragraph(text, style='List Bullet')

def add_table(headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = 'Light Grid Accent 1'
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = h
        for p in hdr[i].paragraphs:
            for r in p.runs:
                r.bold = True
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            table.rows[ri + 1].cells[ci].text = str(val)
    doc.add_paragraph()

def add_code(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = 'Consolas'
    run.font.size = Pt(9)
    p.paragraph_format.left_indent = Inches(0.3)

# === PORTADA ===
add_title('AdoptaAPI')
add_p('Documento de Diseño y Planificación', bold=True).alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph()
add_p('Sistema de Gestión de Adopción de Mascotas').alignment = WD_ALIGN_PARAGRAPH.CENTER
add_p('Versión 1.0 — Agosto 2026').alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.add_paragraph()
add_table(
    ['Campo', 'Valor'],
    [
        ['Stack', 'ASP.NET Core MVC 8 · C# · JavaScript · SQL Server · Azure'],
        ['Arquitectura', 'MVC en capas (Presentation · Business Logic · Data Access)'],
        ['Metodología', 'Agile / Scrum'],
        ['Equipo', 'Samanta Rojas, Killiam García, Jonnathan Rey, Santiago Cuervo (4 integrantes)'],
    ]
)
doc.add_page_break()

# === 1. CONTEXTO ===
add_h1('1. Contexto y Objetivos')

add_h2('1.1 Objetivo General')
add_p('Desarrollar una API REST que centralice y digitalice el proceso de publicación, búsqueda y seguimiento de adopciones de mascotas, conectando de forma ágil y trazable a fundaciones de rescate animal con potenciales adoptantes, sustituyendo la gestión desorganizada actual basada en redes sociales.')

add_h2('1.2 Objetivos Específicos')
add_table(
    ['ID', 'Objetivo'],
    [
        ['OE-01', 'Diseñar y documentar una API REST bajo Swagger para registrar, consultar y actualizar fichas de mascotas'],
        ['OE-02', 'Implementar filtrado de mascotas por especie, edad, tamaño y ciudad'],
        ['OE-03', 'Desarrollar un flujo de solicitud de adopción con estados trazables (pendiente, en revisión, aprobada, rechazada, completada)'],
        ['OE-04', 'Generar reportes para que las fundaciones visualicen mascotas disponibles vs. adoptadas'],
        ['OE-05', 'Proveer Swagger UI para pruebas en vivo y, opcionalmente, un SDK generado con Swagger Codegen'],
    ]
)

add_h2('1.3 Descripción del Problema')
add_p('En Colombia, cerca del 58% de los hogares tiene al menos una mascota, pero la red de rescate es informal y atomizada (fundaciones, colectivos y hogares de paso). La información sobre animales disponibles queda dispersa en redes sociales (Instagram, Facebook, hashtags), sin control centralizado ni actualización automática de estados.')
add_p('Problemas identificados:')
add_bullet('Dispersión informativa — el adoptante debe revisar decenas de perfiles y grupos.')
add_bullet('Falta de confianza — no existe un registro verificable de rescatistas legítimos.')
add_bullet('Proceso lento e intrazable — las solicitudes se gestionan por mensajes privados, saturando refugios y hogares de paso.')

doc.add_page_break()

# === 2. ALCANCE ===
add_h1('2. Alcance')

add_h2('2.1 Incluye')
for item in [
    'API REST con endpoints para usuarios, mascotas, solicitudes y reportes',
    'Autenticación básica por rol (fundación / adoptante)',
    'Filtros de búsqueda (especie, edad, tamaño, ciudad, estado)',
    'Documentación interactiva con Swagger UI',
    'Modelo de datos relacional en SQL Server',
    'Interfaz web MVC como cliente de la API',
    'Mockups navegables en Figma',
]:
    add_bullet(item)

add_h2('2.2 No incluye')
for item in [
    'Pasarela de pagos o donaciones',
    'Notificaciones push en tiempo real',
    'Aplicación móvil nativa (solo diseño responsive en mockups)',
    'Verificación legal o judicial del proceso de adopción',
]:
    add_bullet(item)

doc.add_page_break()

# === 3. ÉPICAS ===
add_h1('3. Épicas y Módulos')

add_table(
    ['Épica', 'Módulo', 'Descripción', 'Prioridad', 'Sprint'],
    [
        ['E-01', 'Autenticación y Usuarios', 'Registro, login y gestión de roles (fundación / adoptante)', 'Alta', 'Sprint 1'],
        ['E-02', 'Gestión de Mascotas', 'CRUD de fichas de mascotas con filtros de búsqueda avanzada', 'Alta', 'Sprint 1'],
        ['E-03', 'Solicitudes de Adopción', 'Flujo completo con máquina de estados trazable', 'Alta', 'Sprint 2'],
        ['E-04', 'Reportes e Impacto', 'Dashboard de métricas para fundaciones', 'Media', 'Sprint 2'],
        ['E-05', 'Documentación API', 'Swagger UI, OpenAPI spec y pruebas interactivas', 'Media', 'Sprint 3'],
        ['E-06', 'Interfaz Web y UX', 'Vistas MVC + mockups navegables en Figma', 'Media', 'Sprint 1–3'],
    ]
)

add_h3('Desglose por módulo')
add_code("""E-01 Autenticación
 ├── Registro de fundaciones
 ├── Registro de adoptantes
 ├── Login con JWT
 └── Autorización por rol

E-02 Mascotas
 ├── Publicar ficha de mascota
 ├── Consultar listado con filtros
 ├── Ver detalle de mascota
 └── Actualizar / eliminar ficha

E-03 Solicitudes
 ├── Crear solicitud de adopción
 ├── Consultar solicitudes (adoptante / fundación)
 ├── Cambiar estado de solicitud
 └── Rechazo automático de solicitudes concurrentes

E-04 Reportes
 ├── Total mascotas por estado
 ├── Adopciones completadas por periodo
 └── Impacto general de la fundación

E-05 Documentación
 ├── Configuración Swashbuckle
 ├── Anotaciones XML en controllers
 └── Pruebas interactivas en Swagger UI

E-06 Interfaz Web
 ├── Página de inicio y listado
 ├── Detalle de mascota
 ├── Formulario de solicitud
 ├── Panel de fundación
 └── Mockups Figma navegables""")

doc.add_page_break()

# === 4. HISTORIAS DE USUARIO ===
add_h1('4. Historias de Usuario')

stories = [
    ('Módulo E-01 — Autenticación y Usuarios', [
        ('HU-01 — Registro de fundación',
         'Como fundación de rescate animal, quiero registrarme con los datos de mi organización, para poder publicar mascotas en la plataforma.',
         ['El formulario exige: nombre, email, contraseña, ciudad, nombre de organización',
          'El email debe ser único en el sistema',
          'La contraseña se almacena hasheada (BCrypt / Identity)',
          'Al registrarse, el tipo de usuario queda como Fundacion',
          'Retorna HTTP 201 con datos del usuario (sin contraseña)']),
        ('HU-02 — Registro de adoptante',
         'Como persona interesada en adoptar, quiero registrarme en la plataforma, para poder enviar solicitudes de adopción.',
         ['El formulario exige: nombre, email, contraseña, ciudad',
          'El email debe ser único en el sistema',
          'Al registrarse, el tipo de usuario queda como Adoptante',
          'Retorna HTTP 201 con datos del usuario']),
        ('HU-03 — Inicio de sesión',
         'Como usuario registrado, quiero iniciar sesión con email y contraseña, para acceder a las funcionalidades según mi rol.',
         ['Credenciales válidas retornan un token JWT con expiración configurable',
          'El token incluye claims: userId, email, rol',
          'Credenciales inválidas retornan HTTP 401',
          'Endpoints protegidos rechazan peticiones sin token o con token expirado']),
    ]),
    ('Módulo E-02 — Gestión de Mascotas', [
        ('HU-04 — Publicar mascota',
         'Como fundación autenticada, quiero publicar una ficha de mascota, para que los adoptantes puedan encontrarla.',
         ['Campos obligatorios: nombre, especie, edad (meses), tamaño, ciudad, descripción',
          'Campos opcionales: raza, URL de foto',
          'Estado inicial: Disponible',
          'Solo usuarios con rol Fundacion pueden crear mascotas',
          'Retorna HTTP 201 con la ficha creada']),
        ('HU-05 — Buscar mascotas con filtros',
         'Como adoptante (o visitante), quiero buscar mascotas aplicando filtros, para encontrar la que mejor se adapte a mis condiciones.',
         ['Filtros disponibles: especie, edad (rango), tamaño, ciudad, estado',
          'Todos los filtros son opcionales y combinables',
          'Resultados paginados (page, pageSize)',
          'Endpoint público, no requiere autenticación',
          'Retorna lista con: id, nombre, especie, edad, tamaño, ciudad, foto, estado']),
        ('HU-06 — Actualizar o eliminar mascota',
         'Como fundación, quiero editar o eliminar las fichas que publiqué, para mantener la información actualizada.',
         ['Solo la fundación propietaria puede modificar o eliminar la ficha',
          'No se puede eliminar una mascota con solicitudes en estado EnRevision o Aprobada',
          'Al eliminar, las solicitudes pendientes se rechazan automáticamente',
          'Retorna HTTP 200 (update) o HTTP 204 (delete)']),
        ('HU-07 — Ver detalle de mascota',
         'Como adoptante, quiero ver la información completa de una mascota, para decidir si deseo solicitar su adopción.',
         ['Muestra todos los campos de la ficha',
          'Incluye datos básicos de la fundación (nombre, ciudad)',
          'Endpoint público',
          'Retorna HTTP 404 si la mascota no existe']),
    ]),
    ('Módulo E-03 — Solicitudes de Adopción', [
        ('HU-08 — Enviar solicitud de adopción',
         'Como adoptante autenticado, quiero enviar una solicitud de adopción para una mascota, para iniciar el proceso formal.',
         ['Estado inicial de la solicitud: Pendiente',
          'Solo se puede solicitar una mascota en estado Disponible',
          'Un adoptante no puede tener más de una solicitud activa para la misma mascota',
          'Al crear la solicitud, la mascota pasa a estado EnProceso',
          'Campo opcional: mensaje al rescatista',
          'Retorna HTTP 201 con la solicitud creada']),
        ('HU-09 — Gestionar solicitudes (fundación)',
         'Como fundación, quiero revisar y cambiar el estado de las solicitudes recibidas, para gestionar el proceso de adopción.',
         ['Transiciones válidas: Pendiente → EnRevision → Aprobada | Rechazada → Completada',
          'Solo la fundación dueña de la mascota puede cambiar el estado',
          'Al aprobar: la mascota pasa a Adoptada; las demás solicitudes activas se rechazan automáticamente',
          'Al rechazar: si no quedan solicitudes activas, la mascota vuelve a Disponible',
          'Transiciones inválidas retornan HTTP 422 con mensaje descriptivo']),
        ('HU-10 — Consultar mis solicitudes (adoptante)',
         'Como adoptante, quiero ver el estado de todas mis solicitudes, para hacer seguimiento del proceso.',
         ['Lista solo las solicitudes del adoptante autenticado',
          'Muestra: mascota, fundación, estado, fecha de solicitud, fecha de última actualización',
          'Ordenadas por fecha descendente',
          'Retorna lista vacía (no error) si no hay solicitudes']),
    ]),
    ('Módulo E-04 — Reportes', [
        ('HU-11 — Reporte de impacto (fundación)',
         'Como fundación, quiero ver un reporte del estado de mis mascotas, para medir mi impacto en adopciones.',
         ['Muestra totales: disponibles, en proceso, adoptadas',
          'Muestra adopciones completadas en un rango de fechas',
          'Solo accesible por la fundación autenticada (sus propios datos)',
          'Retorna JSON estructurado listo para visualización']),
    ]),
    ('Módulo E-05 — Documentación API', [
        ('HU-12 — Probar la API desde Swagger UI',
         'Como desarrollador o evaluador, quiero probar todos los endpoints desde Swagger UI, para validar el comportamiento de la API sin herramientas externas.',
         ['Swagger UI accesible en /swagger',
          'Todos los endpoints documentados con descripción, parámetros y respuestas',
          'Autenticación JWT configurable desde la interfaz de Swagger',
          'OpenAPI 3.0 spec exportable en JSON/YAML']),
    ]),
    ('Módulo E-06 — Interfaz Web', [
        ('HU-13 — Navegar mockups en Figma',
         'Como stakeholder del proyecto, quiero revisar mockups navegables del flujo completo, para validar la experiencia de usuario antes del desarrollo.',
         ['Mockups cubren: inicio, listado, detalle, login, registro, solicitud, panel fundación',
          'Diseño responsive (desktop + mobile)',
          'Flujo navegable entre pantallas principales',
          'Link compartido accesible para el equipo y evaluadores']),
    ]),
]

for module_name, hus in stories:
    add_h2(module_name)
    for hu_title, hu_story, criteria in hus:
        add_h3(hu_title)
        add_p(hu_story, bold=False)
        add_p('Criterios de aceptación:', bold=True)
        for c in criteria:
            add_bullet(c)
        doc.add_paragraph()

doc.add_page_break()

# === 5. TAREAS ===
add_h1('5. Tareas Detalladas')

add_h2('Sprint 0 — Configuración inicial (Semana 1)')
add_table(
    ['ID', 'Tarea', 'Épica', 'Responsable', 'Estimación'],
    [
        ['T-01', 'Crear solución .NET 8 con proyectos: Web, Api, Business, Data, Shared', '—', 'Backend', '4h'],
        ['T-02', 'Configurar EF Core + cadena de conexión SQL Server', 'E-02', 'Backend', '3h'],
        ['T-03', 'Crear entidades y migración inicial', 'E-02', 'Backend', '4h'],
        ['T-04', 'Configurar Swashbuckle (Swagger) en proyecto Api', 'E-05', 'Backend', '2h'],
        ['T-05', 'Inicializar repositorio Git + README + .gitignore', '—', 'Todos', '1h'],
        ['T-06', 'Crear estructura de mockups en Figma (wireframes base)', 'E-06', 'Frontend/UX', '6h'],
    ]
)

add_h2('Sprint 1 — Autenticación + Mascotas (Semanas 2–3)')
add_table(
    ['ID', 'Tarea', 'Historia', 'Detalle técnico', 'Est.'],
    [
        ['T-07', 'Implementar AuthService + AuthController', 'HU-01, HU-02, HU-03', 'Registro, login, JWT con claims de rol', '8h'],
        ['T-08', 'Middleware de autorización por rol', 'HU-03', '[Authorize(Roles = "Fundacion")]', '3h'],
        ['T-09', 'Implementar MascotaService + MascotasController', 'HU-04, HU-06', 'CRUD completo con validación de propiedad', '8h'],
        ['T-10', 'Implementar filtros y paginación en GET /mascotas', 'HU-05', 'Query params + LINQ dinámico', '5h'],
        ['T-11', 'Endpoint GET /mascotas/{id}', 'HU-07', 'Incluir datos de fundación', '2h'],
        ['T-12', 'Vistas MVC: Home, Listado, Detalle', 'HU-05, HU-07', 'Razor + fetch API', '10h'],
        ['T-13', 'Vistas MVC: Login y Registro', 'HU-01, HU-02, HU-03', 'Formularios + manejo de token', '6h'],
        ['T-14', 'Elaborar diagrama de Casos de Uso', '—', 'Exportar a docs/diagrams/', '3h'],
        ['T-15', 'Elaborar diagrama de Clases', '—', 'Exportar a docs/diagrams/', '4h'],
    ]
)

add_h2('Sprint 2 — Solicitudes + Reportes (Semanas 4–5)')
add_table(
    ['ID', 'Tarea', 'Historia', 'Detalle técnico', 'Est.'],
    [
        ['T-16', 'Implementar SolicitudService con máquina de estados', 'HU-08, HU-09', 'Validar transiciones, rechazo automático', '10h'],
        ['T-17', 'Implementar SolicitudesController', 'HU-08, HU-09, HU-10', 'POST, GET, PUT estado', '6h'],
        ['T-18', 'Lógica de cambio de estado de mascota al aprobar/rechazar', 'HU-09', 'Transacción atómica en BD', '4h'],
        ['T-19', 'Implementar ReporteService + ReportesController', 'HU-11', 'Agregaciones LINQ por fundación', '5h'],
        ['T-20', 'Vista MVC: formulario de solicitud', 'HU-08', 'Modal o página dedicada', '4h'],
        ['T-21', 'Vista MVC: panel de fundación (solicitudes + reporte)', 'HU-09, HU-11', 'Dashboard con tabs', '10h'],
        ['T-22', 'Vista MVC: mis solicitudes (adoptante)', 'HU-10', 'Listado con badges de estado', '4h'],
        ['T-23', 'Elaborar diagrama de Secuencia', '—', 'Flujo solicitud de adopción', '3h'],
        ['T-24', 'Elaborar diagrama de Componentes', '—', 'Arquitectura en capas', '4h'],
    ]
)

add_h2('Sprint 3 — Documentación + Despliegue (Semana 6)')
add_table(
    ['ID', 'Tarea', 'Historia', 'Detalle técnico', 'Est.'],
    [
        ['T-25', 'Completar anotaciones XML en todos los controllers', 'HU-12', 'Summary, params, responses', '4h'],
        ['T-26', 'Pruebas unitarias (Services)', '—', 'xUnit + Moq', '8h'],
        ['T-27', 'Pruebas de integración (Controllers)', '—', 'WebApplicationFactory', '6h'],
        ['T-28', 'Finalizar mockups Figma navegables', 'HU-13', 'Flujo completo + responsive', '8h'],
        ['T-29', 'Despliegue en Azure App Service + SQL Azure', '—', 'CI/CD básico con GitHub Actions', '6h'],
        ['T-30', 'Demo final + documentación README', '—', 'Instrucciones de setup y uso', '3h'],
    ]
)

doc.add_page_break()

# === 6. MODELO DE DATOS ===
add_h1('6. Modelo de Datos')

add_h2('6.1 Entidades principales')
add_table(
    ['Entidad', 'Campos clave', 'Relaciones'],
    [
        ['USUARIO', 'Id, Nombre, Email (UK), PasswordHash, TipoUsuario, Ciudad, FechaRegistro, Activo', '1:0..1 con FUNDACION; 1:N con SOLICITUD_ADOPCION'],
        ['FUNDACION', 'Id, UsuarioId (FK UK), NombreOrganizacion, Descripcion, Telefono, Verificada', '1:N con MASCOTA'],
        ['MASCOTA', 'Id, FundacionId (FK), Nombre, Especie, Raza, EdadMeses, Tamano, Ciudad, Descripcion, FotoUrl, Estado, FechaPublicacion', '1:N con SOLICITUD_ADOPCION'],
        ['SOLICITUD_ADOPCION', 'Id, MascotaId (FK), AdoptanteId (FK), Estado, Mensaje, FechaSolicitud, FechaActualizacion', 'N:1 con MASCOTA y USUARIO'],
    ]
)

add_h2('6.2 Enumeraciones')
add_code("""TipoUsuario       { Fundacion, Adoptante }
TamanoMascota     { Pequeno, Mediano, Grande }
EstadoMascota     { Disponible, EnProceso, Adoptada }
EstadoSolicitud   { Pendiente, EnRevision, Aprobada, Rechazada, Completada }""")

add_h2('6.3 Reglas de negocio')
add_table(
    ['Regla', 'Descripción'],
    [
        ['RN-01', 'Un usuario de tipo Fundacion tiene exactamente un registro en FUNDACION'],
        ['RN-02', 'Una mascota solo puede tener una solicitud Aprobada o Completada'],
        ['RN-03', 'Al aprobar una solicitud, las demás activas de la misma mascota pasan a Rechazada'],
        ['RN-04', 'Una mascota Adoptada no acepta nuevas solicitudes'],
        ['RN-05', 'El email de usuario es único en todo el sistema'],
        ['RN-06', 'Índice compuesto en MASCOTA(Especie, Ciudad, Estado) para optimizar búsquedas'],
    ]
)

add_h2('6.4 Máquina de estados — Solicitud de Adopción')
add_code("""[*] → Pendiente          (Adoptante envía solicitud)
Pendiente → EnRevision      (Fundación inicia revisión)
Pendiente → Rechazada       (Fundación rechaza)
EnRevision → Aprobada       (Fundación aprueba)
EnRevision → Rechazada      (Fundación rechaza)
Aprobada → Completada       (Adopción finalizada)
Rechazada → [*]
Completada → [*]""")

doc.add_page_break()

# === 7. CASOS DE USO ===
add_h1('7. Diagrama de Casos de Uso')

add_h2('7.1 Actores')
add_table(
    ['Actor', 'Descripción'],
    [
        ['Adoptante', 'Usuario registrado que busca y solicita adopciones'],
        ['Fundación', 'Organización de rescate que publica mascotas y gestiona solicitudes'],
        ['Visitante', 'Usuario no autenticado que puede buscar y ver mascotas'],
        ['Desarrollador', 'Evalúa y prueba la API via Swagger UI'],
    ]
)

add_h2('7.2 Casos de uso por módulo')
add_table(
    ['Módulo', 'Casos de uso', 'Actor principal'],
    [
        ['Autenticación', 'UC-01 Registrarse adoptante, UC-02 Registrarse fundación, UC-03 Iniciar sesión, UC-04 Cerrar sesión', 'Adoptante / Fundación'],
        ['Mascotas', 'UC-05 Publicar mascota, UC-06 Buscar con filtros, UC-07 Ver detalle, UC-08 Actualizar, UC-09 Eliminar', 'Fundación / Visitante'],
        ['Adopción', 'UC-10 Enviar solicitud, UC-11 Consultar mis solicitudes, UC-12 Revisar solicitudes, UC-13 Cambiar estado', 'Adoptante / Fundación'],
        ['Reportes', 'UC-14 Ver reporte de impacto', 'Fundación'],
        ['Documentación', 'UC-15 Probar endpoints en Swagger UI', 'Desarrollador'],
    ]
)

add_h2('7.3 Descripción de casos de uso principales')
add_table(
    ['Caso de uso', 'Actor', 'Precondición', 'Flujo principal', 'Postcondición'],
    [
        ['UC-10 Enviar solicitud', 'Adoptante', 'Autenticado; mascota Disponible', '1. Selecciona mascota → 2. Escribe mensaje → 3. Confirma → 4. Sistema crea solicitud Pendiente y mascota pasa a EnProceso', 'Solicitud registrada'],
        ['UC-13 Cambiar estado', 'Fundación', 'Solicitud existe y pertenece a su mascota', '1. Selecciona solicitud → 2. Elige nuevo estado → 3. Sistema valida transición → 4. Actualiza solicitud y mascota', 'Estado actualizado'],
        ['UC-06 Buscar mascotas', 'Visitante/Adoptante', 'Ninguna', '1. Aplica filtros → 2. Sistema consulta BD → 3. Retorna resultados paginados', 'Listado mostrado'],
    ]
)

add_h2('7.4 Relaciones entre casos de uso')
add_bullet('UC-10 (Enviar solicitud) incluye UC-07 (Ver detalle de mascota)')
add_bullet('UC-13 (Cambiar estado) extiende UC-12 (Revisar solicitudes recibidas)')
add_bullet('UC-08 (Actualizar ficha) incluye UC-05 (Publicar mascota)')

doc.add_page_break()

# === 8. CLASES ===
add_h1('8. Diagrama de Clases')

add_h2('8.1 Clases de dominio (Entidades)')
add_table(
    ['Clase', 'Atributos principales', 'Relaciones'],
    [
        ['Usuario', 'Id, Nombre, Email, PasswordHash, Tipo, Ciudad, FechaRegistro, Activo', '1 → 0..1 Fundacion; 1 → * SolicitudAdopcion'],
        ['Fundacion', 'Id, UsuarioId, NombreOrganizacion, Descripcion, Telefono, Verificada', '1 → * Mascota'],
        ['Mascota', 'Id, FundacionId, Nombre, Especie, Raza, EdadMeses, Tamano, Ciudad, Descripcion, FotoUrl, Estado', '1 → * SolicitudAdopcion'],
        ['SolicitudAdopcion', 'Id, MascotaId, AdoptanteId, Estado, Mensaje, FechaSolicitud, FechaActualizacion', 'N → 1 Mascota; N → 1 Usuario'],
    ]
)

add_h2('8.2 Interfaces de servicio (Capa Business)')
add_table(
    ['Interface', 'Métodos principales'],
    [
        ['IAuthService', 'RegisterAsync(dto), LoginAsync(dto), GetByIdAsync(id)'],
        ['IMascotaService', 'CreateAsync(dto, fundacionId), GetByFiltersAsync(filters), GetByIdAsync(id), UpdateAsync(id, dto, fundacionId), DeleteAsync(id, fundacionId)'],
        ['ISolicitudService', 'CreateAsync(dto, adoptanteId), ChangeStatusAsync(id, estado, fundacionId), GetByAdoptanteAsync(id), GetByFundacionAsync(id)'],
        ['IReporteService', 'GetReporteAsync(fundacionId, desde, hasta)'],
    ]
)

add_h2('8.3 Implementaciones de servicio')
add_table(
    ['Clase', 'Dependencias', 'Responsabilidad clave'],
    [
        ['AuthService', 'IUsuarioRepository, IPasswordHasher, ITokenGenerator', 'Registro, login, generación JWT'],
        ['MascotaService', 'IMascotaRepository, IMapper', 'CRUD mascotas, filtros, validación de propiedad'],
        ['SolicitudService', 'ISolicitudRepository, IMascotaRepository', 'Máquina de estados, rechazo concurrente, transacciones'],
        ['ReporteService', 'IMascotaRepository, ISolicitudRepository', 'Agregaciones y métricas por fundación'],
    ]
)

add_h2('8.4 DTOs principales')
add_table(
    ['DTO', 'Campos'],
    [
        ['RegisterDto', 'Nombre, Email, Password, Ciudad, Tipo, NombreOrganizacion'],
        ['MascotaFilterDto', 'Especie, EdadMin, EdadMax, Tamano, Ciudad, Estado, Page, PageSize'],
        ['CreateSolicitudDto', 'MascotaId, Mensaje'],
        ['ReporteFundacionDto', 'TotalDisponibles, TotalEnProceso, TotalAdoptadas, AdopcionesCompletadasPeriodo'],
        ['AuthResponseDto', 'Token, Usuario'],
    ]
)

doc.add_page_break()

# === 9. SECUENCIA ===
add_h1('9. Diagrama de Secuencia')

add_h2('9.1 Flujo: Solicitud de adopción (Adoptante)')
add_p('Actores: Adoptante → MVC+JS → API Controller → SolicitudService → Repositories → SQL Server')
for step in [
    '1. Adoptante selecciona mascota y completa formulario',
    '2. Web envía POST /api/solicitudes { mascotaId, mensaje } con JWT',
    '3. API valida token y rol Adoptante',
    '4. SolicitudService verifica que la mascota esté en estado Disponible',
    '5. SolicitudService verifica que no exista solicitud activa del mismo adoptante',
    '6. Se crea SolicitudAdopcion con estado Pendiente',
    '7. Se actualiza Mascota a estado EnProceso',
    '8. API retorna 201 Created con SolicitudDto',
]:
    add_bullet(step)

add_h2('9.2 Flujo: Fundación aprueba solicitud')
add_p('Actores: Fundación → MVC+JS → API Controller → SolicitudService → Repositories → SQL Server')
for step in [
    '1. Fundación selecciona solicitud y elige estado Aprobada',
    '2. Web envía PUT /api/solicitudes/{id}/estado { estado: "Aprobada" }',
    '3. API valida token y rol Fundacion',
    '4. SolicitudService valida transición EnRevision → Aprobada',
    '5. SolicitudService valida que la mascota pertenezca a la fundación',
    '6. Se actualiza solicitud a Aprobada',
    '7. Se rechazan automáticamente todas las demás solicitudes activas de la mascota',
    '8. Se actualiza Mascota a estado Adoptada',
    '9. API retorna 200 OK (transacción atómica)',
]:
    add_bullet(step)

add_h2('9.3 Flujo: Búsqueda pública de mascotas')
add_p('Actores: Visitante → MVC+JS → MascotasController → MascotaService → MascotaRepository → SQL Server')
for step in [
    '1. Visitante aplica filtros (especie=Perro, ciudad=Bogotá)',
    '2. Web envía GET /api/mascotas?especie=Perro&ciudad=Bogotá&page=1&pageSize=10',
    '3. MascotaService ejecuta consulta con filtros dinámicos y paginación',
    '4. Repository ejecuta SELECT con OFFSET/FETCH en SQL Server',
    '5. API retorna 200 OK { items[], totalCount, page, pageSize }',
    '6. Web renderiza tarjetas de mascotas con paginación',
]:
    add_bullet(step)

doc.add_page_break()

# === 10. COMPONENTES ===
add_h1('10. Diagrama de Componentes')

add_h2('10.1 Capas de la arquitectura')
add_table(
    ['Capa', 'Componentes', 'Responsabilidad'],
    [
        ['Presentación', 'AdoptaAPI.Web (MVC), JavaScript (fetch), Figma Mockups', 'Interfaz de usuario, consumo de API REST'],
        ['API', 'AuthController, MascotasController, SolicitudesController, ReportesController, Swagger UI, JWT Middleware', 'Exposición de endpoints REST, autenticación'],
        ['Business Logic', 'AuthService, MascotaService, SolicitudService, ReporteService, Validators, AutoMapper', 'Reglas de negocio, validaciones, mapeo DTOs'],
        ['Data Access', 'UsuarioRepository, MascotaRepository, SolicitudRepository, AdoptaDbContext (EF Core 8)', 'Persistencia, consultas, migraciones'],
        ['Storage', 'Azure SQL Database (SQL Server)', 'Almacenamiento relacional'],
        ['Cloud', 'Azure App Service, Azure Key Vault', 'Hosting y gestión de secretos'],
    ]
)

add_h2('10.2 Descripción de componentes')
add_table(
    ['Componente', 'Proyecto', 'Responsabilidad'],
    [
        ['AdoptaAPI.Web', 'Presentation', 'Vistas Razor, assets estáticos, cliente JS que consume la API'],
        ['AdoptaAPI.Api', 'Presentation', 'Controllers REST, middleware JWT, configuración Swagger'],
        ['AuthService', 'Business', 'Registro, login, generación y validación de JWT'],
        ['MascotaService', 'Business', 'CRUD de mascotas, filtros, validación de propiedad'],
        ['SolicitudService', 'Business', 'Máquina de estados, rechazo concurrente, transacciones'],
        ['ReporteService', 'Business', 'Agregaciones y métricas por fundación'],
        ['Repositories', 'Data', 'Abstracción de acceso a datos con EF Core'],
        ['AdoptaDbContext', 'Data', 'Mapeo ORM, migraciones, configuración de entidades'],
        ['Validators', 'Business', 'Reglas de validación de DTOs (FluentValidation)'],
        ['AutoMapper Profiles', 'Business', 'Mapeo Entity ↔ DTO'],
        ['Azure SQL Database', 'Storage', 'Persistencia relacional'],
        ['Azure App Service', 'Cloud', 'Hosting de Web + API'],
    ]
)

add_h2('10.3 Interfaces entre capas')
add_p('Contratos HTTP (API REST):')
add_table(
    ['Endpoint', 'Servicio interno'],
    [
        ['POST /api/auth/register', 'IAuthService.RegisterAsync'],
        ['POST /api/auth/login', 'IAuthService.LoginAsync'],
        ['GET /api/mascotas', 'IMascotaService.GetByFiltersAsync'],
        ['POST /api/mascotas', 'IMascotaService.CreateAsync'],
        ['POST /api/solicitudes', 'ISolicitudService.CreateAsync'],
        ['PUT /api/solicitudes/{id}/estado', 'ISolicitudService.ChangeStatusAsync'],
        ['GET /api/reportes/fundacion', 'IReporteService.GetReporteAsync'],
    ]
)

add_h2('10.4 Flujo de comunicación entre componentes')
add_code("""Navegador → AdoptaAPI.Web (MVC + JS)
    → HTTP REST + JWT → AdoptaAPI.Api (Controllers)
        → AuthService / MascotaService / SolicitudService / ReporteService
            → Validators + AutoMapper
            → Repositories (Usuario, Mascota, Solicitud)
                → AdoptaDbContext (EF Core 8)
                    → Azure SQL Database

Swagger UI → Controllers (pruebas directas sin MVC)
Azure Key Vault → Connection strings + JWT secret""")

add_h2('10.5 Despliegue en Azure')
add_table(
    ['Recurso Azure', 'Función'],
    [
        ['App Service (Web App)', 'Hosting de AdoptaAPI.Web'],
        ['App Service (API App)', 'Hosting de AdoptaAPI.Api + Swagger'],
        ['Azure SQL Database', 'Base de datos AdoptaDB'],
        ['Azure Key Vault', 'Secretos: connection strings, JWT secret'],
    ]
)

doc.add_page_break()

# === 11. TRAZABILIDAD ===
add_h1('11. Matriz de Trazabilidad')

add_table(
    ['Objetivo', 'Épica', 'Historia', 'Tarea(s)', 'Diagrama', 'Entregable'],
    [
        ['OE-01', 'E-05', 'HU-12', 'T-04, T-25', 'Componentes §10', 'Swagger UI + OpenAPI'],
        ['OE-02', 'E-02', 'HU-05', 'T-10', 'Secuencia §9.3', 'GET /api/mascotas con filtros'],
        ['OE-03', 'E-03', 'HU-08, HU-09', 'T-16, T-17, T-18', 'Secuencia §9.1, §9.2', 'Máquina de estados'],
        ['OE-04', 'E-04', 'HU-11', 'T-19', 'Clases §8.2', 'GET /api/reportes/fundacion'],
        ['OE-05', 'E-05, E-06', 'HU-12, HU-13', 'T-25, T-28', 'Componentes §10', 'Swagger + Figma'],
        ['—', 'E-01', 'HU-01–03', 'T-07, T-08, T-13', 'Casos de Uso §7', 'Auth JWT'],
        ['—', 'E-02', 'HU-04, HU-06, HU-07', 'T-09, T-11, T-12', 'Clases §8.1, ER §6', 'CRUD Mascotas'],
        ['—', 'E-03', 'HU-10', 'T-22', 'Secuencia §9.1', 'Vista adoptante'],
        ['—', 'E-06', 'HU-13', 'T-06, T-28', '—', 'Mockups Figma'],
    ]
)

add_h2('Apéndice — Endpoints REST')
add_table(
    ['Método', 'Ruta', 'Auth', 'Rol', 'Historia'],
    [
        ['POST', '/api/auth/register', 'No', '—', 'HU-01, HU-02'],
        ['POST', '/api/auth/login', 'No', '—', 'HU-03'],
        ['GET', '/api/mascotas', 'No', '—', 'HU-05'],
        ['GET', '/api/mascotas/{id}', 'No', '—', 'HU-07'],
        ['POST', '/api/mascotas', 'Sí', 'Fundación', 'HU-04'],
        ['PUT', '/api/mascotas/{id}', 'Sí', 'Fundación', 'HU-06'],
        ['DELETE', '/api/mascotas/{id}', 'Sí', 'Fundación', 'HU-06'],
        ['POST', '/api/solicitudes', 'Sí', 'Adoptante', 'HU-08'],
        ['GET', '/api/solicitudes/mis-solicitudes', 'Sí', 'Adoptante', 'HU-10'],
        ['GET', '/api/solicitudes/fundacion', 'Sí', 'Fundación', 'HU-09'],
        ['PUT', '/api/solicitudes/{id}/estado', 'Sí', 'Fundación', 'HU-09'],
        ['GET', '/api/reportes/fundacion', 'Sí', 'Fundación', 'HU-11'],
    ]
)

# Guardar
doc.save(OUTPUT)
print(f"Documento generado: {OUTPUT}")
