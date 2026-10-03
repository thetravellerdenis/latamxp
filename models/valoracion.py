from datetime import datetime
from app.extensions import db

class Valoracion(db.Model):
    __tablename__ = 'valoracion'
    id_valoracion = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_tour = db.Column(db.Integer, db.ForeignKey('tour.id_tour'), nullable=False)
    puntuacion = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Text, default="")
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

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
            "fecha": self.fecha.isoformat() if self.fecha else None
        }