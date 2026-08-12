from pydantic import BaseModel


class Error_Scheme(BaseModel):
    """
    Esquema base para el envio de respuestas de error del servidor al cliente.
    Contiene los siguientes campos:
     - error: Tipo de error producido (recurso no encontrado, conflicto, falta de autenticacion, etc.).
     - codigoInterno: Codigo identificativo del error generado.
     - mensaje: Detalle del error obtenido.
     - timestamp: Fecha y hora de generacion del error (con zona horaria Venezolana, UTC-04).
    """

    error: str
    codigoInterno: str
    mensaje: str | dict
    timestamp: str
