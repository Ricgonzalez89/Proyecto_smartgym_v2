from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.database.session import Base


class Producto(Base):
    """
    Modelo ORM para la tabla 'producto' y los productos fisicos registrados (en general).
    """

    __tablename__ = "producto"

    id_producto = Column(Integer, primary_key=True, autoincrement=True)
    descripcion_produ = Column(String(40), nullable=False, unique=True)
    categoria_produ = Column(String(30), nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    lote = relationship("Lote_Producto", back_populates="producto")
