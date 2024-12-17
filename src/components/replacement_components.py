from dash import html, dcc
import dash_bootstrap_components as dbc
from src.utils.selection import create_checklist
from src.utils.load_config import app_config

config = app_config

replacement_checklist_yaml = config.get('b4_scenario_checklist')
assert replacement_checklist_yaml is not None, 'The config for scenario checklist could not be set'

replacement_checklist = create_checklist(
    label=replacement_checklist_yaml['label'],
    checklist=replacement_checklist_yaml['checklist'],
    first_item=replacement_checklist_yaml['first_item'],
    dropdown_id=replacement_checklist_yaml['checklist_id']
)

replacement_custom_dropdowns = html.Div(
    [
        html.Div(
            [
                dbc.Label('Envelope'),
                dcc.Dropdown(
                    options=[
                        '20 Year Full Replacement',
                        '25 Year Full Replacement',
                        '40 Year Full Replacement'
                    ],
                    value='20 Year Full Replacement',
                    id='custom_b4_envelope_id',
                    clearable=False,
                    className='mb-3'
                ),
            ],
        ),
        html.Div(
            [
                dbc.Label('Finishes'),
                dcc.Dropdown(
                    options=[
                        '20 Year Full Replacement',
                        '25 Year Full Replacement',
                        '40 Year Full Replacement'
                    ],
                    value='20 Year Full Replacement',
                    id='custom_b4_finishes_id',
                    clearable=False,
                    className='mb-3'
                ),
            ],
        ),
        html.Div(
            [
                dbc.Label('Circularity'),
                dcc.Dropdown(
                    options=[
                        '20% Design for Deconstruction',
                        '40% Design for Deconstruction',
                        '60% Design for Deconstruction'
                    ],
                    value='20% Design for Deconstruction',
                    id='custom_b4_circularity_id',
                    clearable=False,
                    className='mb-3'
                ),
            ],
        ),
    ],
    className='mb-3'
)

replacement_scenarios = dbc.Card(
    [
        dbc.CardHeader(
            'Replacement Scenarios'
        ),
        dbc.CardBody(
            [
                replacement_checklist,
                replacement_custom_dropdowns
            ]
        )
    ]
)
