from dash import html
import dash_bootstrap_components as dbc
from src.utils.selection import create_checklist
from src.utils.load_config import app_config

config = app_config

replacement_checklist_yaml = config.get('replacement_scenario_checklist')
assert replacement_checklist_yaml is not None, 'The config for scenario checklist could not be set'

replacement_checklist = create_checklist(
    label=replacement_checklist_yaml['label'],
    checklist=replacement_checklist_yaml['checklist'],
    first_item=replacement_checklist_yaml['first_item'],
    dropdown_id={"type": "prebuilt_scenario", "id": 'replacement_checklist'}
)

replacement_special_mat = html.Div(
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
                dbc.InputGroupText("Replacement Rate (yr)"),
                dbc.Input(placeholder="0", type="number"),
            ],
            className="mb-3",
        ),
    ]
)

replacement_scenarios = dbc.Card(
    [
        dbc.CardHeader(
            'Replacement Scenarios'
        ),
        dbc.CardBody(
            [
                replacement_checklist,
                replacement_special_mat
            ]
        )
    ]
)
