from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.database.session import Base


class Rol(Base):
    """
    Modelo ORM para la tabla 'rol'. Representa los roles registrados.
    """

    __tablename__ = "rol"

    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    descripcion_rol = Column(String(40), unique=True, nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    usuario = relationship("Usuario", back_populates="rol")
