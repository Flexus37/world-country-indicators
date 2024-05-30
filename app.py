import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html

from pages import all_map, country, indicators

external_stylesheets = [dbc.themes.MATERIA]
app = Dash(__name__, external_stylesheets=external_stylesheets,  use_pages=True)
app.config.suppress_callback_exceptions = True


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "17rem",
    "padding": "2rem 1rem",
    "color": 'white',
    "background-color": "#444", # Цвет фона боковой панели
    "box-shadow": "7px 0 15px #888"
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    }

sidebar = html.Div(
    [
        html.H2("Показатели стран мира", className="display-6"),
        html.Hr(),
        html.P(
            "Учебный проект студента БСБО-15-21 Дудин Алексея", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Карта мира", href="/", active="exact"),
                dbc.NavLink("Страны", href="/country", active="exact"),
                dbc.NavLink("Статистика", href="/indicators", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return all_map.layout
    elif pathname == "/country":
        return country.layout
    elif pathname == "/indicators":
        return indicators.layout
    # 404
    return html.Div(
        [
            html.H1("404: Страница не найдена", className="text-danger"),
            html.Hr(),
            html.P(f"Путь {pathname} не найден..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == '__main__':
        app.run_server(debug=True)

