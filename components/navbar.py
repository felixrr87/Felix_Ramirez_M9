# components/navbar.py

import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
from dash import dcc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Inicio", href="/home")),
        dbc.NavItem(dbc.NavLink("Performance", href="/performance")),
        dbc.NavItem(dbc.NavLink("Área No Competitiva", href="/area")),
        dbc.NavItem(dbc.NavLink("Logout", href="/logout", external_link=True)),
    ],
    brand="Dashboard Deportivo",
    brand_href="/home",
    color="dark",
    dark=True,
    fluid=True,
    style={"padding": "10px 20px", "fontWeight": "bold"}
)
