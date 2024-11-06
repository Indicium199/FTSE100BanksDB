# welcome.py
import dash
from dash import html
def create_welcome_tab():
    return html.Div([
        html.H1("Welcome to the Dashboard"),
        html.P("This is your homepage. Here you can find an overview of all the information available in the dashboard."),
        html.Img(src='https://via.placeholder.com/400', alt='Welcome Image'),  # Placeholder image
        html.Hr(),
        html.P("Feel free to explore the other tabs to access detailed information.")
    ])
