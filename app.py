import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Initialize Dash app with pages
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Define the navigation layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Investors & Distribution", href="/page-2")),
            dbc.NavItem(dbc.NavLink("Acquisitions & SWOT", href="/page-3")),
        ],
        brand="PropTech Market Study",
        brand_href="/",
        color="primary",
        dark=True,
    ),
    html.Div(id='page-content')
])

# Page 1: Overview of PropTech Technologies
def page_1_layout():
    return html.Div([
        html.H1("PropTech Technologies Overview"),
        html.P("Introduction to PropTech technologies and their impact."),
        dbc.Row([
            dbc.Col(
                dbc.Accordion([
                    dbc.AccordionItem("Definition of Technology A", title="Technology A"),
                    dbc.AccordionItem("Definition of Technology B", title="Technology B"),
                    dbc.AccordionItem("Definition of Technology C", title="Technology C"),
                ], start_collapsed=True), width=4
            ),
            dbc.Col(
                dcc.Graph(id='tech-frequency-boxplot'), width=8
            )
        ])
    ])

# Page 2: Investors in Tech & PropTech Distribution in France
def page_2_layout():
    return html.Div([
        html.H1("Investors in Tech & PropTech Distribution in France"),
        dcc.Graph(id='investors-tech-display'),
        dcc.Graph(id='proptech-map')
    ])

# Page 3: Potential Acquisitions & SWOT Analysis
def page_3_layout():
    return html.Div([
        html.H1("Potential Acquisitions & SWOT Analysis"),
        dcc.Graph(id='top-companies-display'),
        html.Div(id='swot-analysis')
    ])

# Callback to update page content
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-2':
        return page_2_layout()
    elif pathname == '/page-3':
        return page_3_layout()
    return page_1_layout()

if __name__ == '__main__':
    app.run_server(debug=True)

server = app.server
