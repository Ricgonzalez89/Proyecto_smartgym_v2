from enum import Enum


class Rol_Enum(str, Enum):
    """
    Enumeracion para estandarizar los roles existentes en el sistema.
    """

    ADMINISTRACION = "Administración"
    FINANZAS = "Finanzas"
    ENTRENADORES = "Entrenadores"
    CLIENTES = "Clientes"


class Estado_Oper_Maquina_Enum(str, Enum):
    """
    Estados operativos para las maquinas (usado tambien dentro de los tickets de
    mantenimiento).
    """

    ACTIVA = "Activa"
    MANTENIMIENTO = "En mantenimiento"
    FUERA_SERVICIO = "Fuera de servicio"


class Status_Reserva_Enum(str, Enum):
    """
    Estatus validos para las reservas de sesiones deportivas.
    """

    PENDIENTE = "Pendiente"
    ASISTENTE = "Asistente"
    NO_ASISTENTE = "No asistente"
    CANCELADA = "Cancelada"


class Status_Sesion_Enum(str, Enum):
    """
    Estatus validos para una sesion deportiva.
    """

    PROGRAMADA = "Programada"
    FINALIZADA = "Finalizada"
    CANCELADA = "Cancelada"


class Actividad_Membresia_Enum(str, Enum):
    """
    Estados de actividad posibles para una membresia de un cliente.
    """

    ACTIVA = "Activa"
    VENCIDA = "Vencida"
    POR_VENCER = "Por vencer"
    INACTIVA = "Inactiva"


class Descripcion_Pago_Enum(str, Enum):
    """
    Descripciones posibles de los pagos realizados por un cliente para un plan.
    """

    ADQUISICION = "Adquision de plan"
    RENOVACION = "Renovacion de plan"


class Categoria_Producto_Enum(str, Enum):
    """
    Enumeracion de las categorias existentes de productos.
    """

    VESTIMENTA = "Vestimenta"
    ACCESORIOS = "Accesorios"
    SUPLEMENTOS = "Suplementos"
