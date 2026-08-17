from sqlalchemy import Column, Integer, Numeric, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database.session import Base


class Entrenador(Base):
    """
    Modelo ORM para la tabla 'entrenador' y los entrenadores registrados.
    """

    __tablename__ = "entrenador"

    cedula_entre = Column(String(20), primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), unique=True)
    nombre_entre = Column(String(40), nullable=False)
    apellido_entre = Column(String(40), nullable=False)
    sueldo_entre = Column(Numeric(10, 2), nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    usuario = relationship("Usuario", back_populates="entrenador")
    biometria = relationship("Biometria_Cliente", back_populates="entrenador")
    sesion = relationship("Sesion", back_populates="entrenador")
