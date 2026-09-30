---
name: template-creator
description: "Crear o actualizar una skill personal de plantilla reutilizable a partir de un ejemplo o artefacto solicitado."
---

Extrae del ejemplo la estructura, las variables y las decisiones que deben conservarse. Crea una skill en .agents/skills con nombre y descripción precisos, y añade solo los recursos necesarios. Guarda como plantilla los archivos reutilizables que el usuario tenga derecho a distribuir; evita conservar datos personales del ejemplo si no son parte de la plantilla.

Valida la plantilla generando un ejemplo nuevo y revisa el resultado visual cuando corresponda. Las URLs de Drive necesitan una conexión disponible para obtener el archivo; si falta, solicita el contenido imprescindible. No modifiques la caché de plugins de Codex.

Consulta [compatibilidad cloud](../../cloud/COMPATIBILITY.md) si faltan herramientas o dependencias.
