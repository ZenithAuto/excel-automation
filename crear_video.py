import pandas as pd
import random
from datetime import datetime, timedelta

# Script para crear un archivo de Excel con errores para la demostración del video
def crear_excel_sucio():
    print("🛠️ Generando base de datos con errores para el video...")
    
    nombres = ["juan ", "MARIA GARCIA", "carlos Lopez", "ana martinez", "pedro GOMEZ", "Lucia Fernandez"]
    servicios = ["Python Script", "Excel Automation", "Data Cleaning", "Web Scraping", "API Integration"]
    paises = ["mexico", "USA", "spain", "COLOMBIA", "argentina", "CHILE"]
    
    data = []
    
    # Generamos 250 filas de datos "sucios"
    for i in range(250):
        nombre = random.choice(nombres)
        servicio = random.choice(servicios)
        # Error: Precios con formatos inconsistentes y algunos vacíos (None)
        precio = random.choice([f"${random.randint(50, 500)}", random.randint(50, 500), None])
        # Error: Fechas en diferentes formatos o mal escritas
        fecha = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime(random.choice(["%Y-%m-%d", "%d/%m/%Y", "InvalidDate"]))
        pais = random.choice(paises)
        # Error: Correos electrónicos mal formados
        email = f"{nombre.replace(' ', '.').lower()}@example" if i % 10 == 0 else f"{nombre.replace(' ', '.').lower()}@mail.com"
        
        data.append([nombre, servicio, precio, fecha, pais, email])

    # Añadir 20 duplicados exactos para demostrar la limpieza
    for _ in range(20):
        data.append(data[0])

    df = pd.DataFrame(data, columns=["Cliente", "Servicio", "Precio", "Fecha_Venta", "Pais", "Email"])
    
    # Guardar archivo
    nombre_archivo = "DATOS_CRUDOS_ZENITH_VIDEO.xlsx"
    df.to_excel(nombre_archivo, index=False)
    print(f"✅ Archivo '{nombre_archivo}' creado con 270 filas (listo para limpiar).")

if __name__ == "__main__":
    crear_excel_sucio()