from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

def generar_portafolio():
    archivo = "PORTAFOLIO_ZENITH.pdf"
    doc = SimpleDocTemplate(archivo, pagesize=letter, 
                            rightMargin=50, leftMargin=50, 
                            topMargin=50, bottomMargin=50)
    
    # Colores de marca: Navy Blue y Cyan
    color_navy = colors.Color(0.05, 0.1, 0.25)
    color_cyan = colors.Color(0, 0.8, 0.8)
    
    styles = getSampleStyleSheet()
    
    # Estilos Personalizados
    style_titulo = ParagraphStyle(
        'Titulo',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=color_cyan,
        alignment=1, # Centro
        spaceAfter=20,
        fontName='Helvetica-Bold'
    )
    
    style_subtitulo = ParagraphStyle(
        'Subtitulo',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=color_navy,
        borderPadding=5,
        spaceBefore=15,
        spaceAfter=10,
        fontName='Helvetica-Bold'
    )

    style_cuerpo = ParagraphStyle(
        'Cuerpo',
        parent=styles['Normal'],
        fontSize=11,
        leading=14, # Interlineado
        alignment=4, # Justificado
        fontName='Helvetica'
    )

    style_garantia = ParagraphStyle(
        'Garantia',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.whitesmoke,
        backColor=color_navy,
        borderPadding=10,
        alignment=1
    )

    elementos = []

    # Encabezado
    elementos.append(Paragraph("ZenithAuto", style_titulo))
    elementos.append(Paragraph("Soluciones de Automatización y Software de Alto Rendimiento", style_cuerpo))
    elementos.append(Spacer(1, 0.5 * inch))

    # Sección 1: Limpieza de Big Data
    elementos.append(Paragraph("1. Limpieza de Big Data", style_subtitulo))
    elementos.append(Paragraph(
        "Transformamos datos crudos y desordenados en activos estratégicos. Mediante scripts "
        "optimizados en Python, eliminamos duplicados, normalizamos formatos y preparamos "
        "grandes volúmenes de información para análisis avanzado o integración en bases de datos.",
        style_cuerpo
    ))

    # Sección 2: Reportes Automáticos
    elementos.append(Paragraph("2. Reportes Automáticos", style_subtitulo))
    elementos.append(Paragraph(
        "Diga adiós a las tareas repetitivas. Creamos sistemas que generan reportes en PDF, "
        "Excel o dashboards interactivos de forma programada. Visualización clara de métricas "
        "clave que ahorra horas de trabajo manual cada semana.",
        style_cuerpo
    ))

    # Sección 3: Web Scraping
    elementos.append(Paragraph("3. Web Scraping Profesional", style_subtitulo))
    elementos.append(Paragraph(
        "Extracción ética y eficiente de datos desde portales web, e-commerce o redes sociales. "
        "Nuestras soluciones manejan dinámicas complejas para entregar la información "
        "que su negocio necesita para mantenerse competitivo.",
        style_cuerpo
    ))

    elementos.append(Spacer(1, 1 * inch))

    # Sección de Garantía
    elementos.append(Paragraph("GARANTÍA ZENITHAUTO", style_garantia))
    elementos.append(Spacer(1, 0.1 * inch))
    elementos.append(Paragraph(
        "Compromiso de calidad: Todos nuestros proyectos incluyen soporte post-entrega. "
        "Por políticas de seguridad y transparencia, el soporte técnico y la comunicación "
        "son exclusivos a través del chat de Fiverr.",
        style_cuerpo
    ))

    # Generar el archivo
    try:
        doc.build(elementos)
        print(f"Éxito: El archivo '{archivo}' ha sido generado correctamente.")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")

if __name__ == "__main__":
    generar_portafolio()