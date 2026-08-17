from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.core.constants import Estado_Oper_Maquina_Enum
from app.database.session import Base


class Maquina(Base):
    """
    Modelo ORM para la tabla 'maquina' y las maquinas registradas en el inventario.
    """

    __tablename__ = "maquina"

    id_maquina = Column(Integer, primary_key=True, autoincrement=True)
    id_categoria = Column(Integer, ForeignKey("categoria_maquina.id_categoria"))
    nombre_maq = Column(String(40), nullable=False)
    descripcion_maq = Column(String, nullable=False)
    estado_oper_maq = Column(
        String(30), default=Estado_Oper_Maquina_Enum.ACTIVA.value, nullable=False
    )
    status = Column(Boolean, default=True, nullable=False)

    categoria = relationship("Categoria_Maquina", back_populates="maquina")
    ticket = relationship("Ticket_Mantenimiento", back_populates="maquina")
