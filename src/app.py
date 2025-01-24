from pathlib import Path
from dash import Dash, page_container, dcc
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
tm_metadata_df = pd.read_pickle(main_directory.joinpath('data/frontend/project_metadata.pkl'))
tm_impacts_df = pd.read_pickle(main_directory.joinpath('data/frontend/combined_impacts.pkl')).reset_index()
prebuilt_scenario_impacts_df = pd.read_pickle(main_directory.joinpath('data/frontend/combined_prebuilt_scenarios.pkl')).reset_index()
trans_emissions_df = pd.read_pickle(main_directory.joinpath('references/background_data/a4_emissions.pkl'))

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
            data={
                'tm_metadata': tm_metadata_df.to_dict()
            },
            id='template_model_metadata',
            storage_type='memory',
        ),
        dcc.Store(
            data={
                'tm_impacts': tm_impacts_df.to_dict()
            },
            id='template_model_impacts',
            storage_type='memory',
        ),
        dcc.Store(
            id='current_tm_impacts',
            storage_type='session',
        ),
        dcc.Store(
            data={
                'prebuilt_scenario_impacts': prebuilt_scenario_impacts_df.to_dict()
            },
            id='prebuilt_scenario_impacts',
            storage_type='memory',
        ),
        dcc.Store(
            id='current_pb_impacts',
            storage_type='session',
        ),
        dcc.Store(
            data={
                'transportation_emission_factors': trans_emissions_df.to_dict()
            },
            id='transportation_emission_factors',
            storage_type='memory',
        ),
        dcc.Store(
            id='intentional_sourcing_impacts',
            storage_type='memory'
        ),
        dcc.Store(
            id='intentional_replacement_impacts',
            storage_type='memory'
        ),
        dcc.Store(
            id='intentional_sourcing_impacts_mc',
            storage_type='memory'
        ),
        dcc.Store(
            id='intentional_replacement_impacts_mc',
            storage_type='memory'
        ),
        dcc.Store(
            id='user_defined_impacts',
            storage_type='memory'
        ),
        dbc.Row(
            [
                dbc.Col(
                    sidebar,
                    xs=3, sm=3, md=2, lg=2, xl=2, xxl=2,
                    style={
                        "width": "14rem",
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
        )
    ],
    fluid=True,
    className='dbc'
)


if __name__ == "__main__":
    app.run_server(debug=True)
