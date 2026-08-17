from sqlalchemy import Column, Integer, String, Numeric, Boolean
from sqlalchemy.orm import relationship

from app.database.session import Base


class Plan(Base):
    """
    Modelo ORM para la tabla 'plan' y los planes de membrsia registrados.
    """

    __tablename__ = "plan"

    id_plan = Column(Integer, primary_key=True, autoincrement=True)
    descripcion_plan = Column(String(40), unique=True, nullable=False)
    costo_plan = Column(Numeric(10, 2), nullable=False)
    duracion_plan = Column(Integer, nullable=False)
    status = Column(Boolean, default=True, nullable=False)

    membresia = relationship("Membresia", back_populates="plan")
