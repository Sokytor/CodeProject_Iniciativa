---
name: sokytor-github-cloud
description: Preparar proyectos de Sokytor antes de subirlos o crear sus repositorios en GitHub, incluyendo reglas, skills portables y CodeGraph para Codex Cloud.
---

Al crear o subir un proyecto de Sokytor, aplica el kit antes del primer push:

`python3 tools/apply-codex-kit.py /ruta/absoluta/al/proyecto`

El script está junto a la raíz de este repositorio; ejecútalo usando su ruta absoluta si el proyecto está en otro directorio. También puede usarse la plantilla privada `Sokytor/codex-project-template`, que ya contiene el kit. Las reglas se combinan con el `AGENTS.md` existente; los conflictos con archivos personalizados se reportan y requieren una combinación consciente, no un reemplazo ciego.

Revisa los cambios preparados, excluye secretos, credenciales y resultados generados, comprueba la configuración con `python3 tools/verify-codex-kit.py` dentro del proyecto y prepara CodeGraph con `bash .agents/cloud/bootstrap.sh`. Crea el repositorio privado salvo una instrucción del usuario que indique otra visibilidad. Conserva las ramas y el historial de repositorios existentes.

Si el usuario solicita subir nuevas skills, incluye solo recursos que tenga derecho a distribuir y registra sus dependencias. Las skills que necesitan conectores no adquieren esos permisos por copiarse. No copies la configuración de autenticación del equipo.

Al publicar un entorno de Codex Cloud, añade `bash .agents/cloud/bootstrap.sh` a su preparación, además de las dependencias propias del proyecto. No confundas un kit subido a GitHub con un entorno cloud publicado.
