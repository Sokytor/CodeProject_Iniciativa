# Compatibilidad de skills en Codex Cloud

Las skills describen un proceso; no instalan conectores ni transfieren permisos.

- CodeGraph: runtime fijado en 1.6.0 y lockfile. Ejecuta `bash .agents/cloud/bootstrap.sh`. Puede usarse por CLI sin MCP.
- imagegen, openai-docs, skill-creator, skill-installer, pdf y cloudflare-deploy: versiones públicas de openai/skills, con sus licencias y recursos. imagegen necesita una herramienta de imágenes disponible; su alternativa CLI requiere una clave autorizada. Cloudflare necesita autenticación del usuario y herramientas compatibles.
- documents, presentations y spreadsheets: adaptaciones portables propias. Prefieren el runtime de Codex y admiten bibliotecas Python en un entorno sin ese runtime. La revisión visual requiere LibreOffice y/o Poppler; indica cuando no pueda hacerse.
- visualize: Mermaid o HTML autónomo; la vista inline depende del visor de la conversación.
- template-creator: guarda plantillas y skills dentro de .agents/skills. Una fuente externa necesita su conexión.
- write-page, maintain-space, organize-space y manage-schedules: requieren las herramientas conectadas de Pages y de programación.
- excel-live-control: requiere una sesión de Excel conectada al entorno; la sesión local del Mac no se transfiere.
- pets, create-pet y update-pet: requieren el conector, especificaciones y validadores de mascotas del producto.
- plugin-management: requiere las herramientas de gestión del producto para realizar cambios de conexiones.

Las adaptaciones no son copias de los recursos internos de la app. No incluyen claves, credenciales, runtimes propietarios ni acceso automático a servicios. Se aplican las herramientas y permisos que la tarea tenga disponibles.

En un entorno cloud nuevo, añade `bash .agents/cloud/bootstrap.sh` a la preparación junto a las dependencias del proyecto. AGENTS.md también solicita esta preparación si el entorno aún no tiene CodeGraph. Si el acceso a npm está bloqueado, debe permitirse registry.npmjs.org durante la instalación.
