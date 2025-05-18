# home_layout.py
from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H2("¡Bienvenido al Dashboard Deportivo!", className="text-center text-primary my-4")
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P(
                    "Selecciona una sección del menú para comenzar a explorar los datos de rendimiento y del área no competitiva.",
                    className="text-center"
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                dbc.Button("Cerrar sesión", id="logout_button", color="danger", className="mt-4"),
                width={"size": 2, "offset": 5},
                className="text-center"
            )
        ),
        html.Div(id="logout_output")
    ],
    fluid=True,
    className="mt-5"
)
