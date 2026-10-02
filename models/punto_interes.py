import math
from app.extensions import db

class PuntoInteres(db.Model):
    __tablename__ = 'punto_interes'
    id_punto = db.Column(db.Integer, primary_key=True)
    id_tour = db.Column(db.Integer, db.ForeignKey('tour.id_tour'), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, default="")
    orden = db.Column(db.Integer, default=0)

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