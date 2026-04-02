import pandas as pd
import os
import time

# ZENITHAUTO - SISTEMA DE PROCESAMIENTO AVANZADO
# Este es el código que debes mostrar corriendo en tu grabación de pantalla.

def ejecutar_limpieza_profunda():
    archivo_entrada = "DATOS_CRUDOS_ZENITH_VIDEO.xlsx"
    archivo_salida = "REPORTE_FINAL_ZENITH_LIMPIO.xlsx"
    
    print("====================================================")
    print("🚀 ZENITHAUTO ENGINE v2.5 - INICIANDO PROCESAMIENTO")
    print("====================================================")
    time.sleep(1)

    if not os.path.exists(archivo_entrada):
        print(f"❌ Error: No se encuentra el archivo {archivo_entrada}")
        return

    # 1. Cargar Datos
    print("📥 Cargando base de datos compleja...")
    df = pd.read_excel(archivo_entrada)
    time.sleep(1)

    # 2. Limpieza de Nombres (Normalización)
    print("🧹 Normalizando nombres de clientes (Title Case)...")
    df['Cliente'] = df['Cliente'].str.title()
    
    # 3. Limpieza de Precios (Convertir a número puro)
    print("💰 Extrayendo y corrigiendo valores monetarios...")
    df['Precio'] = df['Precio'].replace(r'[\$,]', '', regex=True).astype(float)
    df['Precio'] = df['Precio'].fillna(df['Precio'].mean()) # Rellenar vacíos con el promedio

    # 4. Corrección de Fechas
    print("📅 Corrigiendo formatos de fecha inconsistentes...")
    df['Fecha_Venta'] = pd.to_datetime(df['Fecha_Venta'], errors='coerce')
    df = df.dropna(subset=['Fecha_Venta']) # Eliminar fechas que eran texto basura

    # 5. Eliminación de Duplicados
    duplicados = df.duplicated().sum()
    print(f"♻️ Detectados {duplicados} registros duplicados. Eliminando...")
    df = df.drop_duplicates()

    # 6. Filtrado de Emails
    print("📧 Validando integridad de correos electrónicos...")
    df = df[df['Email'].str.contains('@')]

    # 7. Análisis Estadístico (Lo que el cliente quiere ver)
    print("📊 Generando análisis de ventas por país...")
    resumen = df.groupby('Pais')['Precio'].sum().reset_index()

    # 8. Guardado Final con Formato
    print(f"💾 Exportando resultado final a: {archivo_salida}")
    with pd.ExcelWriter(archivo_salida) as writer:
        df.to_excel(writer, sheet_name='Datos_Limpios', index=False)
        resumen.to_excel(writer, sheet_name='Resumen_Ventas', index=False)

    print("====================================================")
    print("✅ ¡PROCESO COMPLETADO CON EXITO!")
    print(f"✨ Total de filas procesadas: {len(df)}")
    print("====================================================")

if __name__ == "__main__":
    ejecutar_limpieza_profunda()