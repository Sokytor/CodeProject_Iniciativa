---
name: codegraph-cloud
description: Preparar o consultar CodeGraph en este repositorio al investigar código, corregir errores o implementar cambios en Codex Cloud.
---

Ejecuta `bash .agents/cloud/bootstrap.sh` desde la raíz cuando falte el índice o el runtime. La preparación instala la versión fijada en el lockfile y construye el índice; no requiere acceso a la configuración de tu Mac.

Para código indexado, utiliza primero el MCP `codegraph_explore` si está disponible, con la ruta del repositorio como `projectPath`. En cualquier otro caso, usa `.agents/bin/codegraph explore "archivo o símbolos"`. Es una consulta del código y sus relaciones, no una prueba de su corrección.

Después de editar, sincroniza con `.agents/bin/codegraph sync` si no hay seguimiento activo o la respuesta avisa de contenido desactualizado. Comprueba el cambio con las pruebas o la compilación del proyecto. Si no hay resultados relevantes, lee solo los archivos necesarios. No inventes herramientas MCP ni afirmes que están conectadas por tener la CLI.
