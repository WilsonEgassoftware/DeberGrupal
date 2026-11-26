# Puertos, protocolos y redes (insumo para el diagrama de P2)

| Servicio | IP interna | Puerto contenedor | Publicado al host | Protocolo | Redes |
|---|---|---|---|---|---|
| frontend-service | 172.28.0.10 | 5000 | Sí → `localhost:8080` | HTTP | public-net + internal-net |
| internal-admin-service | 172.28.0.20 | 5001 | No | HTTP | internal-net |
| fake-metadata | 172.28.0.30 | 80 | No | HTTP | internal-net |

## Flujo legítimo
Usuario → (HTTP 8080) → frontend-service

## Flujo abusado (SSRF)
Usuario → frontend-service `/preview?url=...` → internal-admin-service:5001 / fake-metadata:80

## Puntos de fallo / punto ciego de confianza
- `frontend-service` no valida el destino de `/preview` (CWE-918).
- Los servicios internos confían en cualquier petición que venga de `internal-net` (sin autenticación).
- `frontend-service` es el único nodo con pie en ambas redes (pivote).

## Nota sobre la IP de metadata
AWS usa 169.254.169.254. En el lab se usa 172.28.0.30 porque Docker no garantiza
asignar direcciones link-local. La mecánica del ataque es idéntica.
