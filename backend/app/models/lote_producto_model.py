from sqlalchemy import Column, Integer, Numeric, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.session import Base


class Lote_Producto(Base):
    """
    Modelo ORM para la tabla 'lote_producto' y los lotes de productos registrados.
    """

    __tablename__ = "lote_producto"

    id_lote = Column(Integer, primary_key=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey("producto.id_producto"))
    precio_actual = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)
    fecha_vencimiento = Column(Date, nullable=True)
    status = Column(Boolean, default=True, nullable=False)

    producto = relationship("Producto", back_populates="lote")
    detalle = relationship("Venta_Detalle", back_populates="lote")
