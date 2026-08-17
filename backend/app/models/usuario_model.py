from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.session import Base


class Usuario(Base):
    """
    Modelo ORM para la tabla 'usuario'. Representa a los usuarios registrados.
    """

    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    id_rol = Column(Integer, ForeignKey("rol.id_rol"))
    correo = Column(String(40), unique=True, nullable=False)
    clave_hash = Column(String(100), nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    rol = relationship("Rol", back_populates="usuario")
    entrenador = relationship("Entrenador", back_populates="usuario")
    cliente = relationship("Cliente", back_populates="usuario")
    ticket = relationship("Ticker_Mantenimiento", back_populates="usuario")
