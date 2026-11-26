# Laboratorio ABET — SSRF en Arquitecturas Distribuidas

ITIZ2302 — Sistemas Distribuidos · Grupo 4

> ⚠️ Entorno **vulnerable a propósito**, solo para uso académico, aislado en Docker.
> Todas las credenciales son ficticias. No desplegar fuera de este laboratorio.

## Requisitos
- Docker Desktop (o Docker Engine + Compose v2)
- Git

## Levantar el entorno
```bash
cd lab-environment
docker compose up --build
```

## Verificar que funciona
En otra terminal:
```bash
curl http://localhost:8080/health
```
Los servicios internos NO deben responder desde tu máquina:
```bash
curl http://localhost:5001/health   # debe fallar (puerto no publicado)
```

## Apagar y limpiar
```bash
docker compose down               # apagar
docker compose down --rmi local   # apagar y borrar imágenes del lab
```

## Estructura
| Carpeta | Contenido | Responsable |
|---|---|---|
| `lab-environment/` | docker-compose y los 3 servicios | P1 |
| `attack-guide/` | guía y scripts del ataque | P3 |
| `hardening/` | contramedidas y re-ejecución | P4 |
| `docs/` | documento final, diagramas, bitácora IA | P2, P5 |

Flujo de Git: `docs/flujo-git.md` · Puertos y redes: `docs/puertos-y-protocolos.md`
