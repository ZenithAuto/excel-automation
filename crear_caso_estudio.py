from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

# Título
pdf.cell(0, 15, "CASO DE ESTUDIO: Automatizacion de Inventario", 0, 1, 'C')
pdf.ln(5)

# Introducción
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "El Problema:", 0, 1)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8, "Muchos negocios pierden dinero por falta de stock o pasan horas revisando tablas de Excel manualmente para detectar productos agotados.")
pdf.ln(5)

# Solución
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "La Solucion ZenithAuto:", 0, 1)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8, "Implementamos un Bot de Telegram conectado directamente a su archivo de inventario. El sistema monitorea cada cambio en tiempo real y envia una alerta instantanea cuando el stock baja de un limite critico.")
pdf.ln(5)

# Resultados
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "Resultados Obtenidos:", 0, 1)
pdf.set_font("Arial", '', 12)
puntos = [
    "1. Reduccion del 100% en el tiempo de monitoreo manual.",
    "2. Notificaciones instantaneas 24/7.",
    "3. Prevencion de perdida de ventas por falta de producto.",
    "4. Interfaz amigable directamente en su celular."
]
for punto in puntos:
    pdf.cell(0, 8, punto, 0, 1)

pdf.output('Caso_Estudio_Bot_Inventario.pdf')
print("✅ Archivo 'Caso_Estudio_Bot_Inventario.pdf' creado con exito.")