import pandas as pd
import os

def ejecutar_automatizacion():
    try:
        # 1. Pedir el nombre del archivo
        archivo = input("📁 Introduce el nombre del archivo Excel (ejemplo: datos.xlsx): ").strip()

        # 2. Verificar si el archivo existe (esto es PRO)
        if not os.path.exists(archivo):
            print(f"❌ Error: El archivo '{archivo}' no se encuentra en esta carpeta.")
            return

        print("⏳ Procesando datos...")
        
        # 3. Leer el Excel
        df = pd.read_excel(archivo)

        # 4. LIMPIEZA (Instrucción del texto: dropna)
        # Esto borra cualquier fila que esté totalmente vacía
        df_limpio = df.dropna(how='all')
        
        # 5. PROCESAMIENTO
        # Sumamos solo las columnas que tienen números
        resumen = df_limpio.select_dtypes(include='number').sum().reset_index()
        resumen.columns = ['Columna', 'Total_Suma']

        # 6. GUARDAR RESULTADO
        nombre_salida = "Reporte_Final_Pro.xlsx"
        resumen.to_excel(nombre_salida, index=False)
        
        print("-" * 30)
        print(f"✅ ¡LISTO! Se procesaron {len(df_limpio)} filas.")
        print(f"📦 Resultado guardado en: {nombre_salida}")
        print("-" * 30)

    except Exception as e:
        # Este es el bloque que evita que el programa se cierre feo
        print(f"⚠️ OCURRIÓ UN ERROR INESPERADO: {e}")

if __name__ == "__main__":
    ejecutar_automatizacion()