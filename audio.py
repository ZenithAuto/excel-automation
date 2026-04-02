from pydub import AudioSegment
import os

def procesar_audio_pro(archivo_voz, archivo_musica, salida="final_editado.mp3"):
    # 1. Cargar archivos
    print("Cargando audios...")
    voz = AudioSegment.from_file(archivo_voz)
    musica = AudioSegment.from_file(archivo_musica)

    # 2. Ajustar música a la duración de la voz
    if len(musica) < len(voz):
        musica = musica * (len(voz) // len(musica) + 1)
    musica = musica[:len(voz)]

    # 3. Configurar Auto-Ducking (IA básica de volumen)
    # Detecta si hay sonido (voz) y baja la música
    print("Aplicando efectos automáticos...")
    umbral_voz = -35  # Sensibilidad
    musica_fondo = AudioSegment.empty()
    chunk_size = 100  # Analizar cada 100ms

    for i in range(0, len(voz), chunk_size):
        segmento_voz = voz[i:i+chunk_size]
        segmento_musica = musica[i:i+chunk_size]

        if segmento_voz.dBFS > umbral_voz:
            # Hay voz: bajar música -20dB
            musica_fondo += segmento_musica - 20
        else:
            # Silencio: música normal -10dB (para que no aturda)
            musica_fondo += segmento_musica - 10

    # 4. Mezclar y Exportar
    print("Mezclando todo...")
    resultado = musica_fondo.overlay(voz)
    resultado.export(salida, format="mp3")
    print(f"¡Listo! Archivo guardado como: {salida}")

# --- CONFIGURACIÓN ---
# Solo asegúrate de que los nombres de tus archivos sean estos:
procesar_audio_pro("mi_voz.mp3", "musica.mp3")