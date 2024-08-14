from dash import Dash, html, page_container
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from src.components.header import create_header
from src.components.footer import create_footer

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

app.layout = dbc.Container(
    [
        dbc.Row(
            html.Header(
                dbc.Row(
                    dbc.Col(
                        header,
                        className='mb-2',
                        width={'size': 12}
                    ),
                    justify='center'
                ),
            )
        ),
        dbc.Row(
            page_container,
        ),
        dbc.Row(
            html.Footer(
                dbc.Row(
                    dbc.Col(
                        footer,
                        className='mt-2',
                        width={'size': 12}
                    ),
                    justify='center'
                ),
            )
        )
    ],
    fluid=True,
    className='dbc'
)


if __name__ == "__main__":
    app.run_server(debug=True)
