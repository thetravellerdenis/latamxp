from datetime import datetime
from app.extensions import db

class Pedido(db.Model):
    __tablename__ = 'pedido'
    id_pedido = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_tour = db.Column(db.Integer, db.ForeignKey('tour.id_tour'), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    monto = db.Column(db.Numeric(10, 2), nullable=False)
    estado = db.Column(db.String(20), nullable=False, default='pending')
    metodo_pago = db.Column(db.String(50), nullable=False)

    def marcar_pagado(self) -> None:
        self.estado = 'paid'

    def marcar_fallido(self) -> None:
        self.estado = 'failed'

    def to_dict(self) -> dict:
        return {
            "id": self.id_pedido,
            "id_tour": self.id_tour,
            "monto": float(self.monto),
            "estado": self.estado,
            "fecha": self.fecha.isoformat() if self.fecha else None
        }