from dash import html
import dash_bootstrap_components as dbc
from src.utils.selection import create_checklist, create_radio
from src.utils.load_config import app_config

config = app_config

transportation_checklist_yaml = config.get('transporation_scenario_checklist')
assert transportation_checklist_yaml is not None, 'The config for scenario checklist could not be set'

transportation_custom_checklist_yaml = config.get('transporation_custom_scenario_checklist')
assert transportation_custom_checklist_yaml is not None, 'The config for scenario checklist could not be set'

transportation_radio_yaml = config.get('transporation_scenario_radio')
assert transportation_radio_yaml is not None, 'The config for scenario checklist could not be set'

transportation_checklist = create_checklist(
    label=transportation_checklist_yaml['label'],
    checklist=transportation_checklist_yaml['checklist'],
    first_item=transportation_checklist_yaml['first_item'],
    dropdown_id={"type": "prebuilt_scenario", "id": 'transportation_checklist'}
)

transportation_custom_checklist = create_checklist(
    label=transportation_custom_checklist_yaml['label'],
    checklist=transportation_custom_checklist_yaml['checklist'],
    first_item=transportation_custom_checklist_yaml['first_item'],
    dropdown_id={"type": "prebuilt_scenario", "id": 'transportation_custom_scenario_checklist'}
)

transportation_radio_model_comp = create_radio(
    label=transportation_radio_yaml['label'],
    radiolist=transportation_radio_yaml['radiolist'],
    first_item=transportation_radio_yaml['first_item'],
    radio_id=transportation_radio_yaml['radio_id']
)

a4_special_mat = html.Div(
    [
        dbc.InputGroup(
            [
                dbc.Select(
                    id='transport_custom_mat_type'
                ),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Distance (mi)"),
                dbc.Input(
                    value=0,
                    type="number",
                    id='transport_custom_distance'
                ),
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
                    value=1,
                    id='transport_custom_transport_type'
                ),
            ],
            className="mb-3",
        ),
    ]
)

a4_special_mat_model_comp = html.Div(
    [
        dbc.InputGroup(
            [
                dbc.Select(
                    options=[],
                    id='transport_custom_mat_type_mc'
                ),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Distance (mi)"),
                dbc.Input(
                    placeholder="0",
                    type="number",
                    id='transport_custom_distance_mc'
                ),
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
                    value=1,
                    id='transport_custom_transport_type_mc'
                ),
            ],
            className="mb-3",
        ),
    ]
)

transportation_scenarios = dbc.Container(
    [
        dbc.Row(
            [
                transportation_checklist,
                transportation_custom_checklist,
                a4_special_mat
            ]
        )
    ]
)
