from dash import html
import dash_bootstrap_components as dbc
from src.utils.selection import create_checklist, create_radio
from src.utils.load_config import app_config

config = app_config

replacement_checklist_yaml = config.get('replacement_scenario_checklist')
assert replacement_checklist_yaml is not None, 'The config for scenario checklist could not be set'

replacement_radio_yaml = config.get('replacement_scenario_radio')
assert replacement_radio_yaml is not None, 'The config for scenario radio could not be set'

replacement_checklist = create_checklist(
    label=replacement_checklist_yaml['label'],
    checklist=replacement_checklist_yaml['checklist'],
    first_item=replacement_checklist_yaml['first_item'],
    dropdown_id={"type": "prebuilt_scenario", "id": 'replacement_checklist'}
)

replacement_radio_model_comp = create_radio(
    label=replacement_radio_yaml['label'],
    radiolist=replacement_radio_yaml['radiolist'],
    first_item=replacement_radio_yaml['first_item'],
    radio_id=replacement_radio_yaml['radio_id']
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
                    value=1,
                    id='replacement_custom_mat_type'
                ),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Replacement Rate (yr)"),
                dbc.Input(
                    placeholder="0",
                    type="number",
                    id='replacement_custom_year'
                ),
            ],
            className="mb-3",
        ),
    ]
)

replacement_special_mat_model_comp = html.Div(
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
                    value=1,
                    id='replacement_custom_mat_type_mc'
                ),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Replacement Rate (yr)"),
                dbc.Input(
                    placeholder="0",
                    type="number",
                    id='replacement_custom_year_mc'
                ),
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
