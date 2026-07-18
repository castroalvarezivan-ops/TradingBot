# GIT GUIDE
## TradingBot Professional

---

# FASE 1 — Instalación de Git

## Verificar si Git está instalado

```powershell
git --version
```

Si no está instalado:

https://git-scm.com/download/win

---

# FASE 2 — Crear el repositorio local

Entrar al proyecto

```powershell
cd "C:\Users\Usuario\OneDrive\Documents\TradingBots\TradingBot"
```

Inicializar Git

```powershell
git init
```

Verificar

```powershell
git status
```

---

# FASE 3 — Agregar archivos

Agregar todos los archivos

```powershell
git add .
```

Verificar

```powershell
git status
```

Los archivos aparecerán preparados para el commit.

---

# FASE 4 — Configuración inicial

Nombre

```powershell
git config --global user.name "IVAN CASTRO"
```

Correo

```powershell
git config --global user.email "castroalvarezivan@gmail.com"
```

Verificar

```powershell
git config --global --list
```

---

# FASE 5 — Primer Commit

```powershell
git commit -m "V2.6.3 Stable - Analytics Engine Base"
```

---

# FASE 6 — Conectar con GitHub

Crear repositorio en GitHub.

Luego ejecutar:

```powershell
git branch -M main
```

```powershell
git remote add origin URL_DEL_REPOSITORIO
```

```powershell
git push -u origin main
```

---

# Flujo de trabajo diario

Guardar cambios

```powershell
git add .
```

Crear versión

```powershell
git commit -m "V2.6.X"
```

Subir cambios

```powershell
git push
```

---

# Comandos útiles

Estado

```powershell
git status
```

Historial

```powershell
git log --oneline
```

Ver ramas

```powershell
git branch
```

Ver repositorio remoto

```powershell
git remote -v
```

---

# Versiones del TradingBot

V2.6.3
Primer commit profesional del proyecto.

Próximos hitos

- V2.6.4
- V2.7
- V2.8
- V3.0