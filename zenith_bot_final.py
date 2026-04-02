import pandas as pd
import telebot
import time
import os

# ==========================================
#   CONFIGURACIÓN - ZENITH AUTO PRO
# ==========================================
TOKEN = 'os.getenv('TELEGRAM_TOKEN')'
CHAT_ID = 'os.getenv('TELEGRAM_CHAT_ID')'
FILE_PATH = 'inventario.xlsx'

bot = telebot.TeleBot(TOKEN)

def monitorear_stock():
    # Limpia la pantalla al iniciar para que se vea profesional
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("==============================================")
    print("      🚀 ZENITH AUTO - SISTEMA INICIADO       ")
    print("==============================================")
    print(f"📡 Monitoreando: {FILE_PATH}")
    print("🟢 Estado: Protegido contra errores (Try-Except)")
    print("==============================================\n")

    ya_avisados = set()

    while True:
        # --- AQUÍ EMPIEZA EL BLINDAJE (PASO 1) ---
        try:
            # 1. Verificamos si el archivo existe antes de intentar leerlo
            if not os.path.exists(FILE_PATH):
                print(f"⚠️  AVISO: No se encuentra '{FILE_PATH}'. El bot esperará a que lo pongas...")
                time.sleep(10) # Espera 10 segundos y vuelve a intentar
                continue

            # 2. Intentamos leer el Excel
            df = pd.read_excel(FILE_PATH)
            
            # --- LÓGICA DE STOCK ---
            # Buscamos productos con stock menor a 5
            bajos = df[df['Stock'] < 5]
            
            for index, row in bajos.iterrows():
                producto = row['Producto']
                cantidad = row['Stock']
                
                if producto not in ya_avisados:
                    mensaje = (
                        f"⚠️ *ALERTA DE STOCK BAJO*\n\n"
                        f"📦 *Producto:* {producto}\n"
                        f"📉 *Cantidad actual:* {cantidad}\n"
                        f"✅ _Sistema Automático Zenith Auto_"
                    )
                    bot.send_message(CHAT_ID, mensaje, parse_mode="Markdown")
                    print(f"🔔 Notificación enviada: {producto} ({cantidad} unidades)")
                    ya_avisados.add(producto)
            
            # Revisar cada 5 segundos
            time.sleep(5)

        # --- AQUÍ SE ACTIVAN LOS ESCUDOS SI ALGO FALLA ---
        except PermissionError:
            # Este error sale si el Excel está abierto por el usuario
            print("❌ ERROR: El archivo está abierto. Ciérralo para que el bot pueda leerlo.")
            time.sleep(5)
            
        except Exception as e:
            # Este atrapa cualquier otro error raro (columnas mal escritas, etc.)
            print(f"❓ Error inesperado: {e}")
            print("Reintentando en 10 segundos...")
            time.sleep(10)

if __name__ == "__main__":
    monitorear_stock()