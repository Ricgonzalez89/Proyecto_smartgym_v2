from datetime import datetime, timedelta, timezone


class App_Exception(Exception):
    """
    Clase base para estandarizar la informacion de las excepciones generadas en la aplicacion.
    """

    def __init__(
        self,
        status_code: int = 500,
        error: str = "Internal Server Error",
        message: str = "Error en el sistema",
        internal_code: str = "SERVER_EXCEPTION",
    ):
        self.status_code = status_code
        self.error = error
        self.message = message
        self.internal_code = internal_code
        self.timestamp = datetime.now(timezone(timedelta(hours=-4))).isoformat()
        super().__init__(self.message)


class Bad_Request_Exception(App_Exception):
    """
    Errores 400 - Bad Request, para fallas en el cuerpo de las solicitudes.
    """

    def __init__(self, message: str, internal_code: str = "BAD_REQUEST_EXCEPTION"):
        super().__init__(400, "Bad Request", message, internal_code)


class Unauthorized_Exception(App_Exception):
    """
    Errores 401 - Unauthorized, para faltas de tokens de acceso o tokens expirados.
    """

    def __init__(self, message: str, internal_code: str = "UNAUTHORIZED_EXCEPTION"):
        super().__init__(401, "Unauthorized", message, internal_code)


class Forbidden_Exception(App_Exception):
    """
    Errores 403 - Forbidden, para errores por falta de permisos/autorizacion.
    """

    def __init__(self, message: str, internal_code: str = "FORBIDDEN_EXCEPTION"):
        super().__init__(403, "Forbidden", message, internal_code)


class Not_Found_Exception(App_Exception):
    """
    Errores 404 - Not Found, para errores por recursos no encontrados.
    """

    def __init__(self, message: str, internal_code: str = "NOT_FOUND_EXCEPTION"):
        super().__init__(404, "Not Found", message, internal_code)


class Conflict_Exception(App_Exception):
    """
    Errores 409 - Conflict, por conflictos con reglas de negocio o solicitudes bien formuladas
    por el cliente pero improcesables por violaciones de restricciones internas del sistema
    (como valores duplicados en campos que deben contener registros distintos).
    El codigo interno debe modificarse para reflejar el conflicto subyacente.
    """

    def __init__(self, message: str, internal_code: str = "CONFLICT_EXCEPTION"):
        super().__init__(409, "Conflict", message, internal_code)
