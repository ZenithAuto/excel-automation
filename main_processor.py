import pandas as pd

# Datos exactos para que el script de automatización funcione
datos = {
    'Fecha': ['2026-03-01', '2026-03-10', '2026-03-15', '2026-03-20', '2026-03-25'],
    'Venta': [1500, 500, 300, 1500, 80]
}

df = pd.DataFrame(datos)

# Esto crea el archivo Ventas.xlsx automáticamente en tu carpeta
df.to_excel("Ventas.xlsx", index=False)

print("✅ ¡Listo! El archivo 'Ventas.xlsx' se ha creado en tu carpeta.")