# Flujo de trabajo en Git

- `main`: protegida, solo entrega final (la integra P1).
- `develop`: integración del equipo.
- `feature/<nombre-tarea>`: una por tarea, siempre creada desde `develop`.

## Paso a paso para cada tarea
```bash
git checkout develop
git pull
git checkout -b feature/mi-tarea
# ... trabajar ...
git add .
git commit -m "feat: descripción corta"
git push -u origin feature/mi-tarea
```
Luego abrir Merge Request (feature → develop). **Otra persona** lo revisa y aprueba.
Antes de pedir merge: `docker compose up --build` debe funcionar sin errores.

## Prefijos de commit
`feat:` nuevo · `fix:` corrección · `docs:` documentación · `chore:` mantenimiento
