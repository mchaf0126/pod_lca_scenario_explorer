from dash import html
import dash_bootstrap_components as dbc
from src.utils.selection import create_checklist
from src.utils.load_config import app_config

config = app_config

eol_checklist_yaml = config.get('eol_scenario_checklist')
assert eol_checklist_yaml is not None, 'The config for scenario checklist could not be set'

eol_checklist = create_checklist(
    label=eol_checklist_yaml['label'],
    checklist=eol_checklist_yaml['checklist'],
    first_item=eol_checklist_yaml['first_item'],
    dropdown_id=eol_checklist_yaml['checklist_id']
)

eol_form = html.Div(
    [
        dbc.Label('Custom Mix'),
        dbc.InputGroup(
            [
                dbc.InputGroupText("% Landfill"),
                dbc.Input(placeholder="percent", type="number"),
                dbc.InputGroupText("%"),
            ],
            className="mb-1",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("% Incineration"),
                dbc.Input(placeholder="percent", type="number"),
                dbc.InputGroupText("%"),
            ],
            className="mb-1",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("% Recycling"),
                dbc.Input(placeholder="percent", type="number"),
                dbc.InputGroupText("%"),
            ],
            className="mb-1",
        ),
    ],
    className='mb-3'
)

eol_special_material = html.Div(
    [
        dbc.Label("Custom Scenario"),
        dbc.InputGroup(
            [
                dbc.Select(
                    options=[
                        {"label": "CLT Floor", "value": 1},
                        {"label": "Glulam Beam", "value": 2},
                    ],
                    value=1
                ),
            ],
            className="mb-1",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("% Reuse"),
                dbc.Input(placeholder="percent", type="number"),
                dbc.InputGroupText("%"),
            ],
            className="mb-3",
        ),
    ]
)

eol_scenarios = dbc.Card(
    [
        dbc.CardHeader(
            'Construction Scenarios'
        ),
        dbc.CardBody(
            [
                eol_checklist,
                eol_form,
                eol_special_material
            ]
        )
    ]
)
