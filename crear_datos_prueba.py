import pandas as pd

# Creamos datos con errores a propósito:
# 1. Una fila duplicada (ID 1)
# 2. Una celda vacía (en Ventas de ID 3)
# 3. Formatos de fecha distintos
data = {
    'Nombre': [''Zenith_Admin'', ''Zenith_Admin'', 'Ana', 'Luis', 'Maria'],
    'Fecha': ['2026-03-01', '2026-03-01', '02/03/2026', '2026-03-03', '04-Mar-2026'],
    'Venta': [1500, 1500, None, 300, 450],
    'Producto': ['Laptop', 'Laptop', 'Mouse', 'Monitor', 'Teclado']
}

df = pd.DataFrame(data)

# Guardamos el archivo con el nombre exacto que pide la instrucción
nombre_archivo = "datos_sucios.xlsx"
df.to_excel(nombre_archivo, index=False)

print(f"✅ ¡Éxito! Se ha creado el archivo: {nombre_archivo}")
print("Ahora puedes correr tu script de limpieza sobre este archivo.")