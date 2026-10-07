from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    idioma_preferido = db.Column(db.String(20), default='es')
    activo = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False) 

    # Связи
    pedidos = db.relationship('Pedido', backref='usuario', lazy=True)
    valoraciones = db.relationship('Valoracion', backref='usuario', lazy=True)
    descargas = db.relationship('DescargaOffline', backref='usuario', lazy=True)

    # <--- ДОБАВЛЕННЫЕ МЕТОДЫ --->
    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def agregar_pedido(self, pedido: 'Pedido') -> None:
        self.pedidos.append(pedido)

    def agregar_valoracion(self, valoracion: 'Valoracion') -> None:
        self.valoraciones.append(valoracion)

    def get_pedidos(self) -> list:
        return self.pedidos

    def get_pedidos_activos(self) -> list:
        return [p for p in self.pedidos if p.estado == "paid"]

    def get_valoraciones(self) -> list:
        return self.valoraciones

    def to_dict(self) -> dict:
        return {
            "id": self.id_usuario,
            "nombre": self.nombre,
            "email": self.email,
            "fecha_registro": self.fecha_registro.isoformat() if self.fecha_registro else None,
            "idioma_preferido": self.idioma_preferido,
            "activo": self.activo,
            "is_admin": self.is_admin
        }

    def __repr__(self) -> str:
        return f"<Usuario {self.id_usuario}: {self.nombre}>"