from datetime import datetime
from typing import Optional


class DescargaOffline:
    """
    Registra cuándo un usuario descarga un tour para uso offline.
    """

    def __init__(
        self,
        id_descarga: int,
        id_usuario: int,
        id_tour: int,
        dispositivo: str = "",
        fecha_descarga: Optional[datetime] = None
    ):
        self.id_descarga = id_descarga
        self.id_usuario = id_usuario
        self.id_tour = id_tour
        self.dispositivo = dispositivo
        self.fecha_descarga = fecha_descarga or datetime.now()

    def to_dict(self) -> dict:
        return {
            "id": self.id_descarga,
            "usuario_id": self.id_usuario,
            "tour_id": self.id_tour,
            "dispositivo": self.dispositivo,
            "fecha_descarga": self.fecha_descarga.isoformat()
        }

    def __repr__(self) -> str:
        return f"<DescargaOffline {self.id_descarga}: Tour {self.id_tour}>"
