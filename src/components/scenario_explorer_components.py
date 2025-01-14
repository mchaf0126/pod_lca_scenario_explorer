from dash import html
import dash_bootstrap_components as dbc
from src.utils.selection import create_dropdown
from src.utils.load_config import app_config

config = app_config

life_cycle_stage_dropdown_yaml = config.get('life_cycle_stage_dropdown')
assert life_cycle_stage_dropdown_yaml is not None, 'The config for lcs could not be set'

scope_dropdown_yaml = config.get('scope_dropdown')
assert scope_dropdown_yaml is not None, 'The config for cat. dropdowns could not be set'

impact_dropdown_yaml = config.get('impact_dropdown')
assert impact_dropdown_yaml is not None, 'The config for the impact dropdowns could not be set'

category_orders = config.get('category_orders')
assert category_orders is not None, 'The ids for category_orders could not be set'

life_cycle_stage_dropdown = create_dropdown(
    label=life_cycle_stage_dropdown_yaml['label'],
    dropdown_list=life_cycle_stage_dropdown_yaml['dropdown_list'],
    first_item=life_cycle_stage_dropdown_yaml['first_item'],
    dropdown_id=life_cycle_stage_dropdown_yaml['dropdown_id']
)

scope_dropdown = create_dropdown(
    label=scope_dropdown_yaml['label'],
    dropdown_list=scope_dropdown_yaml['dropdown_list'],
    first_item=scope_dropdown_yaml['first_item'],
    dropdown_id=scope_dropdown_yaml['dropdown_id']
)

impact_dropdown = create_dropdown(
    label=impact_dropdown_yaml['label'],
    dropdown_list=impact_dropdown_yaml['dropdown_list'],
    first_item=impact_dropdown_yaml['first_item'],
    dropdown_id=impact_dropdown_yaml['dropdown_id']
)

se_sidebar = dbc.Container(
    [
        dbc.Row(
            [
                life_cycle_stage_dropdown,
                scope_dropdown,
                impact_dropdown
            ]
        ),
        dbc.Row(
            html.Div(id='scenario_card')
        )
    ],
    class_name='p-0 mt-2',
    fluid=True
)
