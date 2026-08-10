import os
import sys

from dotenv import load_dotenv

# Carga de variables de entorno en el proceso actual.
load_dotenv()


class Settings:
    """
    Clase base para cargar y almacenar las variables de configuracion del sistema.
    """

    # Carga de variables de entorno para la configuracion del sistema. Se definen ciertos
    # valores por defecto en caso de que no se encuentren algunas.
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "smartgym_v2")

    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    access_token_duration = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")

    # Si no se encuentra el usuario de base de datos, su clave o la clave API definida,
    # se imprime el error por consola y se cancela la ejecucion del sistema
    if not DB_USER:
        print("\nERROR: Usuario de base de datos no encontrado.\n")
        sys.exit(1)

    if not DB_PASSWORD:
        print("\nERROR: Clave de base de datos no encontrada.\n")
        sys.exit(1)

    if not SECRET_KEY:
        print("\nERROR: Clave API secreta no encontrada.\n")
        sys.exit(1)

    # Configuracion de URL para conexion con base de datos.
    DB_URL = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Conversion de valor para la duracion de tokens de acceso.
    ACCESS_TOKEN_EXPIRE_MINUTES = int(access_token_duration)


# Instanciacion de clase de configuracion.
settings = Settings()
