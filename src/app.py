from dash import Dash, page_container, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from src.components.header import create_header
from src.components.footer import create_footer
from src.components.sidebar import create_sidebar

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.PULSE, dbc_css]
)

load_figure_template('pulse')

header = create_header()
footer = create_footer()
sidebar = create_sidebar()

app.layout = dbc.Container(
    [
        dcc.Store(
            id='template_model_name',
            storage_type='session'
        ),
        dbc.Row(
            [
                dbc.Col(
                    sidebar,
                    xs=3, sm=3, md=2, lg=2, xl=2, xxl=2,
                    style={
                        "top": 0,
                        "left": 0,
                        "bottom": 0,
                        "width": "14rem",
                        "padding": "1rem",
                        "background-color": "#f8f9fa",
                    }
                ),
                dbc.Col(
                    dbc.Container(
                        [
                            dbc.Row(
                                dbc.Col(
                                    header,
                                    className='mb-2',
                                    width={'size': 12}
                                ),
                                justify='center'
                            ),
                            dbc.Row(
                                dbc.Col(
                                    page_container,
                                    class_name='gy-5',
                                    xs=9, sm=9, md=10, lg=10, xl=10, xxl=10
                                )
                            ),
                            dbc.Row(
                                dbc.Row(
                                    dbc.Col(
                                        footer,
                                        className='mt-2',
                                        width={'size': 12}
                                    ),
                                    justify='center'
                                ),
                            )
                        ],
                        fluid=True,
                        class_name='p-0'
                    ),
                    class_name='p-0'
                )
            ],
        )
    ],
    fluid=True,
    className='dbc'
)


if __name__ == "__main__":
    app.run_server(debug=True)
