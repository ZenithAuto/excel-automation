# ZenithAuto - Generador de Manual de Usuario
contenido = """
===========================================================
     SOPORTE TÉCNICO - ZENITHAUTO AUTOMATION
===========================================================

¡Gracias por tu compra! Sigue estos pasos para ejecutar tu script:

1. INSTALACIÓN DE PYTHON:
   Si no tienes Python, descárgalo en python.org e instálalo.
   IMPORTANTE: Marca la casilla "Add Python to PATH" al instalar.

2. PREPARAR LAS LIBRERÍAS:
   Abre una terminal y escribe el siguiente comando:
   pip install pandas openpyxl

3. CARGAR TUS DATOS:
   Copia tu archivo de Excel en la misma carpeta donde está el script.
   Asegúrate de que se llame 'datos_sucios.xlsx' o cambia el nombre
   dentro del código.

4. EJECUTAR EL SCRIPT:
   En la terminal, escribe: python zenith_cleaner_pro.py
   
5. REVISAR RESULTADOS:
   El script generará automáticamente un nuevo archivo llamado 
   'reporte_final_limpio.xlsx' con los datos procesados.

-----------------------------------------------------------
⚠️ REGLA DE SEGURIDAD: 
Toda la comunicación y soporte se realiza por el chat de Fiverr.
===========================================================
"""

with open("INSTRUCCIONES_USUARIO.txt", "w", encoding="utf-8") as archivo:
    archivo.write(contenido)

print("✅ Archivo 'INSTRUCCIONES_USUARIO.txt' generado. ¡Listo para enviar al cliente!")