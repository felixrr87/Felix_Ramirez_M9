from dash import html, dcc
import dash_bootstrap_components as dbc

# Definición del layout principal
layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            html.H2("Área No Competitiva", className="text-center my-4")
        )
    ),
    
    dbc.Row(
        dbc.Col(
            dcc.Dropdown(
                id="area_selector",
                options=[
                    {"label": "Medicina (Lesiones)", "value": "Medicina"},
                ],
                placeholder="Selecciona un área...",
                className="mb-4"
            ),
            width={"size": 6, "offset": 3}
        )
    ),
    
    dbc.Row(
        dbc.Col(
            html.Div(id="filters_container"),
            width=12
        )
    ),
    
    dbc.Row(
        dbc.Col(
            html.Div(id="no_data_message", className="text-center"),
            width=12
        )
    ),
    
    dbc.Row(
        dbc.Col(
            dcc.Graph(id="area_chart"),
            width=12
        )
    ),
    
    dbc.Row(
        dbc.Col(
            dcc.Graph(id="secondary_chart"),
            width=12
        )
    )
], fluid=True)
