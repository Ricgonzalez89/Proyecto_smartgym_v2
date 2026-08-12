from datetime import datetime, timezone, timedelta
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError
from starlette.exceptions import HTTPException as Starlette_HTTP_Exception

from app.core.errors import App_Exception
from app.schemes.error_scheme import Error_Scheme


class Exception_Manager:
    """
    Clase gestora de las excepciones generadas por el sistema, durante la validacion de datos,
    errores HTTP o por violaciones de la integridad de la base de datos. Captura ciertos errores
    y los retorna de forma legible al cliente y con la estructura documentada.
    """

    @staticmethod
    def exception_register(app: FastAPI):
        """
        Funcion para registrar los manejadores de excepciones como parte de la aplicacion
        """
        # Se adjuntan todos los maneadores de excepciones a la instancia de FastAPI, de forma
        # que todos los errores generados que coincidan con las clases manejadas sean
        # "capturados" y retornados al cliente con un formato estandar.
        app.add_exception_handler(
            App_Exception, Exception_Manager.app_exception_handler
        )
        app.add_exception_handler(
            RequestValidationError, Exception_Manager.data_validation_exception_handler
        )
        app.add_exception_handler(
            IntegrityError, Exception_Manager.integrity_exception_handler
        )
        app.add_exception_handler(
            Starlette_HTTP_Exception, Exception_Manager.http_exception_handler
        )

    @staticmethod
    async def app_exception_handler(request: Request, exception: App_Exception):
        """
        Manejador de excepciones personalizadas de la aplicacion.
        """

        # Se extrae la informacion de la excepcion de la aplicacion segun el esquema definido.
        exception_data = Error_Scheme(
            error=exception.error,
            codigoInterno=exception.internal_code,
            mensaje=exception.message,
            timestamp=exception.timestamp,
        )

        # Se retorna el mensaje de error con formato JSON.
        return JSONResponse(
            status_code=exception.status_code,
            content=exception_data.model_dump(exclude_none=True),
        )

    @staticmethod
    async def data_validation_exception_handler(
        request: Request, exception: RequestValidationError
    ):
        """
        Manejador de excepciones de validacion de datos.
        """

        # Diccionario base para la especificacion de los campos erroneos.
        dict_error = {}

        # Se construye el mensaje de error con el campo invalido y la descripcion del error.
        for error in exception.errors():
            dict_error[f"{error['loc'][1]}"] = error["msg"]

        # Se construye el mensaje de error final con la informacion anterior.
        exception_data = Error_Scheme(
            error="Bad Request",
            codigoInterno="DATA_VALIDATION_EXCEPTION",
            mensaje=dict_error,
            timestamp=datetime.now(timezone(timedelta(hours=-4))).isoformat(),
        )

        # Se retorna al cliente el error en formato JSON.
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=exception_data.model_dump(exclude_none=True),
        )

    @staticmethod
    async def integrity_exception_handler(request: Request, exception: IntegrityError):
        """
        Manejador de excepciones de integridad de base de datos (producidos por SQLAlchemy).
        """

        # Definicion del mensaje de error final. Se omite la especificacion exacta de la causa
        # para proteger los detalles de la base de datos, abogando por un mensaje generico.
        exception_data = Error_Scheme(
            error="Database conflict",
            codigoInterno="INTEGRITY_EXCEPTION",
            mensaje="Error de integridad en base de datos (ej. registro duplicado o valores nulos no permitidos).",
            timestamp=datetime.now(timezone(timedelta(hours=-4))).isoformat(),
        )

        # Se retorna al cliente en formato JSON.
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content=exception_data.model_dump(exclude_none=True),
        )

    @staticmethod
    async def http_exception_handler(
        request: Request, exception: Starlette_HTTP_Exception
    ):
        """
        Manejador de errores HTTP, generados por Starlette
        """

        # Defincion del mensaje de error final con sus detalles exactos.
        exception_data = Error_Scheme(
            error="HTTP error",
            codigoInterno="HTTP_EXCEPTION",
            mensaje=f"{exception.detail}",
            timestamp=datetime.now(timezone(timedelta(hours=-4))).isoformat(),
        )

        # Retorno del error al cliente en formato JSON.
        return JSONResponse(
            status_code=exception.status_code,
            content=exception_data.model_dump(exclude_none=True),
        )
