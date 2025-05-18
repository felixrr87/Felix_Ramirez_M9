import os
import tempfile
from fpdf import FPDF

def export_performance_pdf(fig1, fig2, resumen_texto, jugadores, output_path="performance_report.pdf"):
    """
    Exporta un PDF con dos gráficas (fig1, fig2) y un resumen de texto.
    Guarda el PDF en output_path.
    
    Parámetros:
    - fig1, fig2: objetos plotly.graph_objects.Figure
    - resumen_texto: str con texto del resumen (puede contener saltos de línea)
    - jugadores: lista de strings con nombres de jugadores
    - output_path: ruta de salida del PDF
    """

    # Crear carpeta destino si no existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Crear imágenes temporales para los gráficos
    temp_dir = tempfile.gettempdir()
    graph1_path = os.path.join(temp_dir, "temp_graph1.png")
    graph2_path = os.path.join(temp_dir, "temp_graph2.png")

    # Guardar imágenes con kaleido (asegúrate de tener kaleido instalado)
    fig1.write_image(graph1_path, format="png", width=1000, height=600, engine="kaleido")
    fig2.write_image(graph2_path, format="png", width=1000, height=600, engine="kaleido")

    # Crear PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Insertar logo si existe
    logo_path = os.path.join("assets", "sportalyze.png")
    if os.path.isfile(logo_path):
        pdf.image(logo_path, x=70, y=10, w=70)
        pdf.ln(45)  # Espacio debajo del logo
    else:
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "SPORTALYZE - Informe de Rendimiento", ln=True, align="C")
        pdf.ln(10)

    # Título del informe
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Informe de Rendimiento Deportivo", ln=True, align="C")
    pdf.ln(10)

    # Resumen
    pdf.set_font("Arial", size=12)
    for linea in resumen_texto.split("\n"):
        pdf.multi_cell(0, 10, linea)
    pdf.ln(10)

    # Insertar gráficos
    pdf.image(graph1_path, x=10, w=190)
    pdf.ln(65)
    pdf.image(graph2_path, x=10, w=190)
    pdf.ln(65)

    # Pie de página con jugadores analizados
    pdf.set_font("Arial", "I", 10)
    jugadores_str = ", ".join(jugadores)
    pdf.multi_cell(0, 10, f"Jugadores analizados: {jugadores_str}", align="C")

    # Guardar archivo PDF
    pdf.output(output_path)

   
