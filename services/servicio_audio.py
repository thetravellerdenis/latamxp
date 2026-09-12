from models.audio_track import AudioTrack


class ServicioAudio:
    """
    Servicio que maneja la generación de enlaces de audio y descargas.
    """

    def __init__(self, storage_provider: str = "s3"):
        self.storage_provider = storage_provider

    def get_audio_file(self, track: AudioTrack, user_id: int, order_id: int) -> str:
        print(f"Usuario {user_id} solicita audio {track.id_audio} del pedido {order_id}")
        return track.archivo_url

    def generar_enlace_descarga(self, track: AudioTrack, expiracion_segundos: int = 3600) -> str:
        return f"https://storage.latamxp.com/{track.archivo_url}?expires=...{expiracion_segundos}"

    def get_duracion_formateada(self, segundos: int) -> str:
        minutos = segundos // 60
        segundos_restantes = segundos % 60
        return f"{minutos:02d}:{segundos_restantes:02d}"
