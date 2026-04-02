from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 20)
        self.set_text_color(0, 80, 158)
        self.cell(0, 10, 'ZENITH AUTO - SOLUTIONS', 0, 1, 'C')
        self.set_font('Arial', 'I', 12)
        self.set_text_color(100)
        self.cell(0, 10, 'Innovacion y Automatizacion de Procesos', 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Sección de Quiénes Somos
pdf.chapter_title('1. Quienes Somos')
pdf.chapter_body('En ZenithAuto nos especializamos en transformar tareas repetitivas en procesos automaticos. Ayudamos a empresas y emprendedores a ahorrar tiempo mediante el uso de Python y herramientas de ultima generacion.')

# Sección de Servicios
pdf.chapter_title('2. Nuestros Servicios Principales')
servicios = (
    "- Desarrollo de Bots de Telegram para notificaciones.\n"
    "- Automatizacion de reportes en Excel y Google Sheets.\n"
    "- Web Scraping y extraccion de datos.\n"
    "- Scripts personalizados para limpieza de archivos PDF y CSV."
)
pdf.chapter_body(servicios)

# Sección de Por qué elegirnos
pdf.chapter_title('3. Por que elegir ZenithAuto?')
pdf.chapter_body('Nuestras soluciones son rapidas, seguras y diseñadas a la medida de cada cliente. Optimizamos su flujo de trabajo para que usted se concentre en lo que realmente importa.')

pdf.output('Portafolio_ZenithAuto.pdf')
print("✅ Archivo 'Portafolio_ZenithAuto.pdf' creado con exito.")