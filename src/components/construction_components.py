from dash import html, dcc
import dash_bootstrap_components as dbc
from src.utils.selection import create_checklist
from src.utils.load_config import app_config

config = app_config

construction_checklist_yaml = config.get('a5_scenario_checklist')
assert construction_checklist_yaml is not None, 'The config for scenario checklist could not be set'

equipment_checklist_yaml = config.get('a5_equipment_checklist')
assert equipment_checklist_yaml is not None, 'The config for equip checklist could not be set'


construction_checklist = create_checklist(
    label=construction_checklist_yaml['label'],
    checklist=construction_checklist_yaml['checklist'],
    first_item=construction_checklist_yaml['first_item'],
    dropdown_id=construction_checklist_yaml['checklist_id']
)

equipment_checklist = create_checklist(
    label=equipment_checklist_yaml['label'],
    checklist=equipment_checklist_yaml['checklist'],
    first_item=equipment_checklist_yaml['first_item'],
    dropdown_id=equipment_checklist_yaml['checklist_id']
)

construction_dropdowns = html.Div(
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

construction_scenarios = dbc.Card(
    [
        dbc.CardHeader(
            'Construction Scenarios'
        ),
        dbc.CardBody(
            [
                construction_checklist,
                equipment_checklist,
                construction_dropdowns
            ]
        )
    ]
)
