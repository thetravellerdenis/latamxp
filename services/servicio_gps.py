from typing import List, Tuple
from models.punto_interes import PuntoInteres
from models.tour import Tour


class ServicioGPS:
    """
    Servicio que maneja la geolocalización y activación de audios por GPS.
    """

    def __init__(self):
        self._lat_actual = None
        self._lng_actual = None

    def actualizar_posicion(self, lat: float, lng: float) -> None:
        self._lat_actual = lat
        self._lng_actual = lng

    def get_posicion(self) -> Tuple[float, float]:
        if self._lat_actual is None or self._lng_actual is None:
            raise ValueError("No se ha establecido una posición.")
        return self._lat_actual, self._lng_actual

    def get_puntos_cercanos(self, tour: Tour, radio_metros: float = 50) -> List[Tuple[PuntoInteres, float]]:
        if self._lat_actual is None or self._lng_actual is None:
            return []
        cercanos = []
        for punto in tour.get_puntos():
            distancia = punto.get_distancia_metros(self._lat_actual, self._lng_actual)
            if distancia <= radio_metros:
                cercanos.append((punto, distancia))
        return sorted(cercanos, key=lambda x: x[1])
