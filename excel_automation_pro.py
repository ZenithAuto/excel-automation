import pandas as pd

# 1. Configuración de archivos
archivo_entrada = "Ventas.xlsx"
archivo_salida = "reporte_mensual.xlsx"

try:
    # 2. Leer el archivo que ya tienes creado
    df = pd.read_excel(archivo_entrada)

    # 3. Procesamiento: Suma de ventas por mes
    # Convertimos la columna Fecha a formato de tiempo real
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df['Mes'] = df['Fecha'].dt.month
    
    # Agrupamos y sumamos
    resumen = df.groupby('Mes')['Venta'].sum().reset_index()

    # 4. Guardar el resultado profesional
    resumen.to_excel(archivo_salida, index=False)

    print(f"✅ ¡Éxito! Se ha generado el archivo: {archivo_salida}")
    print("Revisa tu carpeta para ver el resultado.")

except FileNotFoundError:
    print(f"❌ Error: No encontré el archivo '{archivo_entrada}'. Asegúrate de que esté en la misma carpeta que este código.")
except Exception as e:
    print(f"❌ Ocurrió un error inesperado: {e}")