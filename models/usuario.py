from datetime import datetime
from typing import List, Optional


class Usuario:
    """
    Representa un usuario del sistema LatamXP.
    """

    def __init__(
        self,
        id_usuario: int,
        nombre: str,
        email: str,
        password_hash: str,
        fecha_registro: Optional[datetime] = None,
        idioma_preferido: str = "es",
        activo: bool = True
    ):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.password_hash = password_hash
        self.fecha_registro = fecha_registro or datetime.now()
        self.idioma_preferido = idioma_preferido
        self.activo = activo
        self._pedidos = []
        self._valoraciones = []

    def agregar_pedido(self, pedido: 'Pedido') -> None:
        self._pedidos.append(pedido)

    def agregar_valoracion(self, valoracion: 'Valoracion') -> None:
        self._valoraciones.append(valoracion)

    def get_pedidos(self) -> List['Pedido']:
        return self._pedidos.copy()

    def get_pedidos_activos(self) -> List['Pedido']:
        return [p for p in self._pedidos if p.estado == "paid"]

    def get_valoraciones(self) -> List['Valoracion']:
        return self._valoraciones.copy()

    def to_dict(self) -> dict:
        return {
            "id": self.id_usuario,
            "nombre": self.nombre,
            "email": self.email,
            "fecha_registro": self.fecha_registro.isoformat(),
            "idioma_preferido": self.idioma_preferido,
            "activo": self.activo
        }

    def __repr__(self) -> str:
        return f"<Usuario {self.id_usuario}: {self.nombre}>"
