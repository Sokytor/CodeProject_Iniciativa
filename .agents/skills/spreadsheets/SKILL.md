---
name: spreadsheets
description: "Crear, editar o analizar archivos de hojas de cálculo y preparar entregas para Google Sheets."
---

Prefiere el runtime de hojas de cálculo de Codex si el entorno lo ofrece. Si falta, usa openpyxl para XLSX; para CSV utiliza lectores que respeten delimitadores, codificación y tipos. Conserva las fórmulas cuando el usuario deba modificar el modelo.

Comprueba referencias, totales y formatos con valores representativos. openpyxl guarda fórmulas pero no las calcula: usa un motor disponible, como LibreOffice, para recalcular y verificar valores. No presentes resultados almacenados como cálculos nuevos sin comprobarlos.

Google Sheets necesita una conexión y una herramienta compatible; verifica que el archivo se haya importado antes de entregar un enlace de Google.

Consulta [compatibilidad cloud](../../cloud/COMPATIBILITY.md) si faltan herramientas o dependencias.
