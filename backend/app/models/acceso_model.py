from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from app.database.session import Base


class Acceso(Base):
    """
    Modelo ORM para la tabla 'acceso' y las entradas fisicas registradas en el sistema.
    """

    __tablename__ = "acceso"

    id_entrada = Column(Integer, primary_key=True, autoincrement=True)
    cedula_cliente = Column(String(20), ForeignKey("cliente.cedula_cliente"))
    fecha_entrada = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    admision_entrada = Column(Boolean, nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    cliente = relationship("Cliente", back_populates="acceso")
