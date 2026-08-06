# Diseño y Evaluación de una API REST en el Dominio de Pagos

En el dominio de los pagos fintech, el sistema debe exponer una API REST que permita a los clientes consultar el estado de sus transacciones. La API debe manejar solicitudes de tres canales distintos: web, móvil y API externa. El sistema debe garantizar la idempotencia de las solicitudes y persistir cada solicitud con una clave única. Ante reintentos con la misma clave dentro de 24 horas, la API debe devolver la misma respuesta. Además, debe emitir un evento al sistema de auditoría por cada aceptación de solicitud.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | API REST con FastAPI y SQLAlchemy |
| **Nivel** | junior-l1 |
| **Tipo** | theoretical |
| **Tiempo estimado** | 2 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Exploración del Sistema

**Objetivo:** Identificar las restricciones y ambigüedades del sistema de pagos.

**Tiempo estimado:** 30 minutos

**Instrucciones:**

- Enumera los canales de entrada y sus características.
- Identifica las restricciones del sistema, como el throughput máximo y el SLA requerido.
- Determina las ambigüedades que podrían afectar la implementación de la API.

**Entregable:** Lista de restricciones y ambigüedades identificadas.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el impacto de cada restricción en la arquitectura de la API.
- Piensa en cómo las ambigüedades podrían ser resueltas en la implementación.

</details>

### Fase 2: Evaluación de una Decisión Controversial

**Objetivo:** Evaluar una decisión controversial en el diseño de la API y sus trade-offs.

**Tiempo estimado:** 45 minutos

**Instrucciones:**

- Evalúa la decisión de usar una clave única para garantizar la idempotencia de las solicitudes.
- Identifica los pros y contras de esta decisión.
- Determina las consecuencias de implementar esta decisión en el sistema.

**Entregable:** Registro de decisión que incluye contexto, fuerzas, opciones con pros/contras, decisión y consecuencias.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo la idempotencia afecta la consistencia y la disponibilidad del sistema.
- Piensa en los posibles impactos en la latencia y el throughput.

</details>

### Fase 3: Comunicación a Audiencias Distintas

**Objetivo:** Comunicar la decisión tomada a audiencias técnicas y de negocio.

**Tiempo estimado:** 45 minutos

**Instrucciones:**

- Prepara una presentación para una audiencia técnica que incluya los detalles de la implementación de la API.
- Prepara una presentación para una audiencia de negocio que explique los beneficios y riesgos de la decisión tomada.
- Asegura que ambas presentaciones sean claras y permitan a la audiencia tomar decisiones sin pedir aclaraciones.

**Entregable:** Dos presentaciones: una para audiencia técnica y otra para audiencia de negocio.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el lenguaje y los detalles apropiados para cada audiencia.
- Piensa en cómo comunicar los trade-offs y las consecuencias de la decisión.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es la idempotencia y cómo se aplica en el contexto de la API de pagos?
- **paraQueSirve**: ¿Para qué sirve usar una clave única en la API de pagos?
- **comoSeUsa**: ¿Cómo se usa la idempotencia para garantizar la consistencia en la API de pagos?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar la idempotencia en la API de pagos?
- **queDecisionesImplica**: ¿Qué decisiones implica el uso de una clave única para la idempotencia en la API de pagos?

## Criterios de Evaluacion

- Identificación correcta de restricciones y ambigüedades del sistema.
- Evaluación completa de una decisión controversial con pros y contras.
- Comunicación efectiva de la decisión a audiencias técnicas y de negocio.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
