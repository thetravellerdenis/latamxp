class AudioTrack:
    """
    Representa un archivo de audio dentro de un tour.
    """

    def __init__(
        self,
        id_audio: int,
        id_tour: int,
        orden: int,
        titulo: str,
        duracion_segundos: int,
        archivo_url: str,
        transcripcion: str = ""
    ):
        self.id_audio = id_audio
        self.id_tour = id_tour
        self.orden = orden
        self.titulo = titulo
        self.duracion_segundos = duracion_segundos
        self.archivo_url = archivo_url
        self.transcripcion = transcripcion

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
