from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Reserva(Base):
    __tablename__ = 'reservas'

    id: int = Column(Integer, primary_key=True, autoincrement=True) # type: ignore
    nombre_cliente: str = Column(String(100), nullable=False) # type: ignore
    email: str = Column(String(100), nullable=False) # type: ignore
    fecha_reserva: str = Column(String(20), nullable=False) # type: ignore
    estado: str = Column(String(20), default="CONFIRMADA") # type: ignore
    creado_el: datetime = Column(DateTime, default=datetime.utcnow) # type: ignore

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre_cliente": self.nombre_cliente,
            "email": self.email,
            "fecha_reserva": self.fecha_reserva,
            "estado": self.estado
        }