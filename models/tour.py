from typing import List, Optional, Dict, Any


class Tour:
    """
    Representa un audio-tur en el sistema LatamXP.
    """

    def __init__(
        self,
        id_tour: int,
        titulo: str,
        descripcion: str,
        precio: float,
        duracion_minutos: int,
        ruta_geojson: Optional[Dict[str, Any]] = None,
        portada_url: Optional[str] = None,
        activo: bool = True
    ):
        self.id_tour = id_tour
        self.titulo = titulo
        self.descripcion = descripcion
        self.precio = precio
        self.duracion_minutos = duracion_minutos
        self.ruta_geojson = ruta_geojson or {}
        self.portada_url = portada_url
        self.activo = activo
        self._audios: List['AudioTrack'] = []
        self._puntos: List['PuntoInteres'] = []
        self._valoraciones: List['Valoracion'] = []

    def agregar_audio(self, audio: 'AudioTrack') -> None:
        self._audios.append(audio)

    def agregar_punto(self, punto: 'PuntoInteres') -> None:
        self._puntos.append(punto)

    def agregar_valoracion(self, valoracion: 'Valoracion') -> None:
        self._valoraciones.append(valoracion)

    def get_audios(self) -> List['AudioTrack']:
        return sorted(self._audios, key=lambda a: a.orden)

    def get_puntos(self) -> List['PuntoInteres']:
        return sorted(self._puntos, key=lambda p: p.orden)

    def get_valoraciones(self) -> List['Valoracion']:
        return self._valoraciones.copy()

    def get_duracion_total(self) -> int:
        return sum(a.duracion_segundos for a in self._audios)

    def get_calificacion_promedio(self) -> float:
        if not self._valoraciones:
            return 0.0
        return round(sum(v.puntuacion for v in self._valoraciones) / len(self._valoraciones), 2)

    def to_dict(self) -> dict:
        return {
            "id": self.id_tour,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "duracion_minutos": self.duracion_minutos,
            "portada_url": self.portada_url,
            "activo": self.activo,
            "calificacion_promedio": self.get_calificacion_promedio(),
            "total_valoraciones": len(self._valoraciones)
        }

    def __repr__(self) -> str:
        return f"<Tour {self.id_tour}: {self.titulo}>"
