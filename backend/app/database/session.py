from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings

# Creacion de motor para conexion asincrona con la base de datos.
engine_db = create_async_engine(settings.DB_URL, echo=True)

# Creador de sesiones asincronas con la base de datos.
async_session_local = async_sessionmaker(
    bind=engine_db,
    autocommit=False,
    autoflush=True,
    class_=AsyncSession,
    expire_on_commit=False,
)


# Creacion de base delarativa para manipulacion de modelos ORM.
class Base(DeclarativeBase):
    pass


# Funcion inyectable para crear conexiones asincronas con la base de datos.
async def get_session_db():
    """
    Permite obtener una sesion asincrona para interactuar con la base de datos.
    """
    async with async_session_local() as session:
        yield session


# Funcion para inicializar las tablas de la base de datos.
async def create_db():
    """
    Crea las tablas y sus relaciones en la base de datos partiendo de los modelos de
    SQLAlchemy, si no existen previamente.
    """
    async with engine_db.begin() as conn:
        print("\nIniciando la creacion de esquema de base de datos.\n")
        await conn.run_sync(Base.metadata.create_all)
        print("\nEsquema de base de datos creado exitosamente.\n")
