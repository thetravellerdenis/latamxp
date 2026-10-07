from datetime import datetime
from app.extensions import db

class DescargaOffline(db.Model):
    __tablename__ = 'descarga_offline'
    id_descarga = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_tour = db.Column(db.Integer, db.ForeignKey('tour.id_tour'), nullable=False)
    dispositivo = db.Column(db.String(100), default="")
    fecha_descarga = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "id": self.id_descarga,
            "usuario_id": self.id_usuario,
            "tour_id": self.id_tour,
            "dispositivo": self.dispositivo,
            "fecha_descarga": self.fecha_descarga.isoformat() if self.fecha_descarga else None
        }