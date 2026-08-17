from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.database.session import Base


class Disciplina(Base):
    """
    Modelo ORM para la tabla 'disciplina' y las disciplinas deportivas registradas.
    """

    __tablename__ = "disciplina"

    id_disciplina = Column(Integer, primary_key=True, autoincrement=True)
    descripcion_disci = Column(String(40), unique=True, nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    sesion = relationship("Sesion", back_populates="disciplina")
