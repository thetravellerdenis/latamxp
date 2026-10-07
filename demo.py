from datetime import datetime
from models.usuario import Usuario
from models.tour import Tour
from models.audio_track import AudioTrack
from models.punto_interes import PuntoInteres
from models.pedido import Pedido
from models.valoracion import Valoracion
from models.descarga_offline import DescargaOffline
from services.servicio_pagos import ServicioPagos
from services.servicio_gps import ServicioGPS
from services.servicio_audio import ServicioAudio


def main():
    print("=== LatamXP - Demo de Funcionamiento ===\n")

    usuario = Usuario(1, "Juan Pérez", "juan@email.com", "hashed_password")
    print(f"✓ Usuario creado: {usuario}")

    tour = Tour(1, "Historia del Centro Porteño", "Recorrido histórico...", 7.99, 75)
    print(f"✓ Tour creado: {tour}")

    audio1 = AudioTrack(101, 1, 1, "Introducción", 120, "https://cdn/tour1/intro.mp3")
    audio2 = AudioTrack(102, 1, 2, "Plaza de Mayo", 180, "https://cdn/tour1/plaza.mp3")
    tour.agregar_audio(audio1)
    tour.agregar_audio(audio2)
    print(f"✓ Audios agregados: {len(tour.get_audios())} tracks")

    punto = PuntoInteres(201, 1, -34.6082, -58.3712, "Plaza de Mayo", "Corazón de la historia argentina", 1)
    tour.agregar_punto(punto)
    print(f"✓ Punto de interés agregado: {punto.nombre}")

    pedido = Pedido(5001, 1, 1, 7.99, "mercadopago")
    pedido.marcar_pagado()
    usuario.agregar_pedido(pedido)
    print(f"✓ Pedido creado: {pedido}")

    valoracion = Valoracion(3001, 1, 1, 5, "Excelente recorrido!")
    tour.agregar_valoracion(valoracion)
    usuario.agregar_valoracion(valoracion)
    print(f"✓ Valoración agregada: {valoracion.puntuacion}/5")

    pagos = ServicioPagos(api_key="test_key")
    result = pagos.procesar_pago(pedido, "tok_test_123")
    print(f"✓ Pago procesado: {result['status']}")

    gps = ServicioGPS()
    gps.actualizar_posicion(-34.6080, -58.3710)
    cercanos = gps.get_puntos_cercanos(tour, 50)
    print(f"✓ Puntos cercanos: {len(cercanos)}")

    audio_service = ServicioAudio()
    url = audio_service.get_audio_file(audio1, 1, 5001)
    print(f"✓ URL del audio: {url[:50]}...")

    print("\n=== Resumen del sistema ===")
    print(f"Usuario: {usuario.nombre}")
    print(f"Tour: {tour.titulo}")
    print(f"Calificación promedio: {tour.get_calificacion_promedio()}")
    print(f"Total de pedidos: {len(usuario.get_pedidos())}")
    print(f"Duración total del tour: {tour.get_duracion_total()} seg")


if __name__ == "__main__":
    main()
