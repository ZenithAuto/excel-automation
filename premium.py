import pandas as pd

# 1. Datos de ejemplo para que veas cómo funciona
data = {
    'Producto': ['Laptop', 'Mouse', 'Monitor', 'Laptop', 'Teclado', 'Monitor'],
    'Ventas': [1500, 50, 300, 1500, 80, 300],
    'Fecha': ['2026-03-01', '2026-03-02', '2026-03-02', '2026-03-03', '2026-03-04', '2026-03-05']
}

df = pd.DataFrame(data)

# 2. La función que automatiza la suma de ventas
reporte = df.groupby('Producto')['Ventas'].sum().reset_index()

# 3. Crear el archivo final que le darías al cliente
reporte.to_excel('Reporte_ZenithAuto.xlsx', index=False)

print("✅ ¡Reporte generado con éxito! Revisa tu carpeta.")