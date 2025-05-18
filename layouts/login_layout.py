from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Layout para la página de login
def login_layout():
    return html.Div(
        children=[
            # Fondo de la página
            html.Div(
                className="login-background",
                children=[
                    html.Div(
                        className="login-form-container",
                        children=[
                            html.H2("Bienvenido al Dashboard Deportivo", className="login-header"),
                            
                            # Formulario de login
                            dbc.Input(id="username", placeholder="Usuario", type="text", className="login-input"),
                            dbc.Input(id="password", placeholder="Contraseña", type="password", className="login-input"),
                            
                            dbc.Button("Iniciar sesión", id="login_button", color="primary", className="login-btn"),
                            
                            # Mensaje de error si las credenciales no son correctas
                            html.Div(id="error_message", style={"color": "red", "display": "none"}),
                        ],
                    ),
                ],
            ),
        ]
    )
