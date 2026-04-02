import pandas as pd

# Creamos los datos con errores a propósito (celdas vacías y duplicados)
data = {
    'Nombre': ['Laptop', 'Mouse', 'Monitor', 'Laptop', 'Teclado', 'Mouse', None, 'Monitor', 'Laptop', 'Teclado'],
    'Fecha': ['2026-03-01', '2026-03-02', '2026-03-02', '2026-03-01', '2026-03-04', '2026-03-02', '2026-03-05', None, '2026-03-01', '2026-03-04'],
    'Venta': [1500, 50, 300, 1500, 80, 50, 100, 300, 1500, 80]
}

df = pd.DataFrame(data)

# Guardamos el archivo "sucio"
df.to_excel("datos_sucios.xlsx", index=False)

print("✅ Archivo 'datos_sucios.xlsx' creado con éxito (incluye duplicados y vacíos).")