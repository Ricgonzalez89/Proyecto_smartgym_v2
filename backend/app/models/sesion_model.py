from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.core.constants import Status_Sesion_Enum
from app.database.session import Base


class Sesion(Base):
    """
    Modelo ORM para la tabla 'sesion' y las esiones deportivas registradas.
    """

    __tablename__ = "sesion"

    id_sesion = Column(Integer, primary_key=True, autoincrement=True)
    cedula_entre = Column(String(20), ForeignKey("entrenador.cedula_entre"))
    id_disciplina = Column(Integer, ForeignKey("disciplina.id_disciplina"))
    nombre_sesion = Column(String(100), nullable=False)
    fecha_inicio = Column(DateTime(timezone=True), nullable=False)
    fecha_final = Column(DateTime(timezone=True), nullable=False)
    cupos_disp = Column(Integer, nullable=False)
    status = Column(
        String(30), default=Status_Sesion_Enum.PROGRAMADA.value, nullable=False
    )

    entrenador = relationship("Entrenador", back_populates="sesion")
    disciplina = relationship("Disciplina", back_populates="sesion")
    reserva = relationship("Reserva", back_populates="sesion")
