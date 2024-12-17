"""Results page of dashboard"""
import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import src.utils.general as utils
from src.components.selection import create_dropdown, create_checklist, create_radio
from src.components.a5_components import create_custom_dropdowns
from src.components.load_config import app_config

register_page(__name__, path='/a5_scenario_builder')

layout = html.Div(
    children=[
        dbc.Row(
            dcc.Markdown(
                '''
                # THIS IS STILL IN DEVELOPMENT
                '''
            )
        )
    ]
)

config = app_config

a5_radioitem_yaml = config.get('a5_scenario_radioitem')
assert a5_radioitem_yaml is not None, 'The config for a5 radioitem could not be set'

scope_dropdown_yaml = config.get('scope_dropdown_a5_scenario')
assert scope_dropdown_yaml is not None, 'The config for cat. dropdowns could not be set'

scenario_checklist_yaml = config.get('a5_scenario_checklist')
assert scenario_checklist_yaml is not None, 'The config for scenario checklist could not be set'

equipment_checklist_yaml = config.get('a5_equipment_checklist')
assert equipment_checklist_yaml is not None, 'The config for equip checklist could not be set'

a5_radioitem = create_radio(
    label=a5_radioitem_yaml['label'],
    radiolist=a5_radioitem_yaml['radiolist'],
    first_item=a5_radioitem_yaml['first_item'],
    radio_id=a5_radioitem_yaml['radio_id']
)

scope_dropdown = create_dropdown(
    label=scope_dropdown_yaml['label'],
    dropdown_list=scope_dropdown_yaml['dropdown_list'],
    first_item=scope_dropdown_yaml['first_item'],
    dropdown_id=scope_dropdown_yaml['dropdown_id']
)

impact_dropdown = create_checklist(
    label=scenario_checklist_yaml['label'],
    checklist=scenario_checklist_yaml['checklist'],
    first_item=scenario_checklist_yaml['first_item'],
    dropdown_id=scenario_checklist_yaml['checklist_id']
)

equipment_checklist = create_checklist(
    label=equipment_checklist_yaml['label'],
    checklist=equipment_checklist_yaml['checklist'],
    first_item=equipment_checklist_yaml['first_item'],
    dropdown_id=equipment_checklist_yaml['checklist_id']
)
