from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    DateTime,
    ForeignKey,
    Boolean,
    func,
)
from sqlalchemy.orm import relationship

from app.database.session import Base


class Ticket_Mantenimiento(Base):
    """
    Modelo ORM para la tabla 'ticket_mantenimiento' y los tickets registrados.
    """

    __tablename__ = "ticket_mantenimiento"

    id_ticket = Column(Integer, primary_key=True, autoincrement=True)
    id_maquina = Column(Integer, ForeignKey("maquina.id_maquina"))
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))
    descripcion_ticket = Column(String, nullable=False)
    fecha_falla = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualiz = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        onupdate=func.now(),
    )
    fecha_resolucion = Column(
        DateTime(timezone=True), server_default=None, nullable=True
    )
    costo_resolucion = Column(Numeric(10, 2), default=None, nullable=True)
    estado_maquina = Column(String(30), nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    maquina = relationship("Maquina", back_populates="ticket")
    usuario = relationship("Usuario", back_populates="ticket")
