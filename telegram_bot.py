import pandas as pd
import telebot
import time
import os

# ==========================================
#   CONFIGURACIÓN FINAL - ZENITH AUTO
# ==========================================
TOKEN = 'os.getenv('TELEGRAM_TOKEN')'
CHAT_ID = 'os.getenv('TELEGRAM_CHAT_ID')'
FILE_PATH = 'inventario.xlsx'

# Inicializamos el bot
bot = telebot.TeleBot(TOKEN)

def monitorear_stock():
    # Limpia la terminal para que el video empiece desde cero y limpio
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("==============================================")
    print("      🚀 ZENITH AUTO - SISTEMA ACTIVO        ")
    print("==============================================")
    print(f"📅 Archivo: {FILE_PATH}")
    print("🔍 ESTADO: MONITOREANDO EN TIEMPO REAL...")
    print("==============================================")
    print("💡 Instrucción para el video: Cambia un stock a menos de 5 y guarda el Excel.")

    # Guardamos los productos que ya avisamos para no repetir el mensaje mil veces
    ya_avisados = set()

    while True:
        try:
            # Leer el Excel (usamos engine='openpyxl' por seguridad)
            df = pd.read_excel(FILE_PATH)
            
            # Buscamos productos con stock menor a 5
            bajos = df[df['Stock'] < 5]
            
            for index, row in bajos.iterrows():
                producto = row['Producto']
                cantidad = row['Stock']
                
                # Solo avisar si no hemos avisado en esta sesión
                if producto not in ya_avisados:
                    mensaje = (
                        f"⚠️ *ALERTA DE INVENTARIO*\n\n"
                        f"📦 *Producto:* {producto}\n"
                        f"📉 *Stock Actual:* {cantidad}\n"
                        f"❗ *Estado:* REABASTECER URGENTE"
                    )
                    bot.send_message(CHAT_ID, mensaje, parse_mode="Markdown")
                    print(f"✅ Alerta enviada a Telegram: {producto} ({cantidad} unidades)")
                    ya_avisados.add(producto)
            
            # Revisa cada 3 segundos (Perfecto para que el video no sea lento)
            time.sleep(3)
            
        except Exception as e:
            print(f"❌ Error leyendo el archivo: {e}")
            time.sleep(2)

if __name__ == "__main__":
    monitorear_stock()