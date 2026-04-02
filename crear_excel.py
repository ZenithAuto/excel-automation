import pandas as pd

# 1. Creamos los datos de ejemplo
datos = {
    'Producto': [
        'Laptop Gamer Pro', 
        'Mouse RGB Inalámbrico', 
        'Monitor 4K 144Hz', 
        'Teclado Mecánico', 
        'Audífonos HyperX'
    ],
    'Stock': [15, 3, 20, 2, 12] # Pusimos el Mouse y el Teclado con stock bajo (<5)
}

# 2. Convertimos los datos a un formato que Excel entienda (DataFrame)
df = pd.DataFrame(datos)

# 3. Guardamos el archivo
nombre_archivo = 'inventario.xlsx'
df.to_excel(nombre_archivo, index=False)

print(f"✅ ¡Listo! Se ha creado el archivo '{nombre_archivo}' con éxito.")
print("Ahora ya puedes correr tu Bot de Telegram.")