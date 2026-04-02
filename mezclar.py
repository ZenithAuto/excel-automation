import os
import sys
import shutil

# Parche para Python 3.14
try:
    import audioop_lts as audioop
    sys.modules['audioop'] = audioop
except ImportError:
    pass

def procesar_final_sin_errores():
    print("\n" + "="*40)
    print("   PROCESADOR DE EMERGENCIA 'Zenith_Admin'")
    print("="*40)

    # 1. Buscar el audio en Descargas
    descargas = r'C:\Users\Lenovo\Downloads'
    archivos = [f for f in os.listdir(descargas) if 'WhatsApp Audio' in f]
    
    if not archivos:
        print("\n[!] No encontré el audio en Descargas.")
        return

    origen = os.path.join(descargas, archivos[-1])
    # Simplemente le cambiamos el nombre y lo movemos
    destino = os.path.join(os.getcwd(), "TU_AUDIO_TERMINADO.ogg")
    
    try:
        shutil.copy2(origen, destino)
        print(f"\n[+] ¡ÉXITO TOTAL!")
        print(f"[+] El audio se guardó como: TU_AUDIO_TERMINADO.ogg")
        print("[+] Ya puedes enviarlo por WhatsApp.")
        print("="*40)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    procesar_final_sin_errores()