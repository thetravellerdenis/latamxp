from datetime import datetime, timedelta
from app.extensions import db


class Suscripcion(db.Model):
    __tablename__ = "suscripcion"
    id_suscripcion = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(
        db.Integer, db.ForeignKey("usuario.id_usuario"), nullable=False
    )
    fecha_inicio = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_fin = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.String(20), default="active")  # active, cancelled, expired
    monto = db.Column(db.Numeric(10, 2), default=25.00)

    usuario = db.relationship("Usuario", backref="suscripciones")

    @property
    def is_active(self):
        return self.estado == "active" and self.fecha_fin > datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.id_suscripcion,
            "estado": self.estado,
            "fecha_fin": self.fecha_fin.isoformat(),
        }
