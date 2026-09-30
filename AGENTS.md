# Instrucciones del proyecto

<!-- SOKYTOR_CLOUD_START -->
## Entorno de Sokytor para Codex

El usuario ha autorizado preparar CodeGraph y conservar esta configuración en sus repositorios actuales y futuros.

- Antes de explorar o modificar código, ejecuta `bash .agents/cloud/bootstrap.sh` si el índice o el ejecutable faltan; en un entorno retomado, sincroniza con `.agents/bin/codegraph sync`.
- Usa CodeGraph antes de buscar o leer código: `codegraph_explore` si el MCP está disponible, o `.agents/bin/codegraph explore "archivo, símbolos o pregunta"`. Usa las herramientas normales para documentación y configuración, o para una búsqueda que CodeGraph no resuelva. Si falla la preparación, explica el error y continúa con las herramientas disponibles sin afirmar que CodeGraph funciona.
- El índice `.codegraph/` y el ejecutable `.agents/.runtime/` se generan dentro del entorno; no se suben a GitHub. Los recursos de `.agents/` quedan fuera del índice para priorizar el código del proyecto.
- Las skills del repositorio están en `.agents/skills/`. Lee la skill que corresponda al trabajo; no cargues todas ni ejecutes procesos ajenos a la petición. Consulta `.agents/cloud/COMPATIBILITY.md` si necesita conectores o herramientas de la app.
- Conserva las instrucciones propias del proyecto, sus versiones, sus secretos y su sistema de publicación. Ejecuta comprobaciones adecuadas al cambio. No declares un despliegue exitoso sin verificar su resultado.
- Los cambios en una web conectada a Cloudflare se publican cuando llegan a su rama de producción en GitHub. Las ediciones que solo existen en el entorno no cambian el enlace compartido.
- Cuando el usuario pida subir o crear otro proyecto de GitHub, usa la skill `sokytor-github-cloud` y aplica este kit antes de publicar. Crea los nuevos repositorios de Sokytor como privados, salvo una instrucción explícita distinta.
<!-- SOKYTOR_CLOUD_END -->
