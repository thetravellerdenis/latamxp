from datetime import datetime
from typing import Optional


class Valoracion:
    """
    Representa una valoración (reseña) de un tour realizada por un usuario.
    """

    def __init__(
        self,
        id_valoracion: int,
        id_usuario: int,
        id_tour: int,
        puntuacion: int,
        comentario: str = "",
        fecha: Optional[datetime] = None
    ):
        if not 1 <= puntuacion <= 5:
            raise ValueError("La puntuación debe ser un número entre 1 y 5.")

        self.id_valoracion = id_valoracion
        self.id_usuario = id_usuario
        self.id_tour = id_tour
        self.puntuacion = puntuacion
        self.comentario = comentario
        self.fecha = fecha or datetime.now()

    def es_positiva(self) -> bool:
        return self.puntuacion >= 4

    def es_negativa(self) -> bool:
        return self.puntuacion <= 2

    def to_dict(self) -> dict:
        return {
            "id": self.id_valoracion,
            "usuario_id": self.id_usuario,
            "tour_id": self.id_tour,
            "puntuacion": self.puntuacion,
            "comentario": self.comentario,
            "fecha": self.fecha.isoformat()
        }

    def __repr__(self) -> str:
        return f"<Valoracion {self.id_valoracion}: {self.puntuacion}/5>"
