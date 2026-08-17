from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.database.session import Base


class Categoria_Maquina(Base):
    """
    Modelo ORM de la tabla 'categoria_maquina' y las categorias de maquinas registradas.
    """

    __tablename__ = "categoria_maquina"

    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    descripcion_cate = Column(String(40), unique=True, nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    maquina = relationship("Maquina", back_populates="categoria")
