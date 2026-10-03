from app.extensions import db


class Tour(db.Model):
    __tablename__ = "tour"
    id_tour = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    duracion_minutos = db.Column(db.Integer, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    portada_url = db.Column(db.String(255))
    activo = db.Column(db.Boolean, default=True)
    map_coords = db.Column(db.String(100), default="")

    country = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    city_description = db.Column(db.Text, default="")
    flag_url = db.Column(db.String(255), default="")

    distance_km = db.Column(db.Float, default=0.0)
    neighborhoods = db.Column(db.String(255), default="")
    itinerary = db.Column(db.JSON, default=list)
    banners = db.Column(db.JSON, default=list)
    map_coords = db.Column(db.String(100), default="")

    audios = db.relationship(
        "AudioTrack", backref="tour", lazy=True, cascade="all, delete-orphan"
    )
    puntos = db.relationship(
        "PuntoInteres", backref="tour", lazy=True, cascade="all, delete-orphan"
    )
    pedidos = db.relationship("Pedido", backref="tour", lazy=True)
    valoraciones = db.relationship("Valoracion", backref="tour", lazy=True)

    @property
    def precio_float(self):
        return float(self.precio)

    def get_avg_rating(self) -> float:
        if not self.valoraciones:
            return 0.0
        return sum(v.puntuacion for v in self.valoraciones) / len(self.valoraciones)
