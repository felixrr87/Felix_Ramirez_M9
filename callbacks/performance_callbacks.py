from dash import Input, Output, State, html, no_update, callback_context
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from dash.exceptions import PreventUpdate
from utils.data_loader import load_performance_data
from utils.pdf_exporter import export_performance_pdf


def register_callbacks(app):
    # Callback para player_dropdown (modificado)
    @app.callback(
        Output("player_dropdown", "options"),
        [Input("url", "pathname"),
         Input("team_dropdown", "value")],  # Añadido como dependencia
        prevent_initial_call=False  # Permitir carga inicial
    )
    def update_player_dropdown(pathname, selected_team):
        if pathname != "/performance":
            return no_update
            
        df = load_performance_data()
        if df.empty:
            return []
            
        df.columns = df.columns.str.strip().str.lower()
        df["player"] = df["player"].str.strip()
        
        # Filtrar por equipo si hay selección
        if selected_team:
            df = df[df["team"] == selected_team]
            
        return [{"label": p, "value": p} for p in sorted(df["player"].unique())]

    # Callback para team_dropdown (modificado)
    @app.callback(
        Output("team_dropdown", "options"),
        Input("url", "pathname"),
        prevent_initial_call=False  # Permitir carga inicial
    )
    def update_team_dropdown(pathname):
        if pathname != "/performance":
            return no_update
            
        df = load_performance_data()
        if df.empty:
            return []
            
        df.columns = df.columns.str.strip().str.lower()
        return [{"label": t, "value": t} for t in sorted(df["team"].unique())]

    # Resto de callbacks (se mantienen igual)
    @app.callback(
        Output("graph_comparison", "figure"),
        Output("graph_timeline", "figure"),
        Output("performance_summary", "children"),
        Input("player_dropdown", "value"),
        Input("metric_dropdown", "value"),
        Input("date_range", "start_date"),
        Input("date_range", "end_date"),
        Input("team_dropdown", "value"),
        Input("url", "pathname")
    )
    def update_performance_graph(players, metric, start_date, end_date, team, pathname):
        if pathname != "/performance":
            raise PreventUpdate
            
        df = load_performance_data()
        
        df.columns = df.columns.str.strip().str.lower()
        df['date'] = pd.to_datetime(df['date'])
        
        if players:
            df = df[df["player"].isin(players)]
        if team:
            df = df[df["team"] == team]
        if start_date and end_date:
            df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

        if df.empty or metric not in df.columns:
            return {}, {}, "No hay datos para los filtros seleccionados."

        fig_comp = px.bar(
            df.groupby("player")[metric].sum().reset_index(),
            x="player", y=metric, color="player",
            title=f"Comparativa total por jugador ({metric})"
        )

        fig_time = px.line(
            df.sort_values("date"), x="date", y=metric, color="player",
            markers=True, title=f"Evolución de {metric} en el tiempo"
        )

        resumen = (
            f"Equipo seleccionado: {team if team else 'Todos'}\n"
            f"Jugadores: {', '.join(sorted(set(df['player'])))}\n"
            f"Total acumulado: {df[metric].sum():.1f} {metric}."
        )

        return fig_comp, fig_time, resumen

    @app.callback(
        Output("pdf_export_status", "children"),
        Input("export_pdf_btn", "n_clicks"),
        State("graph_comparison", "figure"),
        State("graph_timeline", "figure"),
        State("performance_summary", "children"),
        State("player_dropdown", "value"),
        State("url", "pathname"),
        prevent_initial_call=True
    )
    def export_pdf(n_clicks, fig1, fig2, resumen, jugadores, pathname):
        if pathname != "/performance" or not jugadores:
            return "⚠️ Selecciona al menos un jugador."

        try:
            fig1_obj = go.Figure(fig1)
            fig2_obj = go.Figure(fig2)

            output_path = os.path.join("assets", "informe_rendimiento.pdf")
            export_performance_pdf(fig1_obj, fig2_obj, resumen, jugadores, output_path=output_path)

            return html.A("✅ PDF generado. Haz clic para descargar.", 
                        href="/assets/informe_rendimiento.pdf", 
                        target="_blank")

        except Exception as e:
            return f"❌ Error al generar PDF: {e}"