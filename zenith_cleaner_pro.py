import pandas as pd

def procesar_datos(archivo_entrada, archivo_salida):
    print(f"--- Iniciando proceso para: {archivo_entrada} ---")
    
    # 1. Leer el archivo
    df = pd.read_excel(archivo_entrada)
    
    # 2. LIMPIEZA: Eliminar filas que estén completamente vacías
    df = df.dropna(how='all')
    
    # 3. LIMPIEZA: Eliminar registros duplicados (como las Laptops repetidas)
    filas_antes = len(df)
    df = df.drop_duplicates()
    filas_despues = len(df)
    
    # 4. LIMPIEZA: Llenar celdas vacías en 'Nombre' con "Sin Nombre"
    df['Nombre'] = df['Nombre'].fillna("Desconocido")
    
    # 5. PROCESAMIENTO: Sumar ventas por producto
    reporte = df.groupby('Nombre')['Venta'].sum().reset_index()
    
    # 6. GUARDAR RESULTADO
    with pd.ExcelWriter(archivo_salida) as writer:
        df.to_excel(writer, sheet_name='Datos_Limpios', index=False)
        reporte.to_excel(writer, sheet_name='Resumen_Ventas', index=False)
    
    print(f"✅ Proceso terminado.")
    print(f"Total de duplicados eliminados: {filas_antes - filas_despues}")
    print(f"Reporte guardado como: {archivo_salida}")

if __name__ == "__main__":
    # Ejecutamos el script usando el archivo sucio que creamos
    procesar_datos("datos_sucios.xlsx", "reporte_final_limpio.xlsx")