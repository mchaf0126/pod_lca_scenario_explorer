import dash_bootstrap_components as dbc
from src.utils.selection import create_checklist, create_radio
from src.utils.load_config import app_config

config = app_config

construction_checklist_yaml = config.get('construction_scenario_checklist')
assert construction_checklist_yaml is not None, 'The config for scenario checklist could not be set'

construction_radio_yaml = config.get('construction_scenario_radio')
assert construction_radio_yaml is not None, 'The config for scenario checklist could not be set'

construction_checklist = create_checklist(
    label=construction_checklist_yaml['label'],
    checklist=construction_checklist_yaml['checklist'],
    first_item=construction_checklist_yaml['first_item'],
    dropdown_id={"type": "prebuilt_scenario", "id": 'construction_checklist'}
)

construction_radio_model_comp = create_radio(
    label=construction_radio_yaml['label'],
    radiolist=construction_radio_yaml['radiolist'],
    first_item=construction_radio_yaml['first_item'],
    radio_id=construction_radio_yaml['radio_id']
)

construction_scenarios = dbc.Card(
    [
        dbc.CardHeader(
            'Construction Scenarios'
        ),
        dbc.CardBody(
            [
                construction_checklist,
            ]
        )
    ]
)
