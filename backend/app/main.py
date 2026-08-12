from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.exception_manager import Exception_Manager


app = FastAPI(
    title="SmartGym API",
    description="Sistema Backend para la gestion financiera y operativa de un gimnasio. Implementa algunas correcciones de errores y funciones faltantes en la version previa, como un mecanismo de migraciones.",
    version="1.1.0",
    swagger_ui_parameters={"persistAuthorization": True},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Exception_Manager.exception_register(app)
