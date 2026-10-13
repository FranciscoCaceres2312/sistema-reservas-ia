import os
from flask import Flask, jsonify, request, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from models.reserva_model import Base, Reserva
from services.weather_service import WeatherService

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///reservas.db")
engine = create_engine(DATABASE_URL, echo=False)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

weather_service = WeatherService()

@app.route('/api/estado', methods=['GET'])
def obtener_estado() -> Response:
    clima = weather_service.obtener_clima_mendoza()
    return jsonify({
        "status": "online",
        "servicio_clima": clima
    })

@app.route('/api/reservar', methods=['POST'])
def crear_reserva() -> Response:
    datos = request.get_json() or {}
    session: Session = SessionLocal()
    
    nueva_reserva = Reserva(
        nombre_cliente=datos.get('nombre', 'Anonimo'),
        email=datos.get('email', 'sin_email@ejemplo.com'),
        fecha_reserva=datos.get('fecha', '2026-10-01')
    )
    
    session.add(nueva_reserva)
    session.commit()
    reserva_dict = nueva_reserva.to_dict()
    session.close()
    
    return jsonify({"mensaje": "Reserva creada con exito", "reserva": reserva_dict})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(port=port, debug=True)