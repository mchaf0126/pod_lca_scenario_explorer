from dash import html, callback, Input, Output
import dash_bootstrap_components as dbc
from src.utils.selection import create_dropdown
from src.components.transportation_components import transportation_scenarios
from src.components.construction_components import construction_scenarios
from src.components.replacement_components import replacement_scenarios
from src.components.eol_components import eol_scenarios
from src.utils.load_config import app_config

config = app_config

life_cycle_stage_dropdown_yaml = config.get('life_cycle_stage_dropdown')
assert life_cycle_stage_dropdown_yaml is not None, 'The config for lcs could not be set'

scope_dropdown_yaml = config.get('scope_dropdown')
assert scope_dropdown_yaml is not None, 'The config for cat. dropdowns could not be set'

impact_dropdown_yaml = config.get('impact_dropdown')
assert impact_dropdown_yaml is not None, 'The config for the impact dropdowns could not be set'

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

scenario_explorer_layout = html.Div(
    children=[
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            se_sidebar
                        ], xs=2, sm=2, md=2, lg=2, xl=2, xxl=2,
                        class_name=''
                    ),
                    # dbc.Col(
                    #     [
                    #         sec.display_data
                    #     ], xs=6, sm=6, md=6, lg=6, xl=6, xxl=6,
                    #     class_name=''
                    # ),
                    # dbc.Col(
                    #     [
                    #         sec.description
                    #     ], xs=4, sm=4, md=4, lg=4, xl=4, xxl=4
                    # ),
                ],
                # justify='center',
                className='vh-100'
            ),
            fluid=True,
            class_name='mw-100'
        ),
    ],
)


@callback(
    Output('scenario_card', 'children'),
    Input('life_cycle_stage_dropdown', 'value')
)
def update_scenario_card(life_cycle_stage):
    if life_cycle_stage == 'Transportation':
        return transportation_scenarios
    elif life_cycle_stage == 'Construction':
        return construction_scenarios
    elif life_cycle_stage == 'Replacement':
        return replacement_scenarios
    elif life_cycle_stage == 'End-of-life':
        return eol_scenarios
    else:
        return "try again!"
