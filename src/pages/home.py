from pathlib import Path
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc


register_page(__name__, path='/')

current_file_path = Path(__file__)
main_directory = current_file_path.parents[2]

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            '''
                            #### Milestone M3.3, Due Q10 - January 24, 2025
                            '''
                        ),
                        dcc.Markdown(
                            '''
                            “Delivery of structured cradle-to-grave WBLCA template models
                            with modeled scenarios to compare at least five mid/endpoint impact
                            categories including GWP/climate change, dynamic impacts over the
                            lifetime of the building, supply chain impacts including land use /
                            land use change of input materials, and end-of-life impacts of HESTIA
                            building designs to those of conventional
                            building practice/assemblies/materials.”
                            ''',
                            className='fw-light'
                        ),
                        html.Br(),
                        dcc.Markdown(
                            '''
                            #### About the dashboard
                            '''
                        ),
                        dcc.Markdown(
                            '''
                            At present, the dashboard is in beta. There are
                            currently two types of pages of note:
                            *  **Results** - the traditional results for a WBLCA.
                            *  **Scenarios** - These will show different scenarios
                            built by the UW Team to enable the user to compare different
                            scenarios against the template model. There are currently four
                            different scenarios mocked up in this dashboard:
                               *  **Transportation Scenarios**
                               *  **Construction Scenarios**
                               *  **Replacement Scenarios**
                               *  **End-of-life Scenarios**
                            ''',
                            className='fw-light'
                        ),
                    ],
                    width={"size": 8},
                    class_name='pe-5'
                ),
            ],
            justify='center',
            className='m-2'
        ),
    ]
)
