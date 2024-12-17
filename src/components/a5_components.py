from dash import html, dcc
import dash_bootstrap_components as dbc


def create_custom_dropdowns() -> html.Div:
    """_summary_

    Returns:
        html.Div: _description_
    """
    custom_dropdowns = html.Div(
        [
            html.Div(
                [
                    dbc.Label('Crane Type'),
                    dcc.Dropdown(
                        options=[
                            'No Crane',
                            'Mobile Crane',
                            'Tower Crane'
                        ],
                        value='No Crane',
                        id='custom_a5_crane_id',
                        clearable=False,
                        className='mb-3'
                    ),
                ],
            ),
            html.Div(
                [
                    dbc.Label('Stories Above Grade'),
                    dcc.Slider(
                        min=0,
                        max=5,
                        step=1,
                        value=0,
                        id='custom_a5_slider_id',
                        className='mb-3'
                    ),
                ],
            ),
            html.Div(
                [
                    dbc.Label('On Site Equipment'),
                    dcc.Dropdown(
                        options=[
                            'Business as Usual',
                            'Low Diesel Consumption',
                            'All Electric'
                        ],
                        value='Business as Usual',
                        id='custom_a5_equipment_id',
                        clearable=False,
                        className='mb-3'
                    ),
                ],
            ),
        ],
        className='mb-3'
    )
    return custom_dropdowns

# a5_scenarios = dbc.Card(
#     [
#         dbc.CardHeader(
#             'Transportation Scenarios'
#         ),
#         dbc.CardBody(
#             [
#                 scenario_checklist,
#                 a4_special_mat
#             ]
#         )
#     ]
# )
