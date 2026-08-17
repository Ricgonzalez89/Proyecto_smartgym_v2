from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.core.constants import Actividad_Membresia_Enum
from app.database.session import Base


class Membresia(Base):
    """
    Modelo ORM para la tabla 'membresia' y las membresias de cliente registradas.
    """

    __tablename__ = "membresia"

    id_membresia = Column(Integer, primary_key=True, autoincrement=True)
    cedula_cliente = Column(String(20), ForeignKey("cliente.cedula_cliente"))
    id_plan = Column(Integer, ForeignKey("plan.id_plan"))
    fecha_inicio = Column(DateTime(timezone=True), nullable=False)
    fecha_venci = Column(DateTime(timezone=True), nullable=False)
    actividad_membre = Column(
        String(20), default=Actividad_Membresia_Enum.INACTIVA.value, nullable=False
    )
    status = Column(Boolean, default=True, nullable=False)

    cliente = relationship("Cliente", back_populates="membresia")
    plan = relationship("Plan", back_populates="membresia")
    pago = relationship("Pago_Membresia", back_populates="membresia")
