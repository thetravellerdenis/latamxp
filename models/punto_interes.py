import math


class PuntoInteres:
    """
    Representa un punto de interés en el mapa dentro de un tour.
    """

    def __init__(
        self,
        id_punto: int,
        id_tour: int,
        lat: float,
        lng: float,
        nombre: str,
        descripcion: str = "",
        orden: int = 0
    ):
        self.id_punto = id_punto
        self.id_tour = id_tour
        self.lat = lat
        self.lng = lng
        self.nombre = nombre
        self.descripcion = descripcion
        self.orden = orden

    def get_distancia(self, lat: float, lng: float) -> float:
        R = 6371
        dlat = math.radians(lat - self.lat)
        dlng = math.radians(lng - self.lng)
        a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(self.lat)) * math.cos(math.radians(lat)) * math.sin(dlng / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    def get_distancia_metros(self, lat: float, lng: float) -> float:
        return self.get_distancia(lat, lng) * 1000

    def to_dict(self) -> dict:
        return {
            "id": self.id_punto,
            "tour_id": self.id_tour,
            "lat": self.lat,
            "lng": self.lng,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "orden": self.orden
        }

    def __repr__(self) -> str:
        return f"<PuntoInteres {self.id_punto}: {self.nombre}>"
