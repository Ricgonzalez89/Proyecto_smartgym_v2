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


class Biometria_Cliente(Base):
    """
    Modelo ORM para la tabla 'biometria_cliente' y las evaluaciones biometricas registradas.
    """

    __tablename__ = "biometria_cliente"

    id_biometria = Column(Integer, primary_key=True, autoincrement=True)
    cedula_cliente = Column(String(20), ForeignKey("cliente.cedula_cliente"))
    cedula_entre = Column(String(20), ForeignKey("entrenador.cedula_entre"))
    peso_cli = Column(Numeric(5, 2), nullable=False)
    estatura_cli = Column(Numeric(5, 2), nullable=False)
    porc_grasa_cli = Column(Numeric(5, 2), nullable=False)
    observaciones = Column(String, nullable=True)
    fecha_biometria = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    status = Column(Boolean, default=True, nullable=False)

    cliente = relationship("Cliente", back_populates="biometria")
    entrenador = relationship("Entrenador", back_populates="biometria")
