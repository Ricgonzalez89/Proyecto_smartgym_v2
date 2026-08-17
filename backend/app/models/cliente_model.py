from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.session import Base


class Cliente(Base):
    """
    Modelo ORM para la tabla 'cliente' y los clientes registrados.
    """

    __tablename__ = "cliente"

    cedula_cliente = Column(String(20), primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), unique=True)
    nombre_cli = Column(String(40), nullable=False)
    apellido_cli = Column(String(40), nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    usuario = relationship("Usuario", back_populates="cliente")
    biometria = relationship("Biometria_Cliente", back_populates="cliente")
    reserva = relationship("Reserva", back_populates="cliente")
    membresia = relationship("Membresia", back_populates="cliente")
    acceso = relationship("Acceso", back_populates="cliente")
    venta = relationship("Venta_Tienda", back_populates="cliente")
