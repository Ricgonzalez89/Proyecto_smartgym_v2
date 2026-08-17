from fastapi.security import HTTPBearer
from pwdlib import PasswordHash
import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import HTTPException, status
from datetime import datetime, timezone, timedelta

# Importacion para obtener la clave API, algoritmo de cifrado y duracion de los tokens.
from app.core.config import settings


# Instanciacion de esquema HTTPBearer para la proteccion de endpoints y el envio de credenciales.
http_bearer_scheme = HTTPBearer()

# Instanciacion de contexto de hasheo para el manejo de claves de usuario.
# Se usa la configuracion recomendada.
password_hasher = PasswordHash.recommended()


def get_password_hash(plain_password: str) -> str:
    """
    Funcion para obtener el hash de una contraseña en texto plano.
    """

    return password_hasher.hash(plain_password)


def verify_password(plain_password: str, password_hash: str) -> str:
    """
    Funcion para verificar si una contraseña coincide con el hash guardado en base de datos.
    """

    return password_hasher.verify(plain_password, password_hash)


def create_access_token(
    token_data: dict, expires_delta: timedelta | None = None
) -> str:
    """
    Funcion para obtener tokens de acceso (JWT) para los usuarios.
    """

    # Se copian los datos ingresados por el usuario para su codificacion.
    to_encode = token_data.copy()

    # Si se ha ingresado un tiempo de expiracion, se asigna al token a partir de la fecha y hora
    # actual (segun el huso venezolano, UTC-04). Si no, se usa la duracion predeterminada.
    if expires_delta:
        expire = datetime.now(timezone(timedelta(hours=-4))) + expires_delta
    else:
        expire = datetime.now(timezone(timedelta(hours=-4))) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    # Se actualiza la carga util del token con su tiempo de expiracion.
    to_encode.update({"exp": expire})

    # Se codifica la carga util, aplicando la clave secreta y algoritmo definidos para su firma,
    # y se retorna el token al usuario.
    return jwt.encode(
        payload=to_encode, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )


def validate_access_token(token: str) -> dict:
    """
    Funcion para comprobar la validez de un token de acceso.
    """

    try:
        # Se decodifica el token y se obtiene su propietario (nombre de usuario).
        token_data = jwt.decode(
            token, key=settings.SECRET_KEY, algorithms=settings.ALGORITHM
        )
        username = token_data.get("sub")

        # Si no posee un usuario asociado, se lanza una excepcion.
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No se pudieron validar las credenciales.",
                headers={"WWW-Authenticate": "Bearer"},
            )

    # Si ocurre un error durante la decodificacion, se lanza una excepcion.
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se pudieron validar las credenciales.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Se retorna la carga util decodificada.
    return token_data
