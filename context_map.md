# Mapa de Contexto del Sistema - Reservas IA

## Arquitectura y Capas
1. **Entry Point (`app.py`)**: Maneja rutas HTTP de Flask y controladores principales.
2. **Capa de Modelos (`models/reserva_model.py`)**: Entidades de datos gestionadas con SQLAlchemy.
3. **Capa de Servicios (`services/weather_service.py`)**: Lógica de integración con APIs externas (OpenWeather API).

## Reglas de Negocio
- Toda consulta de clima requiere manejo de excepciones y valor por defecto (fallback).
- Las reservas deben incluir cliente, email y fecha.
- Las variables sensibles deben consumirse siempre desde `os.getenv()` vía `.env`.