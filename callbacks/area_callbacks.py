from dash import Input, Output, callback, html, dcc
import pandas as pd
import plotly.express as px
from utils.data_loader import load_no_competitiva_data
import dash_bootstrap_components as dbc


def register_callbacks(app):
    # Callback para filtros (se mantiene igual)
    @app.callback(
        [Output("filters_container", "children"),
         Output("no_data_message", "children")],
        Input("area_selector", "value")
    )
    def update_filters(area_selected):
        if area_selected != "Medicina":
            return None, "Selecciona 'Medicina' para ver datos de lesiones"
        
        df = load_no_competitiva_data()
        
        if df.empty:
            error_msg = """
            No se pudieron cargar los datos. Verifica:
            1. Que el archivo no_competitiva_data.csv existe en la carpeta data/
            2. Que tiene las columnas correctas
            3. Que los datos tienen el formato adecuado
            """
            return None, error_msg

        equipos = [{"label": eq, "value": eq} for eq in sorted(df["Equipo"].unique())]
        estados = [{"label": st, "value": st} for st in sorted(df["Estado"].unique())]

        filters = html.Div([
            html.H4("Filtros de Lesiones", style={"marginTop": "20px"}),
            dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        id="team_dropdown",
                        options=equipos,
                        multi=True,
                        placeholder="Filtrar por equipo(s)",
                        className="mb-3"
                    ),
                    md=6
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="status_dropdown",
                        options=estados,
                        multi=True,
                        placeholder="Filtrar por estado",
                        className="mb-3"
                    ),
                    md=6
                )
            ])
        ])
        
        return filters, ""

    # Callback para gráficos (versión mejorada)
    @app.callback(
        Output("area_chart", "figure"),
        Output("secondary_chart", "figure"),
        [Input("team_dropdown", "value"),
         Input("status_dropdown", "value")]
    )
    def update_charts(selected_teams, selected_statuses):
        df = load_no_competitiva_data()
        
        if df.empty:
            empty_fig = px.bar(title="Datos no disponibles").update_layout(
                plot_bgcolor="white",
                paper_bgcolor="white"
            )
            return empty_fig, empty_fig
        
        # Aplicar filtros
        if selected_teams:
            df = df[df["Equipo"].isin(selected_teams)]
        if selected_statuses:
            df = df[df["Estado"].isin(selected_statuses)]
        
        if df.empty:
            empty_fig = px.bar(title="No hay datos con los filtros seleccionados")
            return empty_fig, empty_fig
        
        # --- GRÁFICO 1: Distribución de tipos de lesión ---
        lesion_counts = df["Lesión"].value_counts().reset_index()
        fig1 = px.bar(
            lesion_counts,
            x="Lesión",
            y="count",
            title="Distribución de Tipos de Lesión",
            labels={"count": "Número de casos", "Lesión": "Tipo de Lesión"},
            color="Lesión",
            hover_data={"Lesión": True, "count": True},
            text="count"
        )
        
        fig1.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            xaxis_title="Tipo de Lesión",
            yaxis_title="Número de Casos",
            hovermode="x unified"
        )
        fig1.update_traces(textposition='outside')
        
        # --- GRÁFICO 2: Lesiones por jugador y equipo ---
        # Agrupamos por jugador y equipo
        player_lesions = df.groupby(["Jugador", "Equipo", "Lesión"]).size().reset_index(name="count")
        
        fig2 = px.sunburst(
            player_lesions,
            path=['Equipo', 'Jugador', 'Lesión'],
            values='count',
            title='Distribución de Lesiones por Equipo y Jugador',
            color='Equipo',
            hover_data=['count'],
            height=600
        )
        
        fig2.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white",
            margin=dict(t=40, l=0, r=0, b=0)
        )
        
        return fig1, fig2
