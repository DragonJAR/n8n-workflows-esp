[Version en espanol](https://github.com/DragonJAR/n8n-workflows-esp/blob/main/README.md) | [English Version](https://github.com/DragonJAR/n8n-workflows-esp/blob/main/README-ENGLISH.md)

[Curso gratuito de automatizacion con n8n](https://dragonjar.education/bundle/curso-n8n)

# Coleccion de Flujos de Trabajo de n8n

Este repositorio es un fork de la iniciativa para recolectar y clasificar la mayor cantidad de flujos de trabajo (workflows) de n8n procedentes de diversas fuentes.

## Mejoras Implementadas
- Buscador de Workflows disponible con 10,405 workflows
- Descripciones en espanol para cada workflow
- Eliminacion de duplicados mediante hash unico
- Fusion con la comunidad n8n

## Instrucciones de Uso
1. Abre tu instancia de n8n.
2. Ve a Importar workflow.
3. Selecciona el archivo JSON del workflow.
4. Configura tus credenciales.
5. Ejecuta el workflow.

## Servidor MCP
https://gitmcp.io/DragonJAR/n8n-workflows-esp

## Contribucion
Abre un pull request con tus mejoras al repositorio.

## Aviso
Los workflows se proporcionan tal cual. Antes de usar en produccion, prueba en entorno controlado.

## Listado de Workflows

_Total de workflows: 10405_

### CRM y Ventas

#### HubSpot

- **0017-stripe-hubspot-slack.json**
  - **Descripción:** Integración y automatización con HubSpot CRM.
  - **Complejidad:** Baja (8 nodos)

- **0088-typeform-hubspot-email.json**
  - **Descripción:** Integración y automatización con HubSpot CRM.
  - **Complejidad:** Baja (7 nodos)

- **0122-sync-hubspot-pipedrive.json**
  - **Descripción:** Sincronización bidireccional entre HubSpot y otros sistemas.
  - **Complejidad:** Baja (5 nodos)

- **10014-Automatically-discover-enrich-HubSpot-buying-groups-with-Surfe-and-Google-Sheets.json**
  - **Descripción:** Descubre y enriquece automáticamente los contactos clave en el grupo de compra de una oportunidad de HubSpot combinando el dominio de la empresa de HubSpot con los criterios del grupo de compra que definas (departamentos, jerarquías, países, títulos de trabajo). Luego inserta estos contactos en HubSpot y envía un correo a tu equipo con un resumen limpio que incluye enlaces directos a HubSpot, para que ningún tomador de decisiones caiga por las grietas.
  - **Complejidad:** Media (22 nodos)

- **10064-Auto-enrich-sync-companies-from-Google-Sheets-to-HubSpot-using-GPT-4o-mini.json**
  - **Descripción:** Este workflow se inicia cada vez que agregas un nuevo nombre de empresa a una hoja de Google. Verifica si el nombre de la empresa está completo, luego usa IA para encontrar más detalles sobre la empresa como industria, tamaño, ubicación y sitio web. Luego busca la empresa en tu CRM de HubSpot. Si no está allí, la agrega automáticamente. Finalmente, actualiza la hoja de Google con toda la información nueva de la empresa.
  - **Complejidad:** Media (varios nodos)

- **10086-Automated-lead-capture-scoring-CRM-integration-with-HubSpot-Clearbit-Slack.json**
  - **Descripción:** Captura y califica automáticamente leads convirtiendo leads crudos en prospectos calificados a través de una automatización inteligente. Flujo de alto nivel: Captura de leads → Validación de datos → Enriquecimiento → Puntuación → Enrutamiento inteligente → Integración CRM y Notificaciones. El sistema captura leads de cualquier fuente, valida los datos, los enriquece con inteligencia de empresa, los puntúa basándose en criterios de calificación, y los enruta a HubSpot, Slack y Sheets para rastreo y notificaciones.
  - **Complejidad:** Alta (varios nodos)

- **10087-Predict-customer-churn-risk-create-interventions-with-GPT-4-Zendesk-HubSpot.json**
  - **Descripción:** Este workflow de predicción de riesgo de pérdida revoluciona la retención de clientes al predecir el riesgo de pérdida de 30 a 90 días antes de que ocurra. Flujo de alto nivel: Recopilación diaria de datos → Análisis multi-señal con IA → Puntuación de riesgo y predicción → Enrutamiento de riesgo inteligente → Actualizaciones de CRM y Alertas de Equipo. El sistema recopila datos automáticamente de múltiples fuentes, los analiza con IA para detectar señales de riesgo, asigna puntuaciones y crea intervenciones personalizadas.
  - **Complejidad:** Alta (varios nodos)

- **10240-AI-powered-lead-enrichment-from-Typeform-Calendly-to-HubSpot-CRM.json**
  - **Descripción:** Este workflow se inicia cada vez que llega un nuevo lead a través de Typeform (envío de formulario) o Calendly (reserva de reunión). Captura la información del lead, la estandariza en un formato limpio y verifica si el dominio del correo es de negocio. Si es un dominio de negocio, el workflow usa IA para enriquecer el lead con detalles de la empresa como industria, sede, tamaño y sitio web. Finalmente, combina toda la información, la fusiona con datos existentes del lead en HubSpot y guarda todo ordenadamente en Google Sheets para rastreo y reportes.
  - **Complejidad:** Media (varios nodos)

- **10265-Typeform-to-HubSpot-AI-enriched-scored-leads-with-GPT-4o-mini.json**
  - **Descripción:** Este workflow se inicia cada vez que se envía un nuevo lead a través de Typeform. Limpia y almacena los datos del lead en bruto, verifica si el correo es de negocio, usa IA para enriquecer el lead con información de la empresa, luego lo puntúa con IA. Después del enriquecimiento, actualiza tu CRM de HubSpot con todos los datos del lead y guarda una copia en Google Sheets para rastreo.
  - **Complejidad:** Media (varios nodos)

- **10374-Automate-Gmail-lead-follow-up-with-OpenAI-GPT-4O-HubSpot-Slack-Google-Sheets.json**
  - **Descripción:** Este workflow automatiza el manejo de nuevas respuestas de leads recibidas en Gmail. Captura correos con una etiqueta específica, analiza el mensaje usando IA para determinar sentimiento, intención, urgencia, próxima acción y prioridad, y luego decide si se necesita seguimiento. Si es necesario, crea tareas en HubSpot, notifica al equipo de ventas vía Slack y registra todos los detalles en Google Sheets para rastreo.
  - **Complejidad:** Alta (varios nodos)

- **10411-Analyze-form-feedback-with-GPT-4-sync-tasks-to-Monday-ClickUp-HubSpot.json**
  - **Descripción:** Este workflow automatiza la gestión de comentarios de clientes capturados a través de un formulario. Analiza los comentarios con IA para sentimiento e información, luego crea tareas estructuradas en Monday.com, ClickUp y HubSpot, asegurando que cada preocupación del cliente sea categorizada, priorizada y asignada al equipo correcto.
  - **Complejidad:** Media (varios nodos)

- **10612-Automate-support-ticket-classification-routing-from-HubSpot-to-Jira-with-GPT.json**
  - **Descripción:** Este workflow está diseñado para equipos de soporte al cliente, operaciones y ventas que gestionan mensajes de clientes a través de HubSpot y usan Jira para gestión interna de tareas. Automatiza la clasificación de tickets de soporte en HubSpot usando agentes de IA, detecta el sentimiento, los enruta a la cola correcta de Jira para que el equipo técnico correspondiente los maneje, y mantiene a los clientes informados.
  - **Complejidad:** Media (varios nodos)

- **10727-Quick-HubSpot-contact-lookup-in-Slack-for-sales-support-teams.json**
  - **Descripción:** Este workflow se inicia cuando un usuario activa un comando personalizado en Slack. Verifica si se proporcionó un mensaje válido (dirección de correo o ID de contacto de HubSpot). Basado en la entrada, busca HubSpot para el contacto ya sea por correo electrónico o por ID. Una vez encontrado el contacto, el workflow formatea los detalles en una tarjeta limpia amigable para Slack y la publica de vuelta en el canal de Slack.
  - **Complejidad:** Baja (varios nodos)

- **10802-Lead-routing-system-Qualify-direct-Typeform-leads-to-HubSpot-Sheets-Airtable.json**
  - **Descripción:** Este workflow captura nuevos leads de Typeform, verifica su presupuesto y los enruta según prioridad y origen. Los leads con presupuesto mayor de $5,000 se marcan como alta prioridad y se envían a HubSpot con una tarea de seguimiento para ventas. Los leads de Facebook se registran en Google Sheets para análisis de marketing, mientras los leads de SurveyMonkey se almacenan en Airtable para seguimiento de campañas. Finalmente, cada lead recibe un correo de confirmación automática de Gmail.
  - **Complejidad:** Media (13 nodos)

- **10836-Qualify-high-budget-leads-Typeform-to-HubSpot-Google-Sheets-Slack-alerts.json**
  - **Descripción:** Este workflow captura nuevos leads de Typeform, verifica instantáneamente si su presupuesto supera los $5,000 y los prioriza para seguimiento de ventas acelerado. Los leads de alto presupuesto se enriquecen en HubSpot como contactos con propiedades detalladas y se crea una tarea de seguimiento de alta prioridad. Los leads se enrutan según su origen (Facebook o SurveyMonkey) para almacenamiento apropiado.
  - **Complejidad:** Media (varios nodos)

- **10986-Enrich-HubSpot-contacts-with-LinkedIn-profiles-using-SerpAPI-Google-Docs-and-AI.json**
  - **Descripción:** Disparadores: HubSpot Trigger, Trigger manual, Leer Google Doc, Agente IA. Flujo: HubSpot detecta creación/actualización → Agente lee Google Doc con contexto sobre el contacto → Agent usa LinkedIn SerpAPI para encontrar perfiles públicos de decisores → Enrich datos → Actualiza HubSpot con información (LinkedIn, email, teléfono, cargo). Notifica Slack con resumen. Resuelve problema de información incompleta con LinkedIn SerpAPI (perfiles privados o no encontrados).
  - **Complejidad:** Alta (varios nodos)

- **10988-Automate-Calendly-to-HubSpot-contact-updates-meeting-logging.json**
  - **Descripción:** Este workflow sincroniza automáticamente las reservas de reuniones de Calendly en HubSpot CRM. Verifica si el asistente ya existe como contacto en HubSpot. Extrae los detalles del asistente y la reunión. Crea o actualiza el contacto en HubSpot. Registra el compromiso de la reunión en el contacto de HubSpot. Asegura que cada reserva vinculada al contacto correcto en HubSpot.
  - **Complejidad:** Media (varios nodos)

- **11015-Automate-sales-follow-ups-with-GPT-4o-mini-HubSpot-Slack-Teams-Telegram.json**
  - **Descripción:** Este workflow genera automáticamente mensajes de seguimiento personalizados para leads o clientes después de interacciones clave como demostraciones o llamadas de ventas. Enriquece los detalles del contacto desde HubSpot (o Monday.com opcionalmente), usa GPT-4o-mini para redactar un correo de seguimiento profesional adaptado al contexto del prospecto, y distribuye el mensaje a través de múltiples canales (Slack para equipos internos, Teams para comunicación corporativa, Telegram para notificaciones personales).
  - **Complejidad:** Media (varios nodos)

- **11018-Bidirectional-company-sync-between-ProspectPro-and-HubSpot-with-status-tracking.json**
  - **Descripción:** Esta plantilla sincroniza prospectos desde ProspectPro a HubSpot. Verifica si una empresa ya existe en HubSpot (por ID de ProspectPro o por dominio), luego actualiza el registro o crea uno nuevo. Los resultados de sincronización se registran de vuelta en ProspectPro con etiquetas (HubspotSynced, HubspotSyncFailed) para evitar duplicados y marcar errores, asegurando integraciones confiables y repetibles.
  - **Complejidad:** Media (29 nodos)

- **11111-Automate-lead-qualification-follow-up-with-Gemini-HubSpot-Zoom-Mailchimp.json**
  - **Descripción:** Automatiza la ingesta, calificación y seguimiento de leads. Los leads calificados como CALIFICADOS reciben: reunión programada, detalles de Zoom, confirmación por correo y actualización en CRM. Los leads NO CALIFICADOS reciben: secuencia de seguimiento por correo, actualización en CRM y recordatorio de 30 días. Usa Gemini para inteligencia, Zoom para videoconferencias y Mailchimp para emails masivos.
  - **Complejidad:** Alta (varios nodos)

- **1355-Dynamic-Hubspot-lead-routing-with-GPT-4-and-Airtable-sales-team-distribution.json**
  - **Descripción:** Agente IA para distribución dinámica de leads (HubSpot + Airtable). Procesa leads en tiempo real, busca al rep ideal en Airtable usando coincidencias de contexto (cargo, tamaño, ubicación), asigna leads a ejecutivos y notifica equipos. Notas: Usa HTTP Requests para búsqueda directa en HubSpot (sin soporte de sincronización nativo), requiere configuración manual de campos personalizados.
  - **Complejidad:** Alta (varios nodos)

#### Pipedrive

- **0086-calendly-pipedrive-slack.json**
  - **Descripción:** Integración y automatización con Pipedrive CRM.
  - **Complejidad:** Baja (5 nodos)

- **0216-typeform-pipedrive-mapeo.json**
  - **Descripción:** Integración y automatización con Pipedrive CRM.
  - **Complejidad:** Baja (8 nodos)

- **0228-github-fork-to-pipedrive-lead.json**
  - **Descripción:** Captura y gestión de leads en Pipedrive.
  - **Complejidad:** Baja (8 nodos)

- **0229-github-pullrequest-pipedrive.json**
  - **Descripción:** Integración y automatización con Pipedrive CRM.
  - **Complejidad:** Baja (6 nodos)

- **10113-Complete-Webflow-to-Pipedrive-integration-with-smart-phone-formatting.json**
  - **Descripción:** Integración avanzada de formularios web a CRM Pipedrive con soporte para números de teléfono internacionales. Ideal para equipos de ventas, especialistas en marketing y propietarios de negocios que necesitan gestión sofisticada de leads con detección automática de duplicados y soporte multicanal.
  - **Complejidad:** Alta (varios nodos)

- **10363-Natural-language-QA-for-Pipedrive-leads-using-GPT-4o-mini.json**
  - **Descripción:** Haz preguntas en lenguaje natural sobre los leads de Pipedrive. Este workflow extrae datos en tiempo real de Pipedrive y usa OpenAI GPT-4o-mini para responder preguntas como "leads agregados esta semana", "leads bloqueados por propietario", "siguientes actividades hoy" o "deal stage más alto". Las respuestas están basadas SOLO en datos de Pipedrive, sin alucinaciones ni conocimiento externo.
 Configuración: Conectar Pipedrive y OpenAI, configurar modelo y prompt del sistema.
 Instrucciones de configuración incluidas.
  - **Complejidad:** Media (varios nodos)

- **10365-Generate-daily-Pipedrive-deal-summaries-with-GPT-4o-mini.json**
  - **Descripción:** Este workflow extrae deals y sus notas de Pipedrive, limpia los IDs de etapa en nombres legibles, agrega la información y usa OpenAI para generar un resumen diario de tu pipeline de ventas. Configuración: Conectar Pipedrive y OpenAI. Uso: Análisis de pipeline, informes ejecutivos, detección de tendencias. Ideal para revisiones diarias y reuniones de revisión de pipeline.
  - **Complejidad:** Media (varios nodos)

- **10429-Track-Pipedrive-deals-in-Google-Sheets-for-sales-pipeline-reporting.json**
  - **Descripción:** Este workflow extrae deals de Pipedrive, los categoriza por etapa y los registra en una hoja de Google para informes y rastreo de pipeline de ventas. Ideal para seguimiento de rendimiento, proyecciones y análisis de tendencias de ventas.
  - **Complejidad:** Media (varios nodos)

- **10812-Connect-Pipedrive-deal-outcomes-to-GA4-Google-Ads-via-Measurement-Protocol.json**
  - **Descripción:** Tu publicidad y GA4 a menudo optimizan para eventos superficiales (envíos de formularios, clics) mientras el valor real está en Pipedrive (Qualified, Closed Won). Esta plantilla convierte los hitos de Pipedrive en eventos de servidor GA4, asegurando que tus campañas optimicen para ingresos, no solo clics baratos. Sin código, sin configuraciones de servidor complejas: busca `client_id` en los datos del evento de contacto de Pipedrive, envía a Measurement Protocol con parámetros de campaña, mapea resultado de conversión. Ideal para optimización de ROAS en B2B y attribution multicanal.
  - **Complejidad:** Media (varios nodos)

#### Salesforce

- **0234-excel-to-salesforce.json**
  - **Descripción:** Integración con Salesforce para automatización de ventas.
  - **Complejidad:** Media (12 nodos)

- **0954-3031-from-community-CallForge-01-filter-Gong-calls-synced-to-Salesforce-by.json**
  - **Descripción:** Descripción del workflow. ¿Para quién es? Este workflow está diseñado para equipos de ventas e ingresos que usan Gong y Salesforce para rastrear y analizar llamadas de ventas. Ayuda a automatizar la extracción, filtrado y preprocesamiento de datos de llamadas de Gong para análisis posterior con IA.
  - **Complejidad:** Alta (varios nodos)

- **10187-LeadBot-autopilot-chat-to-lead-for-Salesforce.json**
  - **Descripción:** LeadBot Autopilot — Chat-a-Lead para Salesforce. Descripción — Cómo funciona: 1) Saluda y Guía: Saluda al visitante y recopila información paso a paso — Nombre completo → Correo → Móvil → Interés en producto. 2) Valida Entradas: Verifica formatos de correo/teléfono; vuelve a preguntar si inválidos con cortesía. 3) Desduplica en Salesforce: Busca por correo; actualiza un lead existente si se encuentra. 4) Crea/Actualiza Lead: Escribe en Salesforce, incluyendo el campo `ProductInterest__c`. 5) Notifica Instantáneamente: Envía una alerta de Slack a tu equipo y un correo personalizado al prospecto. 6) Cierra Bucle: Confirma el envío y finaliza el chat. Configuración básica ~ 45-75 minutos.
  - **Complejidad:** Alta (21 nodos)

#### Zoho

- **10809-Automatic-email-categorization-labeling-in-Zoho-Mail-with-GPT-4o-mini.json**
  - **Descripción:** Categorización y etiquetado automático de correos con IA en Zoho Mail. Esta plantilla de n8n demuestra cómo usar la clasificación de texto con IA para categorizar automáticamente correos entrantes en Zoho Mail y aplicar la etiqueta correcta (Soporte, Facturación, RRHH, etc.). Ahorra tiempo manteniendo tu bandeja de entrada organizada, asegura que los correos se enrutan a la categoría correcta y mejora la eficiencia del equipo de soporte.
  - **Complejidad:** Media (varios nodos)

#### Leads/Lead Generation

- **0110-info-uplead-company.json**
  - **Descripción:** Gestión de automatización de leads.
  - **Complejidad:** Baja (2 nodos)

- **0116-typeform_lead_workflow.json**
  - **Descripción:** Gestión de automatización de leads.
  - **Complejidad:** Media (10 nodos)

- **0506-facebook-lead-to-klicktipp.json**
  - **Descripción:** Gestión de automatización de leads.
  - **Complejidad:** Baja (3 nodos)

- **0864-n8n_leaderboard_stats.json**
  - **Descripción:** Gestión de automatización de leads.
  - **Complejidad:** Alta (43 nodos)

- **0913-google-maps-leads-generator.json**
  - **Descripción:** Automatización de generación de leads desde diversas fuentes.
  - **Complejidad:** Alta (42 nodos)

- **10038-Secure-web-form-to-Odoo-CRM-lead-creation-with-UTM-tracking.json**
  - **Descripción:** Crea registros `crm.lead` en Odoo desde cualquier formulario web vía webhook seguro. El workflow valida campos requeridos, resuelve UTMs por nombre (fuente, medio, campaña) y escribe campos estándar de lead en Odoo. Limpio, portátil y listo para producción. Funcionalidades: Webhook seguro con autenticación de encabezado, validación de campos requeridos, resolución de UTMs por nombre, campos de lead estándar de Odoo.
  - **Complejidad:** Media (varios nodos)

- **10062-Automated-LinkedIn-lead-generation-DM-outreach-with-Airtable-and-Unipile.json**
  - **Descripción:** LinkedIn DM Automation. Vista general: Escala sin esfuerzo el outreach personalizado en LinkedIn usando un stack de automatización sin código. Esta plantilla proporciona un sistema potente y fácil de usar para cosechar leads de publicaciones de LinkedIn y gestionar outreach — todo dentro de Airtable y n8n. Características y puntos destacados: Entrada de acción simple, cosecha de leads, centro de calificación, flujo de campaña automatizado, panel de control unificado. Ideal para emprendedores, profesionales de ventas y equipos de crecimiento que buscan escalabilidad, transparencia y facilidad. Sin dependencias de navegador ni scraping manual. Configuración rápida: clona e implementa en menos de 30 minutos sin configuración de desarrollo requerida.
  - **Complejidad:** Alta (80+ nodos)

- **10078-AI-powered-lead-email-classification-auto-reply-with-GPT-4o-and-Gmail.json**
  - **Descripción:** Este workflow responde automáticamente a correos entrantes identificados como leads potenciales usando texto generado por IA. Se conecta a tu bandeja de entrada mediante IMAP en tiempo real, clasifica cada mensaje entrante con un modelo de IA, filtra los que no son leads y envía una respuesta personalizada a los relevantes.
  - **Complejidad:** Media (varios nodos)

- **10103-Generate-qualified-Instagram-leads-from-hashtags-with-Apify-and-Google-Sheets.json**
  - **Descripción:** Generación de leads de Instagram por hashtag. Automatiza el proceso de encontrar y calificar leads de Instagram basados en hashtags. Este workflow lee hashtags de Google Sheets, hace scraping de Instagram usando Apify, analiza el contenido de los captions y el idioma, compila nombres de usuario únicos, recopila información detallada de usuarios y filtra leads basándose en el número de seguidores. Funcionalidades: generación de leads, calificación, scraping multiplataforma, análisis de contenido, filtrado inteligente.
  - **Complejidad:** Alta (varios nodos)

- **10138-Generate-leads-from-Google-Maps-with-email.json**
  - **Descripción:** Generación de leads y extracción de correos de Google Maps. Categorías: Generación de Leads, Scraping Web, Automatización de Negocios. Este workflow crea un sistema completamente gratuito de scraping de correos de Google Maps que extrae correos ilimitados de negocios sin requerir APIs costosas de terceros. Construido enteramente en N8N usando solicitudes HTTP simples y JavaScript, este sistema puede generar miles de leads específicos por negocio.
  - **Complejidad:** Alta (varios nodos)

- **10143-Complete-B2B-sales-pipeline-Apollo-lead-gen-Mailgun-outreach-AI-reply-management.json**
  - **Descripción:** Pipeline de ventas B2B completo automatizado — Generación de Leads → Cold Outreach → Gestión de Respuestas con IA Redactadas. Automatiza tu flujo de prospección desde encontrar oportunidades B2B hasta redactar correos de respuesta usando IA, todo integrado con tu base de datos. Ideal para SDRs, fundadores y agencias de crecimiento que buscan velocidad, personalización y control sin perder capacidades manuales.
  - **Complejidad:** Alta (varios nodos)

- **10154-Lead-generation-agent.json**
  - **Descripción:** Este workflow está para equipos de agencias de marketing digital o equipos de ventas que buscan generar leads automáticamente basados en industria y ubicación. El workflow se activa cada vez que alguien envía el formulario "Lead Machine Form". Luego: busca empresas, recopila detalles de contacto, envía correos personalizados de cold outreach. Usa múltiples fuentes de datos (Google Maps, SerpAPI, etc.) para encontrar emails, realiza validaciones, gestiona intentos de envío y mantiene un registro centralizado en Google Sheets. Ideal para automatizar la prospección B2B a escala.
  - **Complejidad:** Alta (varios nodos)

- **10155-Website-lead-management-Send-contact-form-submissions-to-WhatsApp-Google-Sheets.json**
  - **Descripción:** Gestión de envíos de formularios de contacto. Este workflow procesa automáticamente envíos de formularios de contacto desde tu sitio web, enviando notificaciones instantáneas de WhatsApp con los detalles del lead formateados, mientras simultáneamente registra todos los datos en Google Sheets. Ideal para dueños de negocios, especialistas en marketing y desarrolladores web que necesitan responder rápidamente a consultas web.
 Sin configuración de desarrollo: usa una función de nodo HTTP Request existente para enviar mensajes de WhatsApp.
  - **Complejidad:** Media (varios nodos)

- **10216-Lead-enrichment-pipeline-Leadfeeder-to-Apollo-to-Google-Sheets.json**
  - **Descripción:** Pipeline de enriquecimiento de leads automatizado. Esta automatización crea un flujo diario que: 1) Extrae visitantes de ayer desde Leadfeeder 2) Enriquece datos de la empresa usando la base de datos potente de Apollo.io 3) Entrega leads enriquecidos en una hoja de Google con lógica de deduplicación inteligente 4) Alerta a tu equipo vía Telegram cuando requiere atención. Ideal para equipos de ventas B2B que necesitan datos de empresas enriquecidos y automatización de lead scoring.
  - **Complejidad:** Alta (varios nodos)

- **10220-Automated-lead-to-client-pipeline-with-Google-Sheets-email-notifications-time.json**
  - **Descripción:** Google Sheets CRM Automations: Etapas de Leads → Correos, Seguimiento de Clientes y Duración de Entrega. Convierte una hoja de Google simple en un CRM ligero potenciado por n8n. Este template monitoreas cambios en tus pestañas "Leads" y "Clientes" y reacciona automáticamente: ¿Calificado? → Enviar correo de reserva de Cal.com → "Propuesta coming soon" al pasar a etapa "Awaiting Proposal" → Registrar duración de entrega. Mejora la eficiencia de tu proceso de ventas y permite seguimiento automatizado del ciclo de vida del cliente.
 Ideal para pequeñas empresas y equipos de ventas que usan Google Sheets como base de datos simple.
  - **Complejidad:** Alta (varios nodos)

- **10245-Find-B2B-decision-maker-emails-build-lead-database-with-Serperdev-AnyMailFinder.json**
  - **Descripción:** Buscador automático de correos de tomadores de decisiones para B2B. Este workflow encuentra dominios de empresas, extrae correos de CEO, Ventas, Marketing y Operaciones usando múltiples APIs (SerpAPI, AnyMailFinder, Hunter, etc.), valida la calidad del correo, construye una base de datos completa de prospectos en Google Sheets y permite filtrar para campaña. Automatización de 4 fases: búsqueda de empresas → enriquecimiento de dominios → extracción de correos de tomadores → validación → construcción de base de datos. Ahorra horas de investigación manual y proporciona una base de datos escalable de alta calidad.
  - **Complejidad:** Alta (varios nodos)

- **10303-Google-Maps-leads-namesemailsphones-Apify-Airtable-custom-emails.json**
  - **Descripción:** Este workflow está diseñado para cualquier persona que desee: 1) Recopilar automáticamente contactos desde Google Maps: correos, teléfonos, sitios web, redes sociales (LinkedIn, Facebook, etc.) y ciudad/rating 2) Organizar todo en Airtable sin dolores de exportación CSV 3) Enviar correos personalizados a cada prospecto con plantillas personalizadas. Sin dependencias de navegador: usa API de Apify para scraping, Google Maps para búsqueda de negocios, Airtable para organización, Gmail para envío. Ideal para automatizar la prospección local y enviar outreach personalizado a escala.
  - **Complejidad:** Alta (varios nodos)

- **10309-Qualify-and-Enrich-Leads-with-Octaves-Contextual-Insights-and-Slack-Alerts.json**
  - **Descripción:** Califica y enriquece leads entrantes con insights contextuales y alertas de Slack. Este workflow está diseñado para equipos de ventas, ejecutivos de cuentas y RevOps que necesitan más que calificación básica. Usa Octaves API para inteligencia de productos de los prospectos y enriquecer los leads con insights contextuales profundos sobre cómo tu producto resuelve sus problemas. Envía alertas instantáneas a Slack para leads de alta prioridad o que requieren atención inmediata.
  - **Complejidad:** Alta (varios nodos, requiere nodos comunitarios)

- **10376-Automate-lead-gen-email-outreach-with-Apify-Apolloio-GPT-4-Google-Sheets.json**
  - **Descripción:** Generador automatizado de leads y correo para outreach. Este workflow combina múltiples fuentes de datos y servicios para crear una solución completa de prospección B2B automatizada. Funcionalidades: detección de startups recién financiadas, scraping de LinkedIn, enriquecimiento de datos, generación de correos personalizados con IA, integración con CRM. Nota: Este workflow contiene nodos comunitarios y solo es compatible con instancias autoalojadas de n8n.
  - **Complejidad:** Alta (varios nodos)

- **10382-Bulk-lead-email-validation-with-Google-Sheets-Anymail-Finder.json**
  - **Descripción:** Automatiza la verificación de direcciones de correo almacenadas en una hoja de Google. Este workflow procesa cada correo de la hoja usando la API de Anymail Finder para verificar si es válido y detecta el tipo de proveedor (Gmail, Outlook, Yahoo, etc.). Luego actualiza el estado de la hoja. Ahorra tiempo de limpieza manual y mejora la calidad de tu base de datos de correos. Funcionalidades: verificación masiva, detección de tipo de proveedor, actualización en tiempo real.
  - **Complejidad:** Media (varios nodos)

- **10399-Tracking-cold-email-engagement-metrics-using-Smartlead-and-Google-Sheets.json**
  - **Descripción:** Fetch automáticamente métricas de engagement a nivel de lead (aperturas, clics, respuestas, cancelaciones, rebotes) desde Smartlead y actualícalos en Google Sheets. Úsalo para mantener una única fuente de verdad sobre el rendimiento de tus campañas de correo frío. Proporciona visibilidad completa: aperturas, clics, respuestas por canal, cancelaciones por motivo. Funcionalidades: monitoreo en tiempo real, agregación de datos, análisis de rendimiento, alertas.
  - **Complejidad:** Media (varios nodos)

- **10401-Automated-WhatsApp-lead-nurturing-with-personalized-messages-via-Postgres.json**
  - **Descripción:** Lead nurturing con WhatsApp para MQLs (Marketing Qualified Leads). Este workflow recupera leads no calificados (MQLs) de una base de datos Postgres en intervalos configurados, envía mensajes de plantilla de WhatsApp personalizados vía API de Gallabox y registra la actividad en la base de datos mientras avanza el estatus del lead. Ideal para automatizar la reactivación de leads de calidad media hasta que se conviertan en oportunidades.
  - **Complejidad:** Media (varios nodos)

- **10402-Personalized-cold-email-generator-with-Supabase-Smartlead-Google-Gemini-AI.json**
  - **Descripción:** Generador de correos fríos personalizados para outreach. Este workflow usa IA (Google Gemini) para generar correos de cold outreach hiper-personalizados investigando sitios web de prospectos y empresas. Combina múltiples fuentes: búsqueda web, análisis de IA, integración con CRM (Smartlead), almacenamiento en Google Sheets. Funcionalidades: investigación automática, análisis de sitio web, redacción de correos personalizados, CRM integrado, rastreo de campaña.
  - **Complejidad:** Alta (varios nodos)

- **10436-Enrich-Mondaycom-leads-draft-personalized-emails-with-Explorium-MCP-and-GPT-41.json**
  - **Descripción:** Enriquece leads de Monday.com y redacta correos personalizados usando IA. Transforma tus inbound leads en oportunidades calentadas mediante análisis contextual profundo de cada prospecto, investigación de empresa y generación de correos personalizados de alta conversión. Usa Explorium MCP para investigación B2B, GPT-4.1 para redacción de correos y Monday.com para gestión de leads.
  - **Complejidad:** Alta (varios nodos)

- **10439-Extract-business-leads-from-Gmail-to-Google-Sheets-with-Slack-notifications.json**
  - **Descripción:** Este workflow permite extraer leads potenciales de tu bandeja de entrada. La idea del "reverse outreach" se basa en la noción de que el próximo gran cliente o socio comercial puede estar esperando ser descubierto en tu bandeja de entrada. La automatización tiene dos flujos: 1) Extrae correos históricos en masa 2) Ejecutar una búsqueda programada diaria (configurada para ejecutarse cada mañana) que busca nuevos leads. El workflow analiza inteligentemente cada correo para identificar oportunidades, extrae información del cliente y mantener un registro centralizado.
  - **Complejidad:** Alta (varios nodos)

- **10500-LinkedIn-lead-generation-Auto-DM-system-with-comment-triggers-using-Unipile.json**
  - **Descripción:** Sistema de generación de leads de LinkedIn automatizado. Este workflow monitorea publicaciones de LinkedIn en busca de palabras clave específicas, envía mensajes directos con lead magnets a usuarios comprometidos, gestiona el estado de las solicitudes de conexión y evita duplicados mediante un registro de base de datos. Ideal para agencias de crecimiento que buscan automatizar el outreach en LinkedIn sin violar las reglas de la plataforma.
  - **Complejidad:** Alta (70+ nodos, requiere nodos comunitarios)

- **10527-Restaurant-lead-generation-from-Google-Maps-with-Apify-Airtable-AI-newsletter.json**
  - ** estilo:** Este workflow contiene nodos comunitarios y solo es compatible con instancias autoalojadas de n8n.
  - **Descripción:** Generación de leads de restaurantes automatizada con newsletter de IA. Scraping de Google Maps para encontrar restaurantes, filtrado por calidad (ratings, etc.), enriquecimiento con IA, scraping de sitios web (menú, horarios, precios), generación de newsletter tipo Morning Brew personalizada y envío. Automatización completa del flujo: descubrimiento → análisis → enriquecimiento → contenido → filtrado → generación de newsletter → almacenamiento en Airtable. Requiere múltiples APIs (Apify, SerpAPI, OpenAI).
  - **Complejidad:** Alta (varios nodos)

- **10549-Extract-business-emails-from-Google-Maps-to-Google-Sheets-for-lead-generation.json**
  - **Descripción:** Generador de leads de correos de negocios gratuito desde Google Maps. Este workflow construye un sistema completamente gratuito de scraping de correos de Google Maps usando HTTP requests y JavaScript, sin requerir APIs de terceros. Busca listados de negocios en Google Maps por consultas personalizadas (ej. "abogados en Miami"), extrae sitios web, extrae correos de negocios y los exporta directamente a Google Sheets. Ideal para generar miles de leads específicos por industria.
  - **Complejidad:** Alta (varios nodos)

- **10614-LinkedIn-lead-finder-Gemini-powered-personalized-outreach-with-Google-Sheets.json**
  - **Descripción:** Automatiza el proceso de encontrar leads de LinkedIn y redactar mensajes de outreach personalizados. Toma entrada del usuario (palabras clave + propósito), genera una consulta de búsqueda booleana optimizada para LinkedIn usando Gemini, extrae hasta 20 resultados vía Google Custom Search API, los registra en Google Sheets y luego redacta mensajes de outreach personalizados para cada lead. Finalmente, el workflow actualiza la hoja de Google con los mensajes redactados para fácil revisión y envío.
  - **Complejidad:** Alta (varios nodos)

- **10630-Google-Maps-to-Airtable-lead-scraper-with-GPT-contact-extraction-from-impressum.json**
  - **Descripción:** Workflow automatizado de descubrimiento de empresas en diferentes ciudades, extracción de sus datos de contacto y almacenamiento en Airtable. 1) Bucle por ciudades en Airtable con búsqueda personalizada (ej. "agencia de SEO en Berlín") 2) Consulta Google Maps API para obtener resultados 3) Extrae datos de contacto (dirección, sitio web, teléfono) 4) Extrae datos de contacto adicionales desde el sitio web (usando Scrape.do para datos de contacto e IA para extraer email de impressum) 5) Crear o actualizar registro en Airtable. Funcionalidades: búsqueda de negocios personalizada, extracción de datos de contacto de múltiples fuentes, generación de base de datos B2B. Ideal para listas de prospección sistemática y enriquecimiento de datos.
  - **Complejidad:** Alta (varios nodos)

- **10644-LeadChat-Booker-conversational-lead-capture-that-schedules.json**
  - **Descripción:** LeadBot conversacional con captura y programación. Captura información paso a paso a través de chat amigable, valida entradas, verifica duplicados en Salesforce (actualiza si existe, crea si es nuevo), notifica al equipo internamente vía Slack y envía confirmación por correo al cliente. Si el prospecto califica, programa reunión con Zoom y añade a Mailchimp. Si no califica, envía secuencia de seguimiento y recordatorio de 30 días.
  - **Complejidad:** Alta (varios nodos)

- **10652-Auto-save-Instagram-leads-to-Google-Sheets.json**
  - **Descripción:** Captura automática de leads de Instagram en Google Sheets. Este workflow captura automáticamente leads enviados a través del formulario de Instagram de Meta y los guarda directamente en una hoja de Google. Asegura que cada nuevo lead se registre instantáneamente, creando una base de datos centralizada para equipos de marketing y ventas. Ideal para campañas de marketing en Instagram, influencers y equipos de ventas que necesitan captura automatizada de leads.
  - **Complejidad:** Baja (varios nodos)

- **10701-Generate-B2B-lead-opportunities-from-websites-with-Brightdata-OpenRouter-AI.json**
  - **Descripción:** Identifica automáticamente oportunidades B2B desde sitios web de empresas. Analiza páginas de "About Us", "Team" y "Contact" para identificar puntos de dolor y necesidades, luego usa IA para generar un resumen estructurado de oportunidades de ventas. Usa Bright Data Web Unblocker para acceder a sitios web bloqueados o protegidos, OpenRouter para enrutamiento inteligente de LLMs avanzados (GPT-4, Claude, etc.). Resultado: resumen estructurado + enlaces directos a páginas relevantes. Ideal para SDRs y equipos de cuentas que investigan prospectos y necesitan identificación rápida de oportunidades.
  - **Complejidad:** Alta (varios nodos, requiere nodos comunitarios)

- **10716-Email-new-leads-from-Google-Sheets-via-Outlook-on-a-schedule.json**
  - **Descripción:** Envía correos de outreach a nuevos leads en Google Sheets según una programación diaria. Este workflow lee una hoja de Google con leads no contactados, envía correos personalizados a cada uno usando plantillas variables (campo de asunto personalizado, cuerpo con datos del prospecto, nombre del remitente), marca cada lead como contactado en la hoja después de enviar para evitar correos duplicados. Diseñado para campañas de correo frío sistematizadas que respeten el tiempo de los prospectos y mantienen la integridad de tu marca.
  - **Complejidad:** Media (varios nodos)

- **10725-Generate-AI-powered-sales-proposals-from-JotForm-leads-with-OpenAI-and-Google.json**
  - **Descripción:** Generador automático de propuestas de ventas desde envíos de formularios JotForm. Este workflow usa IA para analizar respuestas de formulario y generar propuestas de ventas personalizadas y profesionales automáticamente. Procesa: 1) Recepción de envío JotForm 2) Análisis con IA del prospecto (necesidades, presupuesto, cronograma) 3) Generación de propuesta con IA (estructura profesional, precios, términos) 4) Creación de documento PDF y envío por correo 5) Seguimiento de propuestas en Google Drive. Ideal para empresas de servicios que necesitan automatizar su proceso de propuestas.
  - **Complejidad:** Alta (varios nodos)

- **10785-Generate-and-research-sales-leads-with-Jina-AI-OpenAI-email-automation-via-Gmail.json**
  - **Descripción:** Genera leads listos para enviar y automatiza correos de outreach personalizados. Este workflow combina múltiples servicios para crear una solución de outbound B2B automatizada. Usa Google (Jina AI) para investigación de negocios, OpenAI para redacción de correos, Gmail para envío y Google Sheets para almacenamiento. Flujo de trabajo: investigación → redacción → envío → seguimiento → almacenamiento. Funcionalidades: investigación B2B, personalización de correos, gestión de campañas, CRM integrado.
  - **Complejidad:** Alta (varios nodos)

- **10825-Research-business-leads-with-Perplexity-AI-save-to-Google-Sheets-using-OpenAI.json**
  - **Descripción:** Automatiza la investigación de nuevos leads en tu área objetivo y estructura los resultados para append en Google Sheets. Usa Perplexity para investigar negocios (ej. "cafeterías en esta ciudad"), limpia y estructura la información en JSON usando OpenAI, luego los agrega a Google Sheets. Ideal para equipos de ventas que hacen prospección geográfica y necesitan leads investigados y organizados.
  - **Complejidad:** Media (varios nodos)

- **10863-Automate-B2B-lead-generation-email-campaigns-with-Google-Maps-SendGrid-AI.json**
  - **Descripción:** Automatiza el ciclo de vida completo de lead generation y email campaigns para B2B. Este workflow n8n-powered combina seis flujos especializados en uno: 1) Generación de leads desde Google Maps (scrapeo, enriquecimiento, almacenamiento) 2) Envío de campañas por correo (SendGrid) 3) Detección y clasificación de respuestas (Gmail, IA) 4) Reenvío y segmentación 5) Gestión de opt-outs y supresiones 6) Análisis de rendimiento 7) Base de datos centralizada (Google Sheets). Automatización completa de outbound: descubrimiento → enriquecimiento → outreach → clasificación → análisis → optimización. Ideal para equipos de outbound B2B que buscan automatización a escala.
  - **Complejidad:** Alta (varios nodos)

- **10872-Deduplicate-lead-data-with-Google-Sheets-automated-email-alerts-log-management.json**
  - **Descripción:** Mantén tu base de datos de leads limpia y confiable con este workflow automatizado. Detecta automáticamente registros duplicados en tu hoja de Google, genera registros estructurados de logs para cada operación de limpieza, envía alertas de correo cuando se detectan problemas y mantiene un registro de auditoría completa. Ideal para bases de datos grandes donde múltiples usuarios o sistemas pueden actualizar registros simultáneamente. Funcionalidades: deduplicación en tiempo real, registro de auditoría, alertas por correo, gestión de historial.
  - **Complejidad:** Alta (varios nodos)

- **10873-Business-hours-lead-response-system-with-Gmail-Google-Sheets-Telegram-alerts.json**
  - **Descripción:** Nunca dejes que tus leads esperen una respuesta profesional. Este workflow n8n-powered garantiza que cada consulta recibida por un formulario de tu sitio web reciba una respuesta oportuna y profesional, ya sea horario laboral o no. El workflow monitorea tu Google Sheet para nuevos formularios, verifica horarios de oficina configurados, verifica si es horario laboral (solo respuestas profesionales) y envía automáticamente correos personalizados con el horario apropiado. Si es horario no laboral, envía un mensaje amable informando que responderemos en horario laboral. Garantiza respuestas rápidas y profesionales para mejorar la experiencia del cliente.
  - **Complejidad:** Media (varios nodos)

- **10884-Monitor-lead-response-time-SLA-breaches-with-Google-Sheets-Telegram-alerts.json**
  - **Descripción:** Nunca pierdas un lead de nuevo por incumplir tu SLA. Este workflow n8n-powered monitorea tu Google Sheet para leads sin respuesta y envía alertas instantáneas a Telegram cuando se detecta una violación de SLA. Los umbrales se pueden configurar (ej.  1 hora, 4 horas, 24 horas). Ideal para equipos de ventas y soporte que tienen SLAs e necesitan monitoreo proactivo para evitar pérdida de oportunidades.
  - **Complejidad:** Media (varios nodos)

- **10869-Qualify-leads-auto-assignment-with-GPT-4-Mini-Google-Sheets-to-ClickUp.json**
  - **Descripción:** Elimina la confusión en la transferencia de ventas a los leads calificados. Este workflow crea y asigna automáticamente tareas en ClickUp cuando el estatus de un lead en Google Sheets cambia a "Qualified" o "Hot", asegurando propiedad asignación y responsabilidad clara. Envia resúmenes de IA generados por GPT-4 Mini que incluyen contexto del prospecto, permitiendo a los representantes ver todo el contexto antes de contactar al lead. Mejora la propiedad de transición y reduce el tiempo de capacitación del equipo.
  - **Complejidad:** Alta (varios nodos)

- **10936-Automate-lead-intake-deduplication-with-Google-Forms-Sheets-and-GoHighLevel-CRM.json**
  - **Descripción:** Elimina entradas duplicadas y simplifica tu gestión de leads. Este workflow monitorea envíos de formularios web en tiempo real, verifica contra una base de datos de GoHighLevel (GHL) CRM para detectar duplicados por correo o nombre/empresa, actualiza o crea registros únicos, y sincroniza con Google Sheets. Ideal para empresas que usan GoHighLevel y quieren evitar corrupción de datos.
  - **Complejidad:** Alta (varios nodos)

- **11024-Automated-lead-follow-up-system-with-Gmail-Google-Calendar-Sheets-sync.json**
  - **Descripción:** Aumenta tus tasas de conversión de reuniones. Este workflow automatiza el seguimiento de leads no reservados que han pasado 24 horas después de un envío de formulario. Envía correos de seguimiento personalizados con enlaces a reservas de calendario (Cal.com, Google Calendar), ofrece horarios alternativos y confirma reservas automáticamente. Si un prospecto responde, el workflow actualiza los datos del lead y cancela las notificaciones de seguimiento programadas. Ideal para equipos de ventas con calendarios que necesitan automatización de seguimiento sistemática.
  - **Complejidad:** Alta (varios nodos)

- **11029-Lead-qualification-auto-assignment-with-GPT-4-Mini-Google-Sheets-to-ClickUp.json**
  - **Descripción:** Calificación inteligente con asignación automática. Usa IA para analizar prospectos de inbound y tomar decisiones de calificación complejas. Detecta patrones de comportamiento, evalúa el nivel de compra (BANT, BANT, SQLI, TSQL), segmenta leads y asigna a los representantes más apropiados basándose en coincidencias de perfil y disponibilidad. Usa ClickUp para gestión de asignación y Google Sheets para registro.
  - **Complejidad:** Alta (varios nodos)

- **11045-Automated-lead-follow-up-system-with-Gmail-Google-Sheets-Slack-Google-Sheets.json**
  - **Descripción:** Sistema de seguimiento de leads automatizado con múltiples etapas. Monitorea Google Sheets para cambios, ejecuta secuencia de follow-ups (Día 1, 3, 7, 14), envía correos automáticos, notifica en Slack, midee conversiones. Configuración flexible: define tu propio plan de follow-up, número de toques, plantillas de correo. Incluye análisis de sentimiento con IA para personalización avanzada.
  - **Complejidad:** Alta (varios nodos)

- **11053-Lead-analysis-personalized-email-generation-with-OpenAI-Firecrawl-gotoHuman.json**
  - **Descripción:** Agente de Outreach IA para reacción rápida a leads nuevos. Este workflow usa IA para analizar información de prospecto (de sitios web, LinkedIn, etc.) y generar correos de outreach personalizados. Característica única: gotoHuman permite revisión y aprobación antes del envío, asegurando calidad y control. Flujo: Análisis → Generación de borrador → Revisión humano → Aprobación → Envío. Ideal para equipos que buscan respuesta rápida con calidad garantizada.
  - **Complejidad:** Alta (varios nodos)

- **11096-Automated-WhatsApp-welcome-messages-for-sales-leads-with-Google-Sheets-Rapiwa.json**
  - **Descripción:** Mensajes de bienvenida automatizados en WhatsApp para leads de ventas. Esta automatización es ideal para equipos de ventas que usan Google Sheets para gestionar leads y Rapiwa (WhatsApp Business API) sin WhatsApp oficial. Procesa leads nuevos de Google Sheets, envía mensajes de bienvenida personalizados con información del prospecto (nombre, empresa, fuente) y notifica al equipo. Sin configuración de servidor compleja: usa webhook de Rapiwa para entrega directa y confiable.
 Ideal para respuestas rápidas y personalización a escala.
  - **Complejidad:** Media (varios nodos)

- **1817-CRM-to-professional-PDF-Proposals-with-Gmail-Drive-Slack-notifications.json**
  - **Descripción:** Transforma la creación de propuestas de ventas de horas a minutos. Genera automáticamente propuestas PDF bellamente diseñadas desde datos de CRM o envíos de formularios, las entrega instantáneamente por correo y mantiene registros estructurados. Usa Gmail Drive para almacenamiento y Slack para colaboración. Ideal para consultores, agencias y freelancers que necesitan profesionalización de propuestas.
  - **Complejidad:** Alta (varios nodos)

#### Email Marketing/Contact

- **0021-mock-contacts-to-sheet.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Baja (4 nodos)

- **0074-getresponse-contact-update-flow.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Baja (5 nodos)

- **0099-crear-contacto-drift.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Baja (2 nodos)

- **0117-calendly-dropcontact-notion-integracion.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Baja (3 nodos)

- **0248-shopify-mautic-contact.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Baja (3 nodos)

- **0335-sendgrid-contact-flow.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Baja (4 nodos)

- **0336-google-contacts-test.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Baja (4 nodos)

- **0344-form-contacto-telegram.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Media (12 nodos)

- **0404-systeme-io-contact-flow.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Media (12 nodos)

- **0529-active-campaign-contact.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Baja (2 nodos)

- **0590-keap-contact-all.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Baja (2 nodos)

- **0749-emelia-campaign-contact.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Baja (3 nodos)

- **0763-autopilot-to-airtable-contact.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Baja (3 nodos)

- **0773-slack-birthday-contacts.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Baja (7 nodos)

- **10068-Automate-marketing-campaigns-with-Airtable-CRM-Brevo-email-tracking.json**
  - **Descripción:** Automatización completa de gestión de campañas de marketing desde un CRM basado en Airtable usando Brevo para envío de correos y rastreo de eventos. El workflow monitorea campañas enviadas, rastrea eventos (aperturas, clics, rebotes, cancelaciones) en tiempo real y mantiene actualizadas las métricas en el CRM para optimización continua. Ideal para equipos de marketing que necesitan visibilidad completa de rendimiento de campañas.
  - **Complejidad:** Alta (varios nodos)

- **1010-workflow-contact-form-automation.json**
  - **Descripción:** Gestión de contactos y automatización.
  - **Complejidad:** Alta (24 nodos)

- **10231-Automate-sponsored-deal-email-responses-with-Gmail-and-GPT-4.json**
  - **Descripción:** Gestión automatizada de solicitudes de patrocinio y correos no deseados. Este workflow usa IA para analizar correos entrantes, detecta automáticamente si son solicitudes de patrocinio, decide la respuesta apropiada (declinación educada, contrapropuesta suave, etc.) y envía automáticamente. Reduce la carga manual de revisar solicitudes y mejora el tiempo de respuesta.
  - **Complejidad:** Media (varios nodos)

- **10248-Parse-and-create-LEDGERS-contacts-from-unstructured-data-with-GPT-4o.json**
  - **Descripción:** Creador de contactos LEDGERS (trabaja con cualquier trigger). Este workflow inteligente usa IA (GPT-4o) para crear automáticamente contactos en LEDGERS desde datos no estructurados (webhook, formularios, etc.). La IA analiza el contenido, extrae información relevante y genera contactos con campos estructurados. Ideal para integraciones complejas donde los datos de entrada varían en formato.
  - **Complejidad:** Alta (varios nodos)

- **10283-Send-personalized-HTML-welcome-emails-to-new-Xero-contacts-via-SMTP.json**
  - **Descripción:** Correo de bienvenida HTML automatizado para nuevos contactos de Xero. Envía automáticamente un correo HTML profesional y personalizado al momento en que se crea un nuevo contacto en tu cuenta de Xero. Mejora la impresión de primera interacción del cliente con diseño profesional. Ideal para contadores, firmantes de servicios y empresas de contabilidad.
  - **Complejidad:** Media (varios nodos)

- **10381-Sync-Google-Sheets-contacts-to-SeaTable-with-updateinsert-logic.json**
  - **Descripción:** Sincroniza tus contactos de Google Sheets con SeaTable. Usa Google Sheets como fuente de datos principal, actualiza o inserta registros en SeaTable basándose en correo electrónico (clave única). Si el registro ya existe en SeaTable, lo actualiza con los datos más recientes. Si no existe, inserta uno nuevo. Garantiza integridad bidireccional y manejo de conflictos (último escritor gana).
  - **Complejidad:** Media (varios nodos)

- **10457-Get-all-the-contacts-from-GetResponse-and-update-them.json**
  - **Descripción:** Obtiene todos los contactos de GetResponse y los actualiza. Simple automatización para mantener sincronizado entre ambos sistemas. Ideal para usuarios de GetResponse que también usan otro CRM.
  - **Complejidad:** Baja (varios nodos)

- **10459-Automated-client-onboarding-system-with-Notion-email-CRM-integration.json**
  - **Descripción:** Sistema de bienvenida al cliente concierge pro. Captura envío de formulario a través de webhook, crea Cliente en Notion, envía correo de bienvenida con horario de reserva opcional, opcionalmente pingea al propietario en Telegram, actualiza CRM simultáneamente (HubSpot, Airtable), guarda un recordatorio temporal en Google Calendar. Ideal para pequeñas empresas y estudios que necesitan experiencia de cliente profesional sin contratar servicios dedicados.
  - **Complejidad:** Alta (varios nodos)

- **10508-Manage-schedule-contacts-with-Telegram-Bot-using-GPT-4o-mini-Google-Services.json**
  - **Descripción:** Asistente personal de IA con Telegram. Transforma tu Telegram en un asistente de IA potente que puede gestionar tu calendario, buscar en la web, acceder a tus contactos y enviar correos simples. Usa GPT-4o-mini para comprensión de lenguaje natural y varios servicios de Google (Calendar, Contacts, Drive, Gmail). Flujo de trabajo: recibe comando → procesa con IA → ejecuta acción → responde. Ideal para profesionales y gestores ocupados.
  - **Complejidad:** Alta (varios nodos)

- **10543-Automate-Gmail-tasks-with-Gemini-AI-assistant-and-contact-management.json**
  - **Descripción:** Automatiza tareas de Gmail usando IA. Usa múltiples casos de uso: enviar, responder, etiquetar, eliminar, buscar y extraer información. Usa Gemini para inteligencia en lenguaje natural para entender contexto y ejecutar comandos. Ideal para usuarios que manejan grandes volúmenes de correo y necesitan organización.
  - **Complejidad:** Alta (varios nodos)

- **10696-Process-contact-form-submissions-with-validation-and-MongoDB-storage.json**
  - **Descripción:** Procesa seguro de envíos de formularios de contacto. Este workflow n8n-powered valida entradas de usuario, formatea datos, previene inyecciones SQL y almacena todo de forma segura en MongoDB. Garantiza integridad de datos y consistencia. Ideal para sitios web con formularios de contacto que requieren seguridad robusta.
  - **Complejidad:** Media (varios nodos)

- **10956-Create-professional-email-drafts-with-GPT-4-Telegram-contact-database.json**
  - **Descripción:** Generador de correos profesionales a través de comandos de Telegram con IA. Usa OpenAI GPT-4 para generar correos formales y profesionales, usa Pinecone vector database con RAG para buscar contactos y contexto. Flujo de trabajo: usuario envía comando → comando → IA busca datos → genera borrador → usuario revisa → envía. Ideal para profesionales que necesitan correos profesionales pero no tiempo para redactarlos todos.
  - **Complejidad:** Alta (varios nodos)

- **11108-Automate-digital-product-delivery-sales-tracking-with-Stripe-Email-Notion.json**
  - **Descripción:** Automatización de entrega de productos digitales después de pagos de Stripe. Este workflow procesa webhooks de Stripe para nuevos pagos, verifica la entrega, actualiza registros en Notion para seguimiento y opcionalmente notifica en Telegram. Ideal para vendedores de productos digitales (plantillas, cursos, SaaS) que necesitan automatización completa post-pago.
  - **Complejidad:** Alta (varios nodos)

#### Other CRM

- **0294-twentycrm-eventos-canales.json**
  - **Descripción:** Workflow de automatización CRM y ventas.
  - **Complejidad:** Media (11 nodos)

- **0490-mediamarkt-deals.json**
  - **Descripción:** Workflow de automatización CRM y ventas.
  - **Complejidad:** Baja (8 nodos)

- **0507-whatsapp-crm-automation.json**
  - **Descripción:** Workflow de automatización CRM y ventas.
  - **Complejidad:** Baja (6 nodos)

- **0879-whatsapp-sales-agent.json**
  - **Descripción:** Workflow de automatización CRM y ventas.
  - **Complejidad:** Alta (28 nodos)

- **11010-Create-ideal-customer-profile-from-websites-content-to-Google-Doc.json**
  - **Descripción:** Generador de Perfil de Cliente Ideal (ICP) desde contenido web. Recolecta datos de sitios web (About Us, Team, Contact), usa crawling (Scraping o Bright Data) para contenido completo, usa IA (GPT-5, Claude u OpenRouter) para análisis profundo, genera ICP estructurado en Google Doc. Para: equipos de growth, marketing y ventas que necesitan entendimiento profundo de su base de clientes ideales.
  - **Complejidad:** Alta (varios nodos)

#### AI/Sales Automation

- **0242-2633-from-community-INSEE-company-data-enrichment-for-Agile-CRM-For-French.json**
  - **Descripción:** Cómo funciona: 1) Extrae todas las entradas de empresas en Agile CRM 2) Busca el nombre de la empresa en la base de datos abierta de INSEE francesa para extraer dirección e ID gubernamental (SIREN) 3) Actualiza las entradas con datos extraídos del INSEE. Workflow también tiene función de solo lectura para asegurar que las entradas no se sobrescriban accidentalmente. Requisitos: Agregar credenciales de AgileCRM y OpenData INSEE.
  - **Complejidad:** Media (varios nodos)

- **0815-ai-company-researcher-sales.json**
  - **Descripción:** Automatización de ventas y leads utilizando IA.
  - **Complejidad:** Alta (22 nodos)

- **10088-Automate-HighLevel-CRM-with-GPT-5-knowledge-retrieval-document-context.json**
  - **Descripción:** Supercharge tu CRM HighLevel con el poder de GPT-5. Esta marketplace transforma cómo trabajas: crea, actualiza y gestiona contactos, oportunidades, tareas y calendarios automáticamente — todo desde un solo agente inteligente que entiende contexto, recupera datos y ejecuta acciones al instante. Desbloquea automatización completa: Lead scoring, enrutamiento inteligente, enriquecimiento personalizado, gestión de tareas, inteligencia documental.
  - **Complejidad:** Alta (varios nodos)

- **10124-Automated-B2B-prospecting-with-RapidAPI-Hunterio-GPT-Gmail.json**
  - **Descripción:** Pipeline B2B automatizado — Lead Gen → Cold Outreach → Gestión de Respuestas con IA Redactadas. Automatiza tu flujo de prospección desde encontrar oportunidades B2B hasta redactar correos de respuesta usando IA, todo integrado con tu base de datos. Ideal para SDRs, fundadores y agencias de crecimiento que buscan velocidad, personalización y control sin perder capacidades manuales.
  - **Complejidad:** Alta (varios nodos)



- **0002-Gumroad-MailerLite-trigger.json**
  - **Descripcion:** Disparador de ventas de Gumroad para automatizar notificaciones y sincronización con MailerLite
  - **Complejidad:** Media (8 nodos)

- **0004-connectwise-ticket-alerts-to-teams.json**
  - **Descripcion:** New Ticket Sistema de alertas automáticas para notificaciones multi-canal y gestión de incidenciass to Teams
  - **Complejidad:** Media (8 nodos)

- **0015-berlin-clima-plivo.json**
  - **Descripcion:** Automatización de berlin clima plivo
  - **Complejidad:** Baja (3 nodos)

- **0017-stripe-hubspot-slack.json**
  - **Descripcion:** On new Stripe Invoice Payment update Hubspot and notify the team in Slack
  - **Complejidad:** Media (8 nodos)

- **0028-verificacion-email-deliverable.json**
  - **Descripcion:** Verificación de correos electrónicos para validar direcciones y detectar emails no entregables
  - **Complejidad:** Baja (4 nodos)

- **0029-mattermost-emelia-trigger.json**
  - **Descripcion:** Automatización de mattermost emelia trigger
  - **Complejidad:** Baja (2 nodos)

- **0033-ip-location-email.json**
  - **Descripcion:** Obtención de ubicación geográfica basada en dirección IP
  - **Complejidad:** Media (6 nodos)

- **0037-mattermost-trigger.json**
  - **Descripcion:** Automatización de mattermost trigger
  - **Complejidad:** Baja (4 nodos)

- **0046-email-invite-calendar.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Baja (3 nodos)

- **0049-chargebee-event-trigger.json**
  - **Descripcion:** Receive updates for events in Chargebee
  - **Complejidad:** Baja (1 nodos)

- **0054-clickup-trigger.json**
  - **Descripcion:** Receive updates for events in ClickUp
  - **Complejidad:** Baja (1 nodos)

- **0062-active-campaign-account-trigger.json**
  - **Descripcion:** Receive updates when a new account is added by an admin in ActiveCampaign
  - **Complejidad:** Baja (1 nodos)

- **0064-twitter-if-trigger.json**
  - **Descripcion:** Automatización de twitter if trigger
  - **Complejidad:** Baja (4 nodos)

- **0075-syncro-opsgenie-integration.json**
  - **Descripcion:** Envío de alertas de Sincronización bidireccional de datos entre plataformas y servicios en tiempo realro a OpsGenie para gestión de incidentes
  - **Complejidad:** Media (7 nodos)

- **0081-shopify-pedidos-trigger.json**
  - **Descripcion:** Automatización de shopify pedidos trigger
  - **Complejidad:** Media (9 nodos)

- **0086-calendly-pipedrive-slack.json**
  - **Descripcion:** Integración con Slack para comunicación
  - **Complejidad:** Baja (5 nodos)

- **0088-typeform-hubspot-email.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Media (7 nodos)

- **0102-google-calendar-meetings-slack.json**
  - **Descripcion:** Integración con Slack para comunicación
  - **Complejidad:** Alta (12 nodos)

- **0106-google-drive-email-alert.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Baja (2 nodos)

- **0108-hubspot-trigger-para-chatbot.json**
  - **Descripcion:** Automatización de hubspot trigger para chatbot
  - **Complejidad:** Baja (4 nodos)

- **0118-slack-error-alert.json**
  - **Descripcion:** Integración con Slack para comunicación
  - **Complejidad:** Baja (2 nodos)

- **0125-flow-trigger-task.json**
  - **Descripcion:** Receive updates for specified tasks in Flow
  - **Complejidad:** Baja (1 nodos)

- **0131-limpia_pacotes_telegram.json**
  - **Descripcion:** Integración con Telegram para mensajería
  - **Complejidad:** Media (7 nodos)

- **0135-dominio-email-extractor.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Baja (3 nodos)

- **0137-tareas-toggl-alertas.json**
  - **Descripcion:** Get new time entries from Toggl
  - **Complejidad:** Baja (1 nodos)

- **0138-telegram-receipts-textract.json**
  - **Descripcion:** Integración con Telegram para mensajería
  - **Complejidad:** Baja (4 nodos)

- **0145-readwise_telegram_sync.json**
  - **Descripcion:** Integración con Telegram para mensajería
  - **Complejidad:** Alta (11 nodos)

- **0154-hubspot-company-alerts.json**
  - **Descripcion:** Automatización de hubspot company alerts
  - **Complejidad:** Baja (5 nodos)

- **0155-mattermost-financial-metrics-cron.json**
  - **Descripcion:** Send financial metrics monthly to Mattermost
  - **Complejidad:** Baja (3 nodos)

- **0156-news-ycombinator-telegram.json**
  - **Descripcion:** Integración con Telegram para mensajería
  - **Complejidad:** Media (7 nodos)

- **0160-sendy-subscribe-campaign.json**
  - **Descripcion:** Add a subscriber to a list and create and send a campaign
  - **Complejidad:** Baja (3 nodos)

- **0161-onfleet-driver-signup-alert.json**
  - **Descripcion:** Onfleet Driver signup message in Slack
  - **Complejidad:** Baja (2 nodos)

- **0164-mattermost-airtable-trigger.json**
  - **Descripcion:** Receive a Mattermost message when new data gets added to Airtable
  - **Complejidad:** Baja (2 nodos)

- **0172-slack-file-downloader.json**
  - **Descripcion:** Integración con Slack para comunicación
  - **Complejidad:** Baja (3 nodos)

- **0177-youtube-telegram-monitor.json**
  - **Descripcion:** Integración con Telegram para mensajería
  - **Complejidad:** Baja (5 nodos)

- **0188-kafka-temp-alert.json**
  - **Descripcion:** Receive messages from a topic and send an Envío de mensajes SMS para notificaciones de texto y alertas urgentes
  - **Complejidad:** Baja (4 nodos)

- **0208-apod-telegram-daily.json**
  - **Descripcion:** Send the Astronomy Picture of the day daily to a Telegram channel
  - **Complejidad:** Baja (3 nodos)

- **0258-rabbitmq-sms-alert.json**
  - **Descripcion:** Receive messages from a queue via RabbitMQ and send an Envío de mensajes SMS para notificaciones de texto y alertas urgentes
  - **Complejidad:** Baja (4 nodos)

- **0271-linear-alert-slack.json**
  - **Descripcion:** Integración con Slack para comunicación
  - **Complejidad:** Media (10 nodos)

- **0273-outlook-automated-email.json**
  - **Descripcion:** Create, add an attachment, and send a draft using the Microsoft Outlook node
  - **Complejidad:** Baja (5 nodos)

- **0274-discord-calendar-sync.json**
  - **Descripcion:** Integración con Discord para gestión de servidor
  - **Complejidad:** Media (9 nodos)

- **0286-slack-gilfoyle-chatbot.json**
  - **Descripcion:** Integración con Slack para comunicación
  - **Complejidad:** Alta (14 nodos)

- **0291-telegram-n8n-control.json**
  - **Descripcion:** Integración con Telegram para mensajería
  - **Complejidad:** Alta (12 nodos)

- **0293-email-validation-flow.json**
  - **Descripcion:** Email form
  - **Complejidad:** Media (7 nodos)

- **0300-nextcloud-deck-email.json**
  - **Descripcion:** Create Nextcloud Deck card from email
  - **Complejidad:** Baja (3 nodos)

- **0301-telegram-journal-reminder.json**
  - **Descripcion:** Daily Journal Reminder
  - **Complejidad:** Baja (3 nodos)

- **0304-email-xml-to-http-post.json**
  - **Descripcion:** ImapEmail, XmlToJson, POST-HTTP-Request
  - **Complejidad:** Baja (5 nodos)

- **0305-certificate-email-batch.json**
  - **Descripcion:** My workflow
  - **Complejidad:** Media (6 nodos)

- **0306-twake-message-trigger.json**
  - **Descripcion:** Send a message on Twake
  - **Complejidad:** Baja (2 nodos)

- **0307-send-sms-from-airtable.json**
  - **Descripcion:** Send Envío de mensajes SMS para notificaciones de texto y alertas urgentes to numbers stored in Airtable with Twilio
  - **Complejidad:** Baja (3 nodos)

- **0311-website-stock-alert.json**
  - **Descripcion:** Website check
  - **Complejidad:** Baja (5 nodos)

- **0315-icypeas-email-verifier.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Media (8 nodos)

- **0316-icypeas-email-search.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Baja (5 nodos)

- **0319-fastmail-mailbox-email.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Media (7 nodos)

- **0340-telegram-ai-bot.json**
  - **Descripcion:** Integración con Telegram para mensajería
  - **Complejidad:** Baja (4 nodos)

- **0341-hubspot-seguimiento-email.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Alta (12 nodos)

- **0342-lead-verification-madkudu-slack.json**
  - **Descripcion:** Integración con Slack para comunicación
  - **Complejidad:** Alta (11 nodos)

- **0343-validacion-email-madkudu-n8n.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Alta (12 nodos)

- **0344-form-contacto-telegram.json**
  - **Descripcion:** Integración con Telegram para mensajería
  - **Complejidad:** Alta (12 nodos)

- **0346-lead-alertas-n8n.json**
  - **Descripcion:** Automatización de lead alertas n8n
  - **Complejidad:** Media (8 nodos)

- **0350-slack-idea-capture.json**
  - **Descripcion:** Integración con Slack para comunicación
  - **Complejidad:** Media (8 nodos)

- **0351-slack-feature-ideas.json**
  - **Descripcion:** Integración con Slack para comunicación
  - **Complejidad:** Media (8 nodos)

- **0355-slack-error-notification.json**
  - **Descripcion:** Integración con Slack para comunicación
  - **Complejidad:** Baja (5 nodos)

- **0358-telegram-error-notification.json**
  - **Descripcion:** Integración con Telegram para mensajería
  - **Complejidad:** Baja (5 nodos)

- **0360-gmail-error-alert.json**
  - **Descripcion:** Automatización de gmail error alert
  - **Complejidad:** Baja (4 nodos)

- **0365-reporte-fallas-telegram.json**
  - **Descripcion:** Integración con Telegram para mensajería
  - **Complejidad:** Media (10 nodos)

- **0366-slack-to-clickup-tasks.json**
  - **Descripcion:** Integración con Slack para comunicación
  - **Complejidad:** Media (6 nodos)

- **0368-youtube-upload-create-playlist.json**
  - **Descripcion:** Upload video, create playlist and add video to playlist
  - **Complejidad:** Baja (5 nodos)

- **0371-telegram-chatbot-ai.json**
  - **Descripcion:** Integración con Telegram para mensajería
  - **Complejidad:** Alta (12 nodos)

- **0375-email-validation-domain-extraction.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Baja (5 nodos)

- **0376-unsubscribe-mautic.json**
  - **Descripcion:** Unsubscribe Mautic contacts from automated unsubscribe emails
  - **Complejidad:** Alta (16 nodos)

- **0380-hacker-news-monitor.json**
  - **Descripcion:** Automatización de hacker news monitor
  - **Complejidad:** Media (7 nodos)

- **0394-manejador-errores.json**
  - **Descripcion:** Automatización de manejador errores
  - **Complejidad:** Alta (11 nodos)

- **0407-n8n-totp-authentication.json**
  - **Descripcion:** TOTP VALIDATION (WITHOUT CREATING CREDENTIAL)
  - **Complejidad:** Baja (5 nodos)

- **0412-zendesk-unassigned-tickets-to-slack.json**
  - **Descripcion:** Zendesk-to-slack
  - **Complejidad:** Baja (5 nodos)

- **0421-alertas-azure-task.json**
  - **Descripcion:** Sistema de alertas y notificaciones
  - **Complejidad:** Baja (5 nodos)

- **0430-calvin-hobbes-discord-daily-comic.json**
  - **Descripcion:** Integración con Discord para gestión de servidor
  - **Complejidad:** Media (8 nodos)

- **0434-convertkit-list-subscribe-tag.json**
  - **Descripcion:** Add subscriber to form, create tag and subscriber to the tag
  - **Complejidad:** Baja (4 nodos)

- **0440-jira_telegram_webhook.json**
  - **Descripcion:** Integración con Telegram para mensajería
  - **Complejidad:** Media (8 nodos)

- **0446-telegram-welcome-bidirectional.json**
  - **Descripcion:** N8N Español - BOT
  - **Complejidad:** Baja (5 nodos)

- **0454-vps-upgrade-email-checker.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Media (7 nodos)

- **0457-vps-resource-monitor.json**
  - **Descripcion:** Automatización de vps resource monitor
  - **Complejidad:** Media (10 nodos)

- **0464-telegram-affirmations-daily.json**
  - **Descripcion:** Daily Text Affirmations
  - **Complejidad:** Baja (3 nodos)

- **0465-discord-webhook-message.json**
  - **Descripcion:** Discord Intro
  - **Complejidad:** Baja (2 nodos)

- **0466-mattermost-rss-monitor.json**
  - **Descripcion:** post to mattermost v2
  - **Complejidad:** Media (6 nodos)

- **0469-telegram-meteogram.json**
  - **Descripcion:** Telegram Weather Workflow
  - **Complejidad:** Baja (3 nodos)

- **0475-nocodebot-multilang.json**
  - **Descripcion:** N8N Español - NocodeBot
  - **Complejidad:** Media (7 nodos)

- **0480-calendar-voice-reminder.json**
  - **Descripcion:** Recordatorios automáticos
  - **Complejidad:** Alta (12 nodos)

- **0483-mailchimp-google-sheets-newsletter.json**
  - **Descripcion:** Automatización de mailchimp google sheets newsletter
  - **Complejidad:** Media (6 nodos)

- **0486-telegram-chinese-tutor.json**
  - **Descripcion:** Integración con Telegram para mensajería
  - **Complejidad:** Media (10 nodos)

- **0488-crear_cliente_segment.json**
  - **Descripcion:** Create a customer and add them to a segment in Customer.io
  - **Complejidad:** Baja (3 nodos)

- **0492-notion-tasks-slack.json**
  - **Descripcion:** Check To Do on Notion and send message on Slack
  - **Complejidad:** Media (6 nodos)

- **0495-gumroad-sale-trigger.json**
  - **Descripcion:** Receive updates when a sale is made in Gumroad
  - **Complejidad:** Baja (1 nodos)

- **0500-pagerduty-mattermost-update.json**
  - **Descripcion:** Automatización de pagerduty mattermost update
  - **Complejidad:** Baja (3 nodos)

- **0501-pager-duty-jira-integracion.json**
  - **Descripcion:** Automatización de pager duty jira integracion
  - **Complejidad:** Baja (5 nodos)

- **0503-error-alertas.json**
  - **Descripcion:** Automatización de error alertas
  - **Complejidad:** Baja (3 nodos)

- **0507-whatsapp-crm-automation.json**
  - **Descripcion:** AccountCraft WhatsApp Automation - Infridet
  - **Complejidad:** Media (6 nodos)

- **0513-email-tracking-pixel.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Media (6 nodos)

- **0516-email-classification-ai.json**
  - **Descripcion:** OpenAI e-mail classification - application
  - **Complejidad:** Media (10 nodos)

- **0520-daily-english-poems.json**
  - **Descripcion:** Daily poems in Telegram
  - **Complejidad:** Baja (4 nodos)

- **0521-mailchimp-subscribe.json**
  - **Descripcion:** Mailchimp
  - **Complejidad:** Baja (2 nodos)

- **0524-mattermost-instagram-stats.json**
  - **Descripcion:** StatsInstagram
  - **Complejidad:** Baja (5 nodos)

- **0525-the-hive-alerts.json**
  - **Descripcion:** TheHive
  - **Complejidad:** Media (7 nodos)

- **0528-twilio_trigger.json**
  - **Descripcion:** A workflow with the Twilio node
  - **Complejidad:** Baja (2 nodos)

- **0543-postmark-email-events-trigger.json**
  - **Descripcion:** Receive updates when an email is bounced or opened
  - **Complejidad:** Baja (1 nodos)

- **0546-thehive-email-iocs.json**
  - **Descripcion:** Email
  - **Complejidad:** Alta (15 nodos)

- **0553-aws-ses-email.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Baja (2 nodos)

- **0556-msg91-sms-flow.json**
  - **Descripcion:** Send an Envío de mensajes SMS para notificaciones de texto y alertas urgentes using MSG91
  - **Complejidad:** Baja (2 nodos)

- **0569-bitbucket-push-monitor.json**
  - **Descripcion:** Automatización de bitbucket push monitor
  - **Complejidad:** Baja (1 nodos)

- **0604-sms-alert-error-notification.json**
  - **Descripcion:** Send an Envío de mensajes SMS para notificaciones de texto y alertas urgentes when a workflow fails
  - **Complejidad:** Baja (2 nodos)

- **0605-mandrill-email.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Baja (2 nodos)

- **0615-send-email-example.json**
  - **Descripcion:** Correos electrónicos y notificaciones
  - **Complejidad:** Baja (2 nodos)

- **0620-58_telegram_coktai_random.json**
  - **Descripcion:** Receive updates from Telegram and send an image of a cocktail
  - **Complejidad:** Baja (3 nodos)



- **0113-webhook-html-response.json**
  - **Descripcion:** Automatización de webhook html response
  - **Complejidad:** Baja (2 nodos)

- **0362-country-query-formatter.json**
  - **Descripcion:** Automatización de country query formatter
  - **Complejidad:** Baja (4 nodos)

- **0367-tweets-publicador.json**
  - **Descripcion:** Automatización de tweets publicador
  - **Complejidad:** Media (6 nodos)

- **0369-youtube-description-automation.json**
  - **Descripcion:** Automatización de youtube description automation
  - **Complejidad:** Media (9 nodos)

- **0381-airtable-seo-metatags.json**
  - **Descripcion:** Automatización de airtable seo metatags
  - **Complejidad:** Media (6 nodos)

- **0382-webhook-google-sheets.json**
  - **Descripcion:** Automatización de webhook google sheets
  - **Complejidad:** Baja (2 nodos)

- **0383-workflow-estado.json**
  - **Descripcion:** Automatización de workflow estado
  - **Complejidad:** Alta (17 nodos)

- **0384-api-flutterflow-data.json**
  - **Descripcion:** Automatización de api flutterflow data
  - **Complejidad:** Media (9 nodos)

- **0385-convertapi-docx2pdf.json**
  - **Descripcion:** Automatización de convertapi docx2pdf
  - **Complejidad:** Baja (5 nodos)

- **0387-convertir-docx-a-pdf.json**
  - **Descripcion:** Automatización de convertir docx a pdf
  - **Complejidad:** Media (6 nodos)

- **0388-scrappey-test-schedule.json**
  - **Descripcion:** Automatización de scrappey test schedule
  - **Complejidad:** Baja (5 nodos)

- **0390-convertapi-xlsx-to-pdf-test.json**
  - **Descripcion:** Automatización de convertapi xlsx to pdf test
  - **Complejidad:** Baja (5 nodos)

- **0391-convertir-pptx-a-json.json**
  - **Descripcion:** Automatización de convertir pptx a json
  - **Complejidad:** Baja (5 nodos)

- **0393-2310_webpage-to-pdf_test.json**
  - **Descripcion:** Automatización de 2310 webpage to pdf test
  - **Complejidad:** Baja (5 nodos)

- **0395-html-to-pdf-automation.json**
  - **Descripcion:** Automatización de html to pdf automation
  - **Complejidad:** Media (6 nodos)

- **0396-convertapi-jpg-to-pdf.json**
  - **Descripcion:** Automatización de convertapi jpg to pdf
  - **Complejidad:** Baja (5 nodos)

- **0397-convertapi-pdf-conversion.json**
  - **Descripcion:** Automatización de convertapi pdf conversion
  - **Complejidad:** Baja (5 nodos)

- **0398-agente-ia-herramientas.json**
  - **Descripcion:** Automatización de agente ia herramientas
  - **Complejidad:** Alta (12 nodos)

- **0399-workflow-credentials-agent.json**
  - **Descripcion:** Automatización de workflow credentials agent
  - **Complejidad:** Alta (13 nodos)

- **0400-gmail-attachment-upload.json**
  - **Descripcion:** Automatización de gmail attachment upload
  - **Complejidad:** Baja (3 nodos)

- **0401-line-chatbot-memory-automation.json**
  - **Descripcion:** Automatización de line chatbot memory automation
  - **Complejidad:** Baja (3 nodos)

- **0408-confluence-template-automation.json**
  - **Descripcion:** Automatización de confluence template automation
  - **Complejidad:** Media (6 nodos)

- **0409-todoist-categorizador.json**
  - **Descripcion:** Automatización de todoist categorizador
  - **Complejidad:** Alta (12 nodos)

- **0426-token-management.json**
  - **Descripcion:** Automatización de token management
  - **Complejidad:** Media (9 nodos)

- **0428-libros-historicos-extractor.json**
  - **Descripcion:** Automatización de libros historicos extractor
  - **Complejidad:** Media (7 nodos)

- **0429-webflow-to-gsheets.json**
  - **Descripcion:** Automatización de webflow to gsheets
  - **Complejidad:** Media (7 nodos)

- **0431-blue-sky-rss.json**
  - **Descripcion:** Automatización de blue sky rss
  - **Complejidad:** Media (10 nodos)

- **0432-meal-plan-generator.json**
  - **Descripcion:** Automatización de meal plan generator
  - **Complejidad:** Media (10 nodos)

- **0436-cleaner-old-executions.json**
  - **Descripcion:** Automatización de cleaner old executions
  - **Complejidad:** Media (7 nodos)

- **0437-youtube-transcript-summary.json**
  - **Descripcion:** Automatización de youtube transcript summary
  - **Complejidad:** Alta (12 nodos)

- **0438-twitch-stream-checker.json**
  - **Descripcion:** Automatización de twitch stream checker
  - **Complejidad:** Media (7 nodos)

- **0439-hn-lookback-bot.json**
  - **Descripcion:** Automatización de hn lookback bot
  - **Complejidad:** Alta (13 nodos)

- **0441-youtube-video-summarizer.json**
  - **Descripcion:** Automatización de youtube video summarizer
  - **Complejidad:** Media (10 nodos)

- **0442-transform-image-to-lego-line.json**
  - **Descripcion:** Transform Image to Lego Style Using Line and Dall-E
  - **Complejidad:** Baja (5 nodos)

- **0443-comparativo-llm-pdf.json**
  - **Descripcion:** Automatización de comparativo llm pdf
  - **Complejidad:** Alta (11 nodos)

- **0444-google-drive-pii-detector.json**
  - **Descripcion:** Automatización de google drive pii detector
  - **Complejidad:** Media (10 nodos)

- **0447-perplexity-ai-chat.json**
  - **Descripcion:** Automatización de perplexity ai chat
  - **Complejidad:** Media (6 nodos)

- **0456-keywords-analysis.json**
  - **Descripcion:** Automatización de keywords analysis
  - **Complejidad:** Media (8 nodos)

- **0458-google-drive-batch-upload.json**
  - **Descripcion:** Automatización de google drive batch upload
  - **Complejidad:** Alta (13 nodos)

- **0459-imagen-gen-config.json**
  - **Descripcion:** Generación de imágenes automatizada con IA para contenido digital
  - **Complejidad:** Baja (3 nodos)

- **0461-milvus-rag-chatbot-flow.json**
  - **Descripcion:** RAG AI Agent with Milvus and Cohere
  - **Complejidad:** Alta (14 nodos)

- **0463-add-task-google.json**
  - **Descripcion:** Add task to tasklist
  - **Complejidad:** Baja (2 nodos)

- **0471-line-chatbot-ssh.json**
  - **Descripcion:** Automatización de line chatbot ssh
  - **Complejidad:** Media (6 nodos)

- **0473-line-chatbot-memory.json**
  - **Descripcion:** Automatización de line chatbot memory
  - **Complejidad:** Media (10 nodos)

- **0478-formulario-google-docs.json**
  - **Descripcion:** Automatización de formulario google docs
  - **Complejidad:** Media (8 nodos)

- **0479-ideas-para-post.json**
  - **Descripcion:** Automatización de ideas para post
  - **Complejidad:** Baja (5 nodos)

- **0482-invitaciones-google-sheets-n8n.json**
  - **Descripcion:** Automatización de invitaciones google sheets n8n
  - **Complejidad:** Alta (11 nodos)

- **0485-library-install.json**
  - **Descripcion:** Automatización de library install
  - **Complejidad:** Media (7 nodos)

- **0487-shopify-fulfillment-auto.json**
  - **Descripcion:** Automatización de shopify fulfillment auto
  - **Complejidad:** Alta (13 nodos)

- **0489-line-n8n-assistant.json**
  - **Descripcion:** Automatización de line n8n assistant
  - **Complejidad:** Baja (5 nodos)

- **0490-mediamarkt-deals.json**
  - **Descripcion:** Automatización de mediamarkt deals
  - **Complejidad:** Media (8 nodos)

- **0491-ai-chat-agent-memory.json**
  - **Descripcion:** Automatización de ai chat agent memory
  - **Complejidad:** Alta (12 nodos)

- **0496-gmail-news-to-linkedin.json**
  - **Descripcion:** Automatización de gmail news to linkedin
  - **Complejidad:** Media (7 nodos)

- **0497-incident-integracion.json**
  - **Descripcion:** Automatización de incident integracion
  - **Complejidad:** Alta (14 nodos)

- **0498-resume-screener.json**
  - **Descripcion:** Automatización de resume screener
  - **Complejidad:** Media (7 nodos)

- **0499-tts-generation.json**
  - **Descripcion:** Automatización de tts generation
  - **Complejidad:** Baja (4 nodos)

- **0502-chart-upload.json**
  - **Descripcion:** Automatización de chart upload
  - **Complejidad:** Baja (5 nodos)

- **0504-sharepoint-upload.json**
  - **Descripcion:** Automatización de sharepoint upload
  - **Complejidad:** Media (9 nodos)

- **0505-openai-image-generation-edit.json**
  - **Descripcion:** Automatización de openai image generation edit
  - **Complejidad:** Alta (11 nodos)

- **0506-facebook-lead-to-klicktipp.json**
  - **Descripcion:** Automatización de facebook lead to klicktipp
  - **Complejidad:** Baja (3 nodos)

- **0508-google-autocomplete-letter.json**
  - **Descripcion:** Automatización de google autocomplete letter
  - **Complejidad:** Alta (11 nodos)

- **0510-html-pdf-png-conversion.json**
  - **Descripcion:** Automatización de html pdf png conversion
  - **Complejidad:** Media (9 nodos)

- **0511-outlook-jira-ai-tickets.json**
  - **Descripcion:** Automatización de outlook jira ai tickets
  - **Complejidad:** Alta (12 nodos)

- **0512-web-scraper-structured.json**
  - **Descripcion:** Automatización de web scraper structured
  - **Complejidad:** Alta (11 nodos)

- **0515-auto-iniciar-flujos-n8n.json**
  - **Descripcion:** Automatización de auto iniciar flujos n8n
  - **Complejidad:** Baja (5 nodos)

- **0518-google-drive-pdf-to-html.json**
  - **Descripcion:** Automated PDF to HTML Conversion
  - **Complejidad:** Media (7 nodos)

- **0523-orlen-factura-automatizada.json**
  - **Descripcion:** Orlen
  - **Complejidad:** Media (10 nodos)

- **0564-line-chatbot-memory.json**
  - **Descripcion:** Automatización de line chatbot memory
  - **Complejidad:** Baja (1 nodos)


Workflows de automatización para plataformas de redes sociales y mensajería.

- **0115-facebook-profile-changes-mattermost.json**
  - **Descripción:** Recibe un mensaje en Mattermost cuando un usuario actualiza su perfil en Facebook
  - **Complejidad:** Baja (2 nodos)

- **0065-telegram-deploy-automation.json**
  - **Descripción:** Automatiza despliegues usando Telegram como trigger para controlar versiones de GitHub
  - **Complejidad:** Media (5 nodos)

- **0208-apod-telegram-daily.json**
  - **Descripción:** Envía diariamente la imagen astronómica del día (APOD) a un canal de Telegram
  - **Complejidad:** Baja (3 nodos)

- **0001-nostr-damus-ai-report.json**
  - **Descripción:** Sistema de reporteo con IA para Nostr, Gmail y Telegram
  - **Complejidad:** No disponible

- **0008-notion_linkedin_pub.json**
  - **Descripción:** Sincroniza contenido de Notion para publicación en LinkedIn
  - **Complejidad:** No disponible

- **0055-line-message-processing.json**
  - **Descripción:** Procesamiento de mensajes a través de webhooks de LINE
  - **Complejidad:** No disponible

- **0131-limpia_pacotes_telegram.json**
  - **Descripción:** Limpieza y mantenimiento de paquetes en Telegram
  - **Complejidad:** No disponible

- **0132-line-chatbot-memory.json**
  - **Descripción:** Chatbot de LINE con capacidad de memoria para extraer nombre y email
  - **Complejidad:** No disponible

- **0149-3066-from-community-Automate-Multi-Platform-Social-Media-Content-Creation-with.json**
  - **Descripción:** Automatiza la creación de contenido para múltiples redes sociales usando IA
  - **Complejidad:** No disponible

- **0156-news-ycombinator-telegram.json**
  - **Descripción:** Envía noticias de Hacker News a través de Telegram mediante solicitudes HTTP
  - **Complejidad:** No disponible

- **0158-2817-from-community-AI-social-media-caption-creator-creates-social-media-post.json**
  - **Descripción:** Generador de títulos para publicaciones en redes sociales usando IA y guardado en Airtable
  - **Complejidad:** No disponible

- **0177-youtube-telegram-monitor.json**
  - **Descripción:** Monitorización de YouTube con notificaciones a través de Telegram
  - **Complejidad:** No disponible

- **0191-3043-from-community-AI-powered-WhatsApp-assistant-for-restaurants-delivery.json**
  - **Descripción:** Asistente de IA para WhatsApp especializado en automatización de pedidos y entregas de restaurantes
  - **Complejidad:** No disponible

- **3186-Create-an-intelligent-Facebook-Messenger-chatbot-with-GPT-4o-mini-message-memory.json**
  - **Descripción:** Chatbot inteligente para Facebook Messenger con GPT-4o-mini y memoria de conversación
  - **Complejidad:** No disponible

- **6990-Auto-publish-social-videos-to-9-platforms-via-Google-Sheets-and-Blotato.json**
  - **Descripción:** Publicación automática de videos en 9 plataformas distintas usando Google Sheets y Blotato
  - **Complejidad:** No disponible

- **7597-Generate-LinkedIn-posts-with-GPT-4-preview-on-WhatsApp-and-auto-publish.json**
  - **Descripción:** Genera publicaciones de LinkedIn con GPT-4 a través de WhatsApp y las publica automáticamente
  - **Complejidad:** No disponible

- **6522-Save-new-files-received-on-Telegram-to-Google-Drive.json**
  - **Descripción:** Guarda automáticamente archivos recibidos en Telegram a Google Drive
  - **Complejidad:** No disponible

- **6001-Summarize-YouTube-video-transcripts-in-Discord-with-Gemini-and-Supabase.json**
  - **Descripción:** Resume transcripciones de videos de YouTube en Discord usando Gemini y Supabase
  - **Complejidad:** No disponible

- **10508-Manage-schedule-contacts-with-Telegram-Bot-using-GPT-4o-mini-Google-Services.json**
  - **Descripción:** Gestiona agenda y contactos usando bot de Telegram con GPT-4o-mini y servicios de Google
  - **Complejidad:** No disponible

- **11400-Send-WooCommerce-new-category-alert-via-WhatsApp-using-Rapiwa-API.json**
  - **Descripción:** Envía alertas de nuevas categorías de WooCommerce por WhatsApp usando API de Rapiwa
  - **Complejidad:** No disponible

- **9282-Automate-customer-support-with-WhatsApp-AI-assistant-for-Whatsapp-groups.json**
  - **Descripción:** Automatiza soporte al cliente con asistente de IA para WhatsApp y grupos
  - **Complejidad:** No disponible

Workflows de automatización para plataformas de comercio electrónico, pagos y tiendas online.

- **0080-shopify-product-alerts.json**
  - **Descripción:** Publica automáticamente nuevos productos de Shopify en Twitter y Telegram
  - **Complejidad:** Baja (3 nodos)

- **0261-mattermost-woocommerce-pedido.json**
  - **Descripción:** Envía notificación a Mattermost cuando se crea un pedido en WooCommerce
  - **Complejidad:** Baja (2 nodos)

- **2737-stripe-payment-link.json**
  - **Descripción:** Crea productos de Stripe y enlaces de pago automáticamente mediante formulario
  - **Complejidad:** Media (7 nodos)

- **0140-onfleet-shopify-task.json**
  - **Descripción:** Crea automáticamente tareas en Onfleet para nuevos cumplidos de Shopify
  - **Complejidad:** No disponible

- **0167-shopify-onfleet-tags-sync.json**
  - **Descripción:** Sincroniza etiquetas de Shopify con eventos en Onfleet
  - **Complejidad:** No disponible

- **0222-pipedrive-stripe-deal.json**
  - **Descripción:** Gestiona negociaciones y pagos entre Pipedrive y Stripe
  - **Complejidad:** No disponible

- **0223-stripe-organization-sync.json**
  - **Descripción:** Sincroniza organizaciones y clientes desde Stripe
  - **Complejidad:** No disponible

- **0224-pipedrive-stripe-product-sync.json**
  - **Descripción:** Sincroniza productos entre Pipedrive y Stripe
  - **Complejidad:** No disponible

- **0225-pipedrive-datagma-enrichment.json**
  - **Descripción:** Enriquece datos de contactos en Pipedrive usando Datagma
  - **Complejidad:** No disponible

- **0227-pipedrive-organization-sync.json**
  - **Descripción:** Sincroniza organizaciones de Pipedrive con Google Drive
  - **Complejidad:** No disponible

- **0240-shopify-zendesk-sync.json**
  - **Descripción:** Mantiene sincronización de ID de usuario y email entre Shopify y Zendesk
  - **Complejidad:** No disponible

- **0241-shopify-zendesk-sync.json**
  - **Descripción:** Sincroniza actualizaciones de pedidos de Shopify con Zendesk
  - **Complejidad:** No disponible

- **0242-2633-from-community-INSEE-company-data-enrichment-for-Agile-CRM-For-French.json**
  - **Descripción:** Enriquecimiento de datos de empresas francesas desde INSEE para Agile CRM
  - **Complejidad:** No disponible

- **0260-woo-product-flow.json**
  - **Descripción:** Crea, actualiza y obtiene productos de WooCommerce
  - **Complejidad:** No disponible

- **2731-woocommerce-chatbot.json**
  - **Descripción:** Chatbot para WooCommerce con atención al cliente automatizada
  - **Complejidad:** No disponible

- **3296-shopify-to-google-spreadsheet.json**
  - **Descripción:** Sincroniza productos de Shopify con Google Sheets
  - **Complejidad:** No disponible

- **0403-stripe-checkout-filters.json**
  - **Descripción:** Filtra y gestiona procesos de checkout en Stripe
  - **Complejidad:** No disponible

- **0082-shopify-reportes-semanal.json**
  - **Descripción:** Genera reportes semanales de ventas y métricas de Shopify
  - **Complejidad:** No disponible

- **0248-shopify-mautic-contact.json**
  - **Descripción:** Sincroniza contactos de Shopify con Mautic
  - **Complejidad:** No disponible

- **6519-Import-multiple-manufacturers-from-Google-Sheets-to-Shopware-6.json**
  - **Descripción:** Importa múltiples fabricantes desde Google Sheets a Shopware 6
  - **Complejidad:** No disponible

- **11400-Send-WooCommerce-new-category-alert-via-WhatsApp-using-Rapiwa-API.json**
  - **Descripción:** Envía alertas de nuevas categorías de WooCommerce por WhatsApp usando API de Rapiwa
  - **Complejidad:** No disponible

- **3114-chatbot_personal_shopper.json**
  - **Descripción:** Chatbot de compras personal para tiendas en línea
  - **Complejidad:** No disponible

- **3201-whatsapp-ai-sales-agent.json**
  - **Descripción:** Agente de ventas con IA para WhatsApp que gestiona pedidos y consultas
  - **Complejidad:** No disponible
# IA Y NLP - SECCIÓN CORREGIDA



La sección "IA y NLP" se organiza en las siguientes subcategorías:

### 1. Asistentes de Chat y Bots
### 2. RAG y Búsqueda Semántica
### 3. Generación de Imágenes y Videos
### 4. Procesamiento de Audio y Voz
### 5. Análisis de Documentos
### 6. Agentes Autónomos (ver sección separada)
### 7. Automatización Empresarial con IA
### 8. Generación de Contenido



### OpenAI / GPT

- **0003-line-chatgpt-image-flow.json**
  - **Descripción:** Generación de imágenes con ChatGPT para integración con LINE messenger, permitiendo a usuarios solicitar creaciones visuales directamente en chats.
  - **Complejidad:** Media (18 nodos)
  - **Tecnologías:** OpenAI GPT, LINE, Image Generation

- **0280-line-chatbot-agent.json**
  - **Descripción:** Agente de chatbot para LINE con capacidades avanzadas de procesamiento de lenguaje natural, respuesta automática y gestión de conversaciones multi-turno.
  - **Complejidad:** Alta (35 nodos)
  - **Tecnologías:** OpenAI, LINE, NLP, Context Management

- **0489-line-n8n-assistant.json**
  - **Descripción:** Asistente integrado de n8n para LINE con respuesta automática, soporte técnico y gestión de consultas de usuarios sobre workflows de automatización.
  - **Complejidad:** Media (22 nodos)
  - **Tecnologías:** OpenAI, LINE, n8n API, FAQ Management

- **0778-discord-ai-agent.json**
  - **Descripción:** Agente de IA para Discord con gestión de mensajes, moderación automática, respuesta a preguntas de comunidad y generación de contenido en tiempo real.
  - **Complejidad:** Alta (45 nodos)
  - **Tecnologías:** OpenAI GPT, Discord Bot, Moderation, Memory

- **0802-google-calendar-ai-agent.json**
  - **Descripción:** Agente de IA para gestión inteligente de Google Calendar que programa reuniones, responde consultas de disponibilidad y optimiza agendas automáticamente.
  - **Complejidad:** Media (28 nodos)
  - **Tecnologías:** OpenAI, Google Calendar API, Scheduling Logic

### Perplexity AI

- **0043-2682-from-community-Perplexity-research-to-HTML-AI-powered-content-creation.json**
  - **Descripción:** Transforma consultas simples en contenido integral y bien estructurado utilizando Perplexity AI para investigación y GPT-4 para transformación del contenido. Crea artículos HTML optimizados para web.
  - **Complejidad:** Media (14 nodos)
  - **Tecnologías:** Perplexity AI, OpenAI GPT-4, HTML Generation

- **0447-perplexity-ai-chat.json**
  - **Descripción:** Busqueda y respuesta en tiempo real con Perplexity AI para consultas de información, manteniendo fuentes actualizadas y contexto de conversación.
  - **Complejidad:** Baja (6 nodos)
  - **Tecnologías:** Perplexity API, Chat Context, Web Search

- **0628-perplexity-research.json**
  - **Descripción:** Sistema de investigación profunda con Perplexity AI para consultas complejas, extracción de múltiples fuentes y generación de reportes sintetizados.
  - **Complejidad:** Baja (5 nodos)
  - **Tecnologías:** Perplexity API, Research Logic, Source Aggregation

### Google Gemini

- **0435-openai-supabase-sql-chat.json**
  - **Descripción:** Chat de IA con base de datos Supabase SQL que permite a usuarios realizar consultas en lenguaje natural sobre datos estructurados, con traducción automática a SQL y resultados formatados.
  - **Complejidad:** Alta (42 nodos)
  - **Tecnologías:** OpenAI, Supabase PostgreSQL, Text-to-SQL, Query Builder

- **0713-bright-data-gemini-chat-enhancement.json**
  - **Descripción:** Automatización avanzada con Gemini AI para procesamiento de lenguaje natural, análisis semántico de conversaciones y generación de respuestas contextualmente relevantes.
  - **Complejidad:** Media (18 nodos)
  - **Tecnologías:** Google Gemini, NLP Processing, Context Analysis

- **0799-supabase-chat-ai.json**
  - **Descripción:** Agente autónomo que ejecuta múltiples pasos de automatización de forma inteligente para chat con documentos almacenados en Supabase con recuperación vectorial.
  - **Complejidad:** Media (11 nodos)
  - **Tecnologías:** Google Gemini, Supabase Vector Search, RAG

### Mistral AI

- **0289-mistral-cadena-hf.json**
  - **Descripción:** Cadena de modelos Mistral vía Hugging Face para generación de texto, traducción, resumen y automatización de tareas complejas con procesamiento distribuido de modelos.
  - **Complejidad:** Baja (4 nodos)
  - **Tecnologías:** Mistral AI, Hugging Face, Model Chaining

### Anthropic Claude

- **0290-feedback-openai-google.json**
  - **Descripción:** Sistema de retroalimentación integrado con OpenAI y Google para análisis automático de feedback de usuarios, clasificación de sentimiento y generación de insights accionables.
  - **Complejidad:** Alta (38 nodos)
  - **Tecnologías:** Anthropic Claude, Google APIs, Sentiment Analysis



### Pinecone

- **0285-bitcoin-chat-flow-pinecone.json**
  - **Descripción:** Chat de criptomonedas con base de datos vectorial Pinecone para búsqueda semántica y recuperación de contexto. Permite consultas sobre precios, tendencias y análisis histórico de Bitcoin.
  - **Complejidad:** Media (15 nodos)
  - **Tecnologías:** Pinecone Vector DB, OpenAI Embeddings, Bitcoin APIs, RAG

### Milvus

- **0461-milvus-rag-chatbot-flow.json**
  - **Descripción:** Chatbot RAG con base vectorial Milvus para recuperación de información relevante, generación de respuestas contextualizadas y soporte multi-idioma.
  - **Complejidad:** Media (14 nodos)
  - **Tecnologías:** Milvus Vector DB, OpenAI, RAG Architecture, Multi-language

### Qdrant

- **0779-rag-movie-recomendacion-qdrant-openai.json**
  - **Descripción:** Sistema de recomendación de películas con RAG + Qdrant que analiza preferencias de usuarios, busca similitudes semánticas y genera recomendaciones personalizadas.
  - **Complejidad:** Alta (52 nodos)
  - **Tecnologías:** Qdrant, OpenAI Embeddings, Movie Database, Recommendation Engine

### Documentos

- **0717-rag-chatbot-docs.json**
  - **Descripción:** Chatbot RAG para documentos empresariales que permite consultar PDFs, Word y otros formatos con búsqueda semántica y generación de respuestas basadas en contexto real.
  - **Complejidad:** Alta (50 nodos)
  - **Tecnologías:** OpenAI, Vector DB, Document Parsing, PDF Processing

- **0798-ai-chat-with-supabase-documents.json**
  - **Descripción:** Chat interactivo con documentos almacenados en Supabase, utilizando embeddings y búsqueda vectorial para recuperar información relevante y generar respuestas coherentes.
  - **Complejidad:** Alta (33 nodos)
  - **Tecnologías:** Supabase, OpenAI, Vector Search, Document Retrieval

- **0750-2621-from-community-AI-agent-to-chat-with-files-in-Supabase-Storage.json**
  - **Descripción:** Agente de IA para conversar con archivos almacenados en Supabase Storage, con indexación automática, búsqueda semántica y generación de respuestas contextualizadas.
  - **Complejidad:** Media (18 nodos)
  - **Tecnologías:** Supabase Storage, OpenAI, File Indexing, Vector Search



### DALL-E / OpenAI Image

- **0505-openai-image-generation-edit.json**
  - **Descripción:** Generación y edición de imágenes con DALL-E que permite crear contenido visual desde texto, modificar imágenes existentes y aplicar estilos artísticos automáticos.
  - **Complejidad:** Media (24 nodos)
  - **Tecnologías:** OpenAI DALL-E, Image Editing, Prompt Engineering

- **0691-openai-image-gen.json**
  - **Descripción:** Generación de imágenes OpenAI con múltiples variantes, ajuste de parámetros (tamaño, calidad, estilo) y almacenamiento automatizado de resultados.
  - **Complejidad:** Media (22 nodos)
  - **Tecnologías:** OpenAI DALL-E, Batch Generation, Storage Integration

### Vision / Image Analysis

- **0608-analisis-imagen-http.json**
  - **Descripción:** Automatiza análisis de imágenes recibidas vía HTTP, extracción de características, reconocimiento de objetos y generación de descripciones con IA visual.
  - **Complejidad:** Baja (3 nodos)
  - **Tecnologías:** OpenAI Vision, HTTP API, Image Processing

- **0609-trigger-leer-imagen-binaria.json**
  - **Descripción:** Trigger que lee imágenes en formato binario desde diversas fuentes, procesa el contenido y inicia workflows de análisis o generación con IA visual.
  - **Complejidad:** Baja (2 nodos)
  - **Tecnologías:** Binary Processing, Image Decoding, AI Vision

### Otros

- **0459-imagen-gen-config.json**
  - **Descripción:** Configuración base para generación de imágenes con parámetros personalizables, plantillas de prompts y control de calidad automatizado.
  - **Complejidad:** Baja (3 nodos)
  - **Tecnologías:** Image Generation API, Config Management, Prompt Templates



### ElevenLabs

- **0331-eleven-openai-audio-translation.json**
  - **Descripción:** Traducción de audio multilingüe con ElevenLabs + OpenAI que transcribe, traduce y genera voz natural, preservando el tono y expresividad del original.
  - **Complejidad:** Media (19 nodos)
  - **Tecnologías:** ElevenLabs, OpenAI Whisper, Audio Translation, Voice Synthesis

- **0378-elevenlabs-text-to-speech.json**
  - **Descripción:** Conversión de texto a voz con ElevenLabs para generar audio natural y automatizado, con múltiples voces, ajuste de velocidad y formato flexible de salida.
  - **Complejidad:** Baja (6 nodos)
  - **Tecnologías:** ElevenLabs TTS, Voice Cloning, Audio Generation

### OpenAI Whisper

- **0664-tts-openai.json**
  - **Descripción:** Sistema completo de texto a voz con OpenAI Whisper que incluye transcripción, detección de idioma, traducción y síntesis de voz de alta calidad.
  - **Complejidad:** Alta (35 nodos)
  - **Tecnologías:** OpenAI Whisper, Speech Recognition, TTS, Multi-language

### Otros

- **0499-tts-generation.json**
  - **Descripción:** Generación de texto a voz automatizada con selección de voces, control de parámetros (pitch, rate, volume) y soporte para múltiples formatos de audio.
  - **Complejidad:** Baja (4 nodos)
  - **Tecnologías:** TTS API, Audio Processing, Format Conversion

- **0534-speech-recognition-wit-ai.json**
  - **Descripción:** Reconocimiento de voz con Wit.ai para comandos de voz, transcripción en tiempo real y conversión de audio a texto con alta precisión.
  - **Complejidad:** Baja (2 nodos)
  - **Tecnologías:** Wit.ai, Speech Recognition, Real-time Transcription

- **0617-2547-from-community-Call-analyzer-with-AssemblyAI-transcription-and-OpenAI.json**
  - **Descripción:** Analizador de llamadas con transcripción AssemblyAI y análisis OpenAI que identifica speakers, extrae temas clave, genera resúmenes y detecta sentimiento en conversaciones.
  - **Complejidad:** Baja (7 nodos)
  - **Tecnologías:** AssemblyAI, OpenAI, Speaker Diarization, Call Analysis



### PDF Processing

- **0443-comparativo-llm-pdf.json**
  - **Descripción:** Comparación inteligente de documentos PDF usando LLMs, extracción de diferencias, análisis de contenido y generación de reportes de comparación estructurados.
  - **Complejidad:** Media (11 nodos)
  - **Tecnologías:** OpenAI, PDF Processing, Document Comparison, NLP

### OCR / Document Extraction

- **0269-download-pdf-robot.json**
  - **Descripción:** Robot automatizado para descarga de PDFs desde múltiples fuentes, organización de archivos y preparación para procesamiento posterior con IA.
  - **Complejidad:** Baja (3 nodos)
  - **Tecnologías:** HTTP Downloads, File Management, PDF Handling

### Content Generation

- **0124-2669-from-community-Auto-generate-documentation-for-n8n-workflows-with-GPT-and.json**
  - **Descripción:** Sistema automático de documentación para instancias de n8n usando Docsify.js. Sirve un sitio web dinámico que permite ver todos los workflows, sus descripciones y documentación generada por IA.
  - **Complejidad:** Media (20 nodos)
  - **Tecnologías:** GPT, Docsify.js, Documentation Generation, n8n API

- **0712-2849-from-community-Content-generator-for-WordPress-v3.json**
  - **Descripción:** Generador de contenido para WordPress v3 con Anthropic Claude, generación de artículos SEO-optimizados, imágenes automáticas y publicación programada en blogs.
  - **Complejidad:** Media (24 nodos)
  - **Tecnologías:** Anthropic Claude, WordPress API, SEO Optimization, Content Scheduling



### CRM Integration

- **0051-2999-from-community-AI-agent-for-PetShop-appointments-Agente-de-IA-para.json**
  - **Descripción:** Agente de IA para Pet Shops que automatiza servicio al cliente, gestión de citas, recordatorios y seguimiento de clientes. Transforma la experiencia del cliente y optimiza operaciones.
  - **Complejidad:** Alta (39 nodos)
  - **Tecnologías:** OpenAI, CRM Integration, Scheduling, Customer Service

### Data Analysis

- **0824-rag-financial-report-gen.json**
  - **Descripción:** Generación de reportes financieros con RAG que analiza datos, identifica tendencias, crea visualizaciones y produce informes ejecutivos con insights accionables.
  - **Complejidad:** Alta (48 nodos)
  - **Tecnologías:** RAG, Financial Analysis, Data Visualization, Report Generation



### Daily Content

- **0520-daily-english-poems.json**
  - **Descripción:** Agente autónomo que ejecuta múltiples pasos de automatización de forma inteligente para generar poemas en inglés diarios con variaciones de estilo y tema.
  - **Complejidad:** Baja (4 nodos)
  - **Tecnologías:** OpenAI, Poetry Generation, Creative Writing, Daily Automation

- **0544-n8n-daily-ai-news.json**
  - **Descripción:** Agente autónomo que ejecuta múltiples pasos de automatización de forma inteligente para recopilar noticias de IA, generar resúmenes y distribuir contenido curado.
  - **Complejidad:** Media (12 nodos)
  - **Tecnologías:** News APIs, OpenAI, Content Curation, Distribution

### Social Media

- **0439-hn-lookback-bot.json**
  - **Descripción:** Scraper de Hacker News que extrae jobs y noticias de tecnología automáticamente, filtra contenido relevante y genera posts para redes sociales.
  - **Complejidad:** Media (13 nodos)
  - **Tecnologías:** Hacker News API, Web Scraping, Content Filtering, Social Media

- **0718-crypto-news-sentiment-bot.json**
  - **Descripción:** Bot de noticias y sentimiento cripto que monitorea fuentes, analiza sentimiento de mercado y genera alertas sobre tendencias de criptomonedas.
  - **Complejidad:** Media (30 nodos)
  - **Tecnologías:** Crypto APIs, Sentiment Analysis, News Monitoring, Alerting



### Web Search

- **0209-google-search-url-generator.json**
  - **Descripción:** Generador de URLs de búsqueda de Google automatizado, creación de queries optimizadas y extracción de resultados para análisis posterior.
  - **Complejidad:** Baja (5 nodos)
  - **Tecnologías:** Google Search API, Query Generation, URL Management

- **0514-2643-from-community-Intelligent-web-query-and-semantic-re-ranking-flow-using.json**
  - **Descripción:** Sistema potente y totalmente automatizado de consultas web y reordenamiento semántico que permite búsquedas precisas y detalladas con ranking inteligente de resultados.
  - **Complejidad:** Media (12 nodos)
  - **Tecnologías:** Semantic Search, Re-ranking, Web Query, AI Ranking

### Research

- **0662-brave-search-chatbot.json**
  - **Descripción:** Chatbot con Brave Search para búsquedas web en tiempo real, respuestas contextuales y seguimiento de conversación multi-turno con fuentes verificadas.
  - **Complejidad:** Media (15 nodos)
  - **Tecnologías:** Brave Search, OpenAI, Real-time Search, Conversation Memory



