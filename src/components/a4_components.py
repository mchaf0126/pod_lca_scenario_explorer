from dash import html
import dash_bootstrap_components as dbc
from src.components.selection import create_radio, create_checklist
from src.components.load_config import app_config

config = app_config

a4_radioitem_yaml = config.get('a4_scenario_radioitem')
assert a4_radioitem_yaml is not None, 'The config for a4 radioitem could not be set'

scope_dropdown_yaml = config.get('scope_dropdown_a4_scenario')
assert scope_dropdown_yaml is not None, 'The config for cat. dropdowns could not be set'

scenario_checklist_yaml = config.get('a4_scenario_checklist')
assert scenario_checklist_yaml is not None, 'The config for scenario checklist could not be set'

impact_dropdown_yaml = config.get('a4_impact_dropdown')
assert impact_dropdown_yaml is not None, 'The config for the impact dropdowns could not be set'

a4_radioitem = create_radio(
    label=a4_radioitem_yaml['label'],
    radiolist=a4_radioitem_yaml['radiolist'],
    first_item=a4_radioitem_yaml['first_item'],
    radio_id=a4_radioitem_yaml['radio_id']
)

scenario_checklist = create_checklist(
    label=scenario_checklist_yaml['label'],
    checklist=scenario_checklist_yaml['checklist'],
    first_item=scenario_checklist_yaml['first_item'],
    dropdown_id=scenario_checklist_yaml['checklist_id']
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

a4_scenarios = dbc.Card(
    [
        dbc.CardHeader(
            'Transportation Scenarios'
        ),
        dbc.CardBody(
            [
                scenario_checklist,
                a4_special_mat
            ]
        )
    ]
)
