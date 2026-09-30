---
name: documents
description: "Crear o editar documentos Word y entregas destinadas a Google Docs, con revisión visual del resultado."
---

Trabaja en los archivos del entorno cloud. Usa el motor de documentos de Codex cuando esté disponible; si falta, usa python-docx para generar y editar DOCX. Para cambios con revisiones, conserva la estructura OOXML y verifica las marcas de revisión, no solo el texto.

Antes de entregar, convierte una copia a PDF con LibreOffice si está disponible y revisa las páginas renderizadas. Comprueba títulos, tablas, saltos y cortes. Si no hay conversor, informa que la revisión visual quedó pendiente. Mantén el DOCX editable.

La entrega en Google Docs requiere una conexión autorizada y una herramienta de creación o importación de documentos. Un DOCX local no demuestra que el documento exista en Google Drive.

Consulta [compatibilidad cloud](../../cloud/COMPATIBILITY.md) si faltan herramientas o dependencias.
