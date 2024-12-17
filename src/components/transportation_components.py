from dash import html
import dash_bootstrap_components as dbc
from src.utils.selection import create_checklist
from src.utils.load_config import app_config

config = app_config

transportation_checklist_yaml = config.get('transporation_scenario_checklist')
assert transportation_checklist_yaml is not None, 'The config for scenario checklist could not be set'

transportation_checklist = create_checklist(
    label=transportation_checklist_yaml['label'],
    checklist=transportation_checklist_yaml['checklist'],
    first_item=transportation_checklist_yaml['first_item'],
    dropdown_id={"type": "prebuilt_scenario", "id": 'transportation_checklist'}
)

a4_special_mat = html.Div(
    [
        dbc.Label("Custom Scenario"),
        dbc.InputGroup(
            [
                dbc.Select(
                    options=[
                        {"label": "Wood fiber insulation", "value": 1},
                        {"label": "CLT", "value": 2},
                        {"label": "Glulam", "value": 3}
                    ],
                    value=1
                ),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Distance (mi)"),
                dbc.Input(placeholder="0", type="number"),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Transport Type"),
                dbc.Select(
                    options=[
                        {"label": "Truck", "value": 1},
                        {"label": "Rail", "value": 2},
                        {"label": "Barge", "value": 3},
                    ],
                    value=1
                ),
            ],
            className="mb-3",
        ),
    ]
)

transportation_scenarios = dbc.Card(
    [
        dbc.CardHeader(
            'Transportation Scenarios'
        ),
        dbc.CardBody(
            [
                transportation_checklist,
                a4_special_mat
            ]
        )
    ]
)
