from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    DateTime,
    Boolean,
    ForeignKey,
    func,
)
from sqlalchemy.orm import relationship

from app.database.session import Base


class Pago_Membresia(Base):
    """
    Modelo ORM para la tabla 'pago_membresia' y los pagos de membresia registados.
    """

    __tablename__ = "pago_membresia"

    nro_pago = Column(Integer, primary_key=True, autoincrement=True)
    id_membresia = Column(Integer, ForeignKey("membresia.id_membresia"))
    nro_referencia = Column(String(20), unique=True, nullable=False)
    monto_pago = Column(Numeric(10, 2), nullable=False)
    fecha_pago = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    descripcion_pago = Column(String(40), nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    membresia = relationship("Membresia", back_populates="pago")
