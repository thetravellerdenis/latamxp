from datetime import datetime
from typing import Optional


class Pedido:
    """
    Representa un pedido (compra) de un tour por parte de un usuario.
    """

    ESTADOS_VALIDOS = ["pending", "paid", "failed", "refunded"]

    def __init__(
        self,
        id_pedido: int,
        id_usuario: int,
        id_tour: int,
        monto: float,
        metodo_pago: str,
        fecha: Optional[datetime] = None,
        estado: str = "pending"
    ):
        if estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido. Debe ser uno de: {self.ESTADOS_VALIDOS}")

        self.id_pedido = id_pedido
        self.id_usuario = id_usuario
        self.id_tour = id_tour
        self.monto = monto
        self.metodo_pago = metodo_pago
        self.fecha = fecha or datetime.now()
        self.estado = estado
        self._tour = None

    def marcar_pagado(self) -> None:
        self.estado = "paid"

    def marcar_fallido(self) -> None:
        self.estado = "failed"

    def marcar_reembolsado(self) -> None:
        self.estado = "refunded"

    def set_tour(self, tour: 'Tour') -> None:
        self._tour = tour

    def get_tour(self) -> Optional['Tour']:
        return self._tour

    def to_dict(self) -> dict:
        return {
            "id": self.id_pedido,
            "usuario_id": self.id_usuario,
            "tour_id": self.id_tour,
            "monto": self.monto,
            "metodo_pago": self.metodo_pago,
            "fecha": self.fecha.isoformat(),
            "estado": self.estado
        }

    def __repr__(self) -> str:
        return f"<Pedido {self.id_pedido}: {self.estado}>"
