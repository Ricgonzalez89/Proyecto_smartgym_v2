from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from app.core.constants import Status_Reserva_Enum
from app.database.session import Base


class Reserva(Base):
    """
    Modelo ORM para la tabla 'reserva' y las reservas de inscripciones registradas.
    """

    __tablename__ = "reserva"

    id_inscripcion = Column(Integer, primary_key=True, autoincrement=True)
    cedula_cliente = Column(String(20), ForeignKey("cliente.cedula_cliente"))
    id_sesion = Column(Integer, ForeignKey("sesion.id_sesion"))
    fecha_inscripcion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    status = Column(
        String(30), default=Status_Reserva_Enum.PENDIENTE.value, nullable=False
    )

    sesion = relationship("Sesion", back_populates="reserva")
    cliente = relationship("Cliente", back_populates="reserva")
