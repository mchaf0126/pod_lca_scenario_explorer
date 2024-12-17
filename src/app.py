from pathlib import Path
from dash import Dash, page_container, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
from dash_bootstrap_templates import load_figure_template
from src.utils.header import create_header
from src.utils.sidebar import create_sidebar

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.PULSE, dbc_css]
)

current_file_path = Path(__file__)
main_directory = current_file_path.parents[1]
tm_metadata_df = pd.read_csv(main_directory.joinpath('data/frontend/project_metadata.csv'))
tm_impacts_df = pd.read_csv(main_directory.joinpath('data/frontend/combined_impacts.csv'))

load_figure_template('pulse')

header = create_header()
sidebar = create_sidebar()

app.layout = dbc.Container(
    [
        dcc.Store(
            id='template_model_name',
            storage_type='session'
        ),
        dcc.Store(
            id='template_model_metadata',
            storage_type='session',
        ),
        dcc.Store(
            id='template_model_impacts',
            storage_type='session',
        ),
        dbc.Row(
            [
                dbc.Col(
                    sidebar,
                    xs=3, sm=3, md=2, lg=2, xl=2, xxl=2,
                    style={
                        "width": "14rem",
                        'position': 'relative'
                    },
                    class_name='p-3 bg-light'
                ),
                dbc.Col(
                    dbc.Container(
                        [
                            dbc.Row(
                                dbc.Col(
                                    header,
                                    className='',
                                    width={'size': 12}
                                ),
                                justify='center'
                            ),
                            dbc.Row(
                                dbc.Col(
                                    page_container,
                                    class_name='',
                                    xs=12, sm=12, md=12, lg=12, xl=12, xxl=12
                                ),
                            ),
                        ],
                        fluid=True,
                        class_name='p-0'
                    ),
                    class_name='p-0'
                )
            ],
            class_name='vh-100'
        )
    ],
    fluid=True,
    className='dbc'
)


@callback(
    Output(component_id='template_model_metadata', component_property='data'),
    Input(component_id='template_model_metadata', component_property='data')
)
def load_tm_metadata(_):
    return {'tm_metadata': tm_metadata_df.to_dict()}


@callback(
    Output(component_id='template_model_impacts', component_property='data'),
    Input(component_id='template_model_impacts', component_property='data')
)
def load_tm_impacts(_):
    return {'tm_impacts': tm_impacts_df.to_dict()}


if __name__ == "__main__":
    app.run_server(debug=True)
