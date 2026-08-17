from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    String,
    DateTime,
    Boolean,
    ForeignKey,
    func,
)
from sqlalchemy.orm import relationship

from app.database.session import Base


class Venta_Tienda(Base):
    """
    Modelo ORM para la tabla 'venta_tienda' y las ventas de productos registradas.
    """

    __tablename__ = "venta_tienda"

    id_venta = Column(Integer, primary_key=True, autoincrement=True)
    cedula_cliente = Column(String(20), ForeignKey("cliente.cedula_cliente"))
    fecha_venta = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    monto_venta = Column(Numeric(10, 2), nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    detalle = relationship("Venta_Detalle", back_populates="venta")
    cliente = relationship("Cliente", back_populates="venta")
