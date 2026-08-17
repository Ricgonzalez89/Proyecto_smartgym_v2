from sqlalchemy import Column, Integer, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.session import Base


class Venta_Detalle(Base):
    """
    Modelo ORM para la tabla 'venta_detalle' y los detalles de las ventas registradas.
    """

    __tablename__ = "venta_detalle"

    id_detalle = Column(Integer, primary_key=True, autoincrement=True)
    id_venta = Column(Integer, ForeignKey("venta_tienda.id_venta"))
    id_lote = Column(Integer, ForeignKey("lote_producto.id_lote"))
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric(10, 2), nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    venta = relationship("Venta_Tienda", back_populates="detalle")
    lote = relationship("Lote_Producto", back_populates="detalle")
