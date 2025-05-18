from dash import Input, Output, State, dcc
from flask_login import login_user, logout_user
from utils.auth import User

def register_callbacks(app):
    # Callback para el login
    @app.callback(
        Output("error_message", "children"),
        Output("error_message", "style"),
        Output("url", "pathname"),  # Para redirigir después de un login exitoso
        Input("login_button", "n_clicks"),
        State("username", "value"),
        State("password", "value"),
        prevent_initial_call=True
    )
    def verify_login(n_clicks, username, password):
        if username == "admin" and password == "admin":
            user = User(id="admin")
            login_user(user)
            return "", {"display": "none"}, "/home"  # Redirigir a /home
        else:
            return "Usuario o contraseña incorrectos", {"display": "block", "color": "red"}, "/"  # Mantener en la página de login

    # Callback para cerrar sesión
    @app.callback(
        Output("logout_output", "children"),
        Input("logout_button", "n_clicks"),
        prevent_initial_call=True
    )
    def logout(n_clicks):
        if n_clicks:
            logout_user()
            return dcc.Location(href="/", id="redirect-logout")  # Redirige a la página de login
