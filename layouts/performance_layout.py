import pandas as pd
import plotly.express as px
from dash import html, dcc
from utils.data_loader import load_performance_data

# --- CARGA DE DATOS CON CONTROL DE ERRORES ---
try:
    df = load_performance_data()

    if df.empty:
        raise ValueError("No se pudieron cargar los datos de performance.")

    if 'date' not in df.columns:
        raise ValueError("No se encontró columna de fecha válida ('date').")

    min_date = df["date"].min().date()
    max_date = df["date"].max().date()

except Exception as e:
    print(f"[ERROR] performance_layout.py - {str(e)}")
    min_date = pd.to_datetime('2024-01-01').date()
    max_date = pd.to_datetime('2024-12-31').date()

# --- LAYOUT PRINCIPAL ---
layout = html.Div([
    html.Div([
        html.H2("Análisis de Rendimiento", className="title-style"),
        html.Img(src="/assets/logo.png", height="50px", style={"float": "right"})
    ], style={
        "display": "flex",
        "justifyContent": "space-between",
        "alignItems": "center",
        "marginBottom": "20px"
    }),

    html.Div([
        html.Div([
            html.Label("Selecciona jugador:", className="label-style"),
            dcc.Loading(
                id="loading-players",
                children=[
                    dcc.Dropdown(
                        id="player_dropdown",
                        options=[],
                        multi=True,
                        placeholder="Elige uno o varios jugadores",
                        className="dropdown-style",
                        persistence=True,
                        persistence_type='memory'
                    )
                ],
                type="circle"
            )
        ], className="filter-container"),

        html.Div([
            html.Label("Selecciona equipo:", className="label-style"),
            dcc.Loading(
                id="loading-teams",
                children=[
                    dcc.Dropdown(
                        id="team_dropdown",
                        options=[],
                        placeholder="Filtra por equipo",
                        className="dropdown-style",
                        persistence=True,
                        persistence_type='memory'
                    )
                ],
                type="circle"
            )
        ], className="filter-container"),

        html.Div([
            html.Label("Selecciona métrica:", className="label-style"),
            dcc.Dropdown(
                id="metric_dropdown",
                options=[
                    {"label": "Goles", "value": "goals"},
                    {"label": "Asistencias", "value": "assists"},
                    {"label": "Minutos jugados", "value": "minutes_played"},
                    {"label": "Distancia (km)", "value": "distance_km"},
                    {"label": "Velocidad (km/h)", "value": "speed_kph"}
                ],
                value="goals",  # Valor por defecto
                placeholder="Elige una métrica",
                className="dropdown-style"
            )
        ], className="filter-container"),

        html.Div([
            html.Label("Selecciona rango de fechas:", className="label-style"),
            dcc.DatePickerRange(
                id="date_range",
                start_date=min_date,
                end_date=max_date,
                min_date_allowed=min_date,
                max_date_allowed=max_date,
                display_format="YYYY-MM-DD",
                className="datepicker-style"
            )
        ], className="filter-container"),
    ], className="filters-grid"),

    html.Div([
        html.Button("📄 Exportar a PDF", id="export_pdf_btn", n_clicks=0, className="pdf-button"),
        dcc.Loading(
            id="pdf-loading",
            children=[html.Div(id="pdf_export_status", className="pdf-status")],
            type="circle"
        )
    ], className="pdf-container"),

    dcc.Graph(id="graph_comparison", className="graph-style"),
    dcc.Graph(id="graph_timeline", className="graph-style"),

    html.Div(id="performance_summary", className="summary-container"),

    html.Div(id="logout-output", style={"display": "none"})
], className="main-container")