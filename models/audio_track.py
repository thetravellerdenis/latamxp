from app.extensions import db

class AudioTrack(db.Model):
    __tablename__ = 'audio_track'
    id_audio = db.Column(db.Integer, primary_key=True)
    id_tour = db.Column(db.Integer, db.ForeignKey('tour.id_tour'), nullable=False)
    orden = db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(150), nullable=False)
    duracion_segundos = db.Column(db.Integer, nullable=False)
    archivo_url = db.Column(db.String(255))
    transcripcion = db.Column(db.Text, default="")

    def get_duracion_formateada(self) -> str:
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return f"{minutos:02d}:{segundos:02d}"

    def to_dict(self) -> dict:
        return {
            "id": self.id_audio,
            "tour_id": self.id_tour,
            "orden": self.orden,
            "titulo": self.titulo,
            "duracion_segundos": self.duracion_segundos,
            "duracion": self.get_duracion_formateada(),
            "archivo_url": self.archivo_url,
            "transcripcion": self.transcripcion
        }

    def __repr__(self) -> str:
        return f"<AudioTrack {self.id_audio}: {self.titulo}>"