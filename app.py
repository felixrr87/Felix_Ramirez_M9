import sys
import os
from utils.data_loader import load_no_competitiva_data, load_performance_data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
from flask import Flask, redirect
from flask_login import LoginManager, UserMixin, login_required, current_user

from components import navbar
from layouts.login_layout import login_layout
from layouts.home_layout import layout as home_layout
from layouts.area_layout import layout as area_layout
from layouts.performance_layout import layout as performance_layout

from callbacks.login_callbacks import register_callbacks as register_login_callbacks
from callbacks.performance_callbacks import register_callbacks as register_performance_callbacks
from callbacks.area_callbacks import register_callbacks as register_area_callbacks

print("\n=== DEBUG: Ruta base ===")
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Precargar datos al inicio
print("Precargando datos...")
try:
    load_performance_data()
    load_no_competitiva_data()
    print("Datos precargados correctamente")
except Exception as e:
    print(f"Error precargando datos: {str(e)}")

# Flask + Login manager
server = Flask(__name__)
server.secret_key = "supersecretkey"
login_manager = LoginManager()
login_manager.init_app(server)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Dash app
app = dash.Dash(__name__, server=server, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Dashboard Deportivo"

# Componente base
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content")
])

# Ruteo entre páginas
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/":
        return login_layout()
    elif pathname == "/home":
        return html.Div([navbar.navbar, home_layout])
    elif pathname == "/performance":
        return html.Div([navbar.navbar, performance_layout])
    elif pathname == "/area":
        return html.Div([navbar.navbar, area_layout])
    else:
        return html.H1("Página no encontrada", style={"textAlign": "center", "marginTop": "40px"})

@server.route('/logout')
def logout():
    from flask_login import logout_user
    logout_user()
    return redirect("/")  # Cambiado para redirigir a la página principal

# Registrar callbacks
register_login_callbacks(app)
register_performance_callbacks(app)
register_area_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)