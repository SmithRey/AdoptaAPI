# Investigación: Framework Scrum

**Tema:** Actores, ceremonias y el Sprint en Scrum  
**Marco de referencia:** Scrum Guide (Ken Schwaber y Jeff Sutherland, 2020)

---

## Introducción

Scrum es un marco de trabajo ágil para desarrollar, entregar y sostener productos complejos. No es una metodología rígida ni una receta de pasos fijos: es un conjunto pequeño de reglas que ayuda a un equipo a inspeccionar el trabajo con frecuencia y a adaptarse cuando cambia el contexto.

Scrum se sostiene en tres pilares:

- **Transparencia:** el trabajo y el progreso deben ser visibles para quienes toman decisiones.
- **Inspección:** el equipo revisa el producto y el proceso en intervalos cortos.
- **Adaptación:** si algo no está funcionando, se ajusta de inmediato.

También se apoya en cinco valores: **compromiso, foco, apertura, respeto y coraje**.

Esta investigación cubre cuatro puntos: los actores de Scrum, las ceremonias, las características principales de un Sprint y la forma en que se realiza un Sprint.

---

## 1. Actores de Scrum

En Scrum hay un solo equipo, llamado **Scrum Team**. Ese equipo es pequeño (por lo general 10 personas o menos), autoorganizado y multifuncional: tiene las habilidades necesarias para entregar valor sin depender de un jefe que asigne cada tarea.

Dentro del Scrum Team existen **tres responsabilidades** (también llamadas actores o roles):

### 1.1 Product Owner (Dueño del Producto)

El Product Owner maximiza el valor del producto. Es la voz del negocio y de los usuarios dentro del equipo.

**Responsabilidades principales:**

- Definir y comunicar el **objetivo del producto** (Product Goal).
- Crear y ordenar el **Product Backlog** (lista priorizada de trabajo).
- Asegurar que los ítems del backlog sean claros, comprensibles y priorizados.
- Decidir qué se entrega y en qué orden, según el valor para el cliente.
- Aceptar o rechazar el resultado de cada Sprint.

El Product Owner es **una sola persona**, no un comité. Puede recibir ideas de muchas partes (cliente, gerencia, usuarios), pero la decisión final sobre el backlog es suya.

### 1.2 Scrum Master

El Scrum Master es el encargado de que Scrum se entienda y se aplique bien. No es el jefe del equipo ni un project manager tradicional. Es un **líder de servicio** (servant leader).

**Responsabilidades principales:**

- Ayudar al equipo a autoorganizarse y a enfocarse en el Sprint Goal.
- Facilitar las ceremonias y mantenerlas dentro de su tiempo.
- Eliminar impedimentos (bloqueos técnicos, burocracia, falta de información).
- Proteger al equipo de interrupciones que pongan en riesgo el Sprint.
- Entrenar a la organización para que trabaje de forma ágil.

El Scrum Master sirve a tres lados: al equipo de desarrollo, al Product Owner y a la organización.

### 1.3 Developers (Desarrolladores)

Los Developers son las personas que crean el incremento del producto en cada Sprint. El nombre no se limita a programadores: incluye a quien diseña, prueba, documenta, analiza o construye lo necesario para entregar valor.

**Responsabilidades principales:**

- Crear el **Sprint Backlog** (plan del Sprint).
- Comprometerse con el **Sprint Goal**.
- Entregar un **Incremento** de calidad al final del Sprint.
- Asegurar que el trabajo cumpla la **Definición de Terminado** (Definition of Done).
- Adaptar su plan día a día según lo que vayan aprendiendo.

No hay subroles oficiales dentro de los Developers (no hay “jefe de programadores” ni títulos que fragmenten la responsabilidad). El equipo es colectivo: todos son responsables del resultado.

### 1.4 Actores externos (no pertenecen al Scrum Team)

Aunque no son actores oficiales de Scrum, en la práctica interactúan con el equipo:

| Actor externo | Relación con Scrum |
|---|---|
| Stakeholders / interesados | Cliente, gerencia, usuarios. Participan sobre todo en la Sprint Review. |
| Usuarios finales | Reciben el valor del producto. Sus necesidades alimentan el Product Backlog. |
| Patrocinador o dueño del negocio | Financia el producto y espera resultados. |

---

## 2. Ceremonias de Scrum

En la guía oficial se llaman **eventos**. En muchos cursos se les dice **ceremonias**. Todas son **time-boxed**: tienen una duración máxima. El Sprint es el evento contenedor; las otras cuatro ocurren **dentro** de cada Sprint.

### 2.1 Sprint

Es el corazón de Scrum. Es un ciclo de tiempo fijo (máximo un mes, normalmente 1 o 2 semanas) donde el equipo entrega un incremento usable del producto. Las demás ceremonias ocurren dentro de él.

### 2.2 Sprint Planning (Planificación del Sprint)

Se realiza al **inicio** del Sprint. El equipo responde tres preguntas:

1. **¿Por qué este Sprint es valioso?** Se define el **Sprint Goal**.
2. **¿Qué se puede hacer en este Sprint?** Se seleccionan ítems del Product Backlog.
3. **¿Cómo se va a realizar el trabajo?** Los Developers desglosan el trabajo en tareas.

**Duración máxima:** 8 horas para un Sprint de un mes (proporcionalmente menos si el Sprint es más corto).

**Participan:** Product Owner, Scrum Master y Developers. Pueden invitarse expertos si hace falta.

**Resultado:** Sprint Goal + Sprint Backlog.

### 2.3 Daily Scrum (Daily / Scrum Diario)

Reunión diaria de **15 minutos** para los Developers. Sirve para inspeccionar el progreso hacia el Sprint Goal y ajustar el plan de las próximas 24 horas.

No es un reporte al Scrum Master. El equipo se sincroniza entre sí. Una forma clásica (ya no obligatoria) es responder:

- ¿Qué hice ayer que ayude al Sprint Goal?
- ¿Qué haré hoy?
- ¿Qué impedimentos tengo?

**Participan:** Developers. El Scrum Master se asegura de que ocurra, pero no tiene que dirigirla. El Product Owner puede asistir si el equipo lo considera útil, sin convertirla en una reunión de estatus.

### 2.4 Sprint Review (Revisión del Sprint)

Se realiza al **final** del Sprint. El equipo muestra el incremento a los interesados, recibe feedback y actualiza el Product Backlog si es necesario.

No es una “demo formal de PowerPoint”. Es una sesión de trabajo para inspeccionar el producto y decidir qué sigue.

**Duración máxima:** 4 horas para un Sprint de un mes.

**Participan:** Scrum Team + stakeholders.

### 2.5 Sprint Retrospective (Retrospectiva)

Es la última ceremonia del Sprint. El equipo inspecciona **cómo trabajó** (personas, procesos, herramientas, calidad) y define mejoras concretas para el siguiente Sprint.

**Duración máxima:** 3 horas para un Sprint de un mes.

**Participan:** Scrum Team (Developers, Product Owner y Scrum Master).

Una estructura simple:

1. ¿Qué salió bien?
2. ¿Qué no salió bien?
3. ¿Qué vamos a mejorar en el próximo Sprint?

---

## 3. Características principales de un Sprint

Un Sprint no es “cualquier periodo de trabajo”. Tiene reglas claras:

### 3.1 Tiempo fijo (time-box)

Dura **un mes o menos**. La duración se mantiene estable. Si el equipo elige 2 semanas, todos los Sprints duran 2 semanas. Eso crea ritmo y permite medir la velocidad (velocity) con más confianza.

### 3.2 Empieza inmediatamente después del anterior

No hay “huecos” entre Sprints. Cuando termina uno, empieza el siguiente. El producto avanza en ciclos continuos.

### 3.3 Tiene un objetivo claro: el Sprint Goal

Cada Sprint persigue un propósito único. El Sprint Goal da cohesión: no es una lista suelta de tareas, sino un resultado que el equipo se compromete a lograr.

### 3.4 Produce un Incremento

Al final debe existir un pedazo de producto **usable**, que cumpla la Definition of Done. Aunque no se publique al cliente, debe estar en estado de poder usarse.

### 3.5 Alcance negociable, meta protegida

Durante el Sprint:

- **No se cambia el Sprint Goal.**
- La calidad no baja.
- El alcance (qué ítems se hacen) **sí puede aclararse o renegociarse** entre Product Owner y Developers si aparece información nueva.

Si el Sprint Goal deja de tener sentido (cambio drástico de mercado, decisión de negocio, etc.), el Product Owner puede **cancelar** el Sprint. Es poco frecuente y se considera un evento costoso.

### 3.6 Contiene todo el trabajo necesario

Dentro del Sprint ocurren la planificación, el desarrollo, las dailies, la revisión y la retrospectiva. También se incluye el trabajo de calidad: pruebas, integración, documentación mínima necesaria, etc.

### 3.7 Ritmo sostenible

Scrum busca un ritmo que el equipo pueda mantener indefinidamente. No se trata de “echar horas extra cada dos semanas”, sino de entregar valor de forma constante.

### Resumen de características

| Característica | Qué significa |
|---|---|
| Time-box | Máximo 1 mes; duración constante |
| Continuidad | Un Sprint empieza al terminar el anterior |
| Sprint Goal | Un objetivo de negocio/producto por ciclo |
| Incremento | Resultado usable y “Done” |
| Inspección y adaptación | Ceremonias para revisar producto y proceso |
| Flexibilidad controlada | Se puede ajustar el alcance, no el objetivo |
| Calidad fija | La Definition of Done no se relaja para “acabar más” |

---

## 4. Cómo se realiza un Sprint

Un Sprint se recorre en un orden lógico. El siguiente flujo es el ciclo completo:

### Paso 1. Antes del Sprint: Product Backlog listo

El Product Owner mantiene el backlog ordenado. Los ítems de mayor prioridad deben estar lo bastante claros para poder planificarse. Esto se conoce como **Product Backlog Refinement** (refinamiento). No es una ceremonia oficial con hora fija, pero es un trabajo continuo.

Cada ítem debería tener, al menos:

- Descripción
- Criterios de aceptación
- Estimación (puntos de historia, t-shirt sizing, etc., si el equipo los usa)
- Prioridad

### Paso 2. Sprint Planning

1. El Product Owner presenta el objetivo del producto y los ítems más valiosos.
2. El equipo define el **Sprint Goal**.
3. Los Developers seleccionan lo que creen que pueden completar.
4. Descomponen el trabajo (tareas técnicas, pruebas, diseño, etc.).
5. Queda formado el **Sprint Backlog**: Sprint Goal + ítems seleccionados + plan para entregarlos.

### Paso 3. Ejecución del Sprint (trabajo diario)

Durante los días del Sprint:

- Los Developers construyen el incremento.
- Cada día se hace el **Daily Scrum** (15 min).
- El tablero (Kanban/Scrum board) se actualiza: Por hacer / En progreso / Terminado.
- Si aparece un impedimento, se escala al Scrum Master.
- Si el alcance cambia, Product Owner y Developers renegocian sin romper el Sprint Goal.

Buenas prácticas durante la ejecución:

- Trabajar en ítems pequeños y terminar uno antes de abrir demasiados.
- Integrar y probar de forma continua.
- No aceptar trabajo extra “por debajo de la mesa” que no esté en el Sprint Backlog.
- Mantener visible el progreso (burndown, tablero, Sprint Goal en la pared o en el chat del equipo).

### Paso 4. Sprint Review

1. Se muestra el incremento funcionando (no solo capturas o diapositivas).
2. Se conversa con los stakeholders: ¿esto genera valor?, ¿qué falta?, ¿qué cambió en el mercado?
3. Se actualiza el Product Backlog con lo aprendido.
4. Se decide, de forma preliminar, hacia dónde va el siguiente Sprint.

### Paso 5. Sprint Retrospective

1. El equipo analiza el proceso, no para culpar a nadie.
2. Elige **una o dos mejoras reales** (no una lista enorme que nadie cumplirá).
3. Esas mejoras pueden entrar al siguiente Sprint Backlog.

### Paso 6. Cierre e inicio del siguiente Sprint

El Incremento queda potencialmente entregable. El Product Owner decide si se libera a producción. Inmediatamente después comienza el siguiente Sprint Planning.

### Diagrama del flujo

```
Product Backlog
        │
        ▼
 Sprint Planning  ──►  Sprint Goal + Sprint Backlog
        │
        ▼
 Trabajo diario + Daily Scrum (cada 24 h)
        │
        ▼
 Sprint Review  ──►  Incremento inspeccionado + backlog actualizado
        │
        ▼
 Sprint Retrospective  ──►  mejoras para el próximo ciclo
        │
        ▼
 Siguiente Sprint (sin pausa)
```

### Artefactos que se usan durante el Sprint

Scrum tiene tres artefactos, cada uno con un compromiso:

| Artefacto | Compromiso | Para qué sirve |
|---|---|---|
| Product Backlog | Product Goal | Qué se quiere lograr con el producto a largo plazo |
| Sprint Backlog | Sprint Goal | Qué se hará en este ciclo y por qué |
| Incremento | Definition of Done | Qué significa “terminado” de verdad |

---

## Conclusión

Scrum organiza el trabajo alrededor de un equipo pequeño con tres actores (Product Owner, Scrum Master y Developers), cinco eventos o ceremonias (Sprint, Planning, Daily, Review y Retrospectiva) y un ciclo corto llamado Sprint.

El Sprint es la unidad de progreso: tiene tiempo fijo, un objetivo, un incremento usable y espacio para inspeccionar tanto el producto como la forma de trabajar. Se realiza siempre igual: se planifica, se construye día a día, se muestra el resultado y se mejora el proceso antes de empezar el siguiente ciclo.

Esa repetición es lo que permite adaptarse sin perder disciplina.

---

## Referencias

1. Schwaber, K. y Sutherland, J. (2020). *The Scrum Guide*. https://scrumguides.org
2. Schwaber, K. y Sutherland, J. (2020). *La Guía de Scrum* (traducción oficial). https://scrumguides.org
3. Sutherland, J. (2014). *Scrum: The Art of Doing Twice the Work in Half the Time*. Crown Business.
4. Rubin, K. S. (2012). *Essential Scrum: A Practical Guide to the Most Popular Agile Process*. Addison-Wesley.
5. Schwaber, K. (2004). *Agile Project Management with Scrum*. Microsoft Press.
