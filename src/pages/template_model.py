"""Results page of dashboard"""
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import src.utils.general as utils
from src.components.selection import create_dropdown, create_checklist, \
    create_radio
from src.components.a4_components import create_special_material_form

register_page(__name__, path='/template_model')

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

current_file_path = Path(__file__)
main_directory = current_file_path.parents[2]

config_path = main_directory.joinpath('src/components/config.yml')

config = utils.read_yaml(config_path)
assert config is not None, 'The config dictionary could not be set'

tm_dropdown_yaml = config.get('tm_dropdown')
assert tm_dropdown_yaml is not None, 'The config for tm dropdown could not be set'

tm_dropdown = create_dropdown(
    label=tm_dropdown_yaml['label'],
    dropdown_list=tm_dropdown_yaml['dropdown_list'],
    first_item=tm_dropdown_yaml['first_item'],
    dropdown_id=tm_dropdown_yaml['dropdown_id']
)


card_child = dbc.CardBody(
    [
        dbc.Label('Template Model Selector', class_name='fs-5 fw-bold my-0'),
        html.Hr(),
        tm_dropdown,
    ],
    class_name='pb-0'
)

tm_controls = dbc.Card(
    [
        card_child,
    ],
    id='dropdown_card'
)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        tm_controls
                    ], xs=4, sm=4, md=3, lg=3, xl=3, xxl=3
                ),
                dbc.Col(
                    [
                        dcc.Markdown('''
                                     THIS IS STILL IN DEVELOPMENT
                                     ''')
                    ], xs=8, sm=8, md=9, lg=9, xl=9, xxl=9
                ),
            ],
            justify='center',
            className='mb-4'
        ),
    ],
)


# @callback(
#     Output('second_card_body_a4', 'children'),
#     Input('a4_scenario_radioitem', 'value')
# )
# def update_second_card_body(radio_item):
#     if radio_item == 'prebuilt':
#         return [scope_dropdown, impact_dropdown]
#     return [special_mat_1, special_mat_2]


# @callback(
#     Output('a4_scenario_bar', 'figure'),
#     [
#         Input('scope_dropdown_a4_scenario', 'value'),
#         Input('a4_scenario_checklist', 'value'),
#     ]
# )
# def update_chart(scope, checklist_value):

#     # update with actual logic
#     percent_dict = {
#         '1_us_avg_dist': 25,
#         '2_global_avg_dist': 50,
#         '3_elec_vehicles': 75
#     }
#     new_df = pd.melt(
#         df,
#         id_vars=scope,
#         value_vars='Global Warming Potential Total (kgCO2eq)',
#         var_name='Impacts',
#         value_name='Impact Amount'
#     )
#     new_df = new_df.groupby(scope).sum()
#     new_df['Impacts'] = '0_default_transport'

#     list_of_dfs = [new_df]
#     for num in checklist_value:
#         temp = df.copy()
#         temp.loc[
#             temp['Life Cycle Stage'] == '[A4] Transportation',
#             'Global Warming Potential Total (kgCO2eq)'
#         ] = temp['Global Warming Potential Total (kgCO2eq)'] * (1 - (percent_dict.get(num) / 100))
#         temp_eol_adjusted_df = pd.melt(
#             temp,
#             id_vars=scope,
#             value_vars='Global Warming Potential Total (kgCO2eq)',
#             var_name='Impacts',
#             value_name='Impact Amount'
#         )
#         temp_eol_adjusted_df = temp_eol_adjusted_df.groupby(scope).sum()
#         temp_eol_adjusted_df['Impacts'] = num

#         list_of_dfs.append(temp_eol_adjusted_df)

#     checklist_df = pd.concat(list_of_dfs)

#     fig = px.bar(
#         checklist_df,
#         x='Impacts',
#         y='Impact Amount',
#         color=checklist_df.index,
#     ).update_yaxes(
#         title=f'Total Global Warming Potential by {scope}',
#         tickformat=',.0f',
#     ).update_xaxes(
#         categoryorder='category ascending',
#         title=''
#     )
#     fig.update_traces(width=.2 + .2 * len(checklist_value))
#     if len(checklist_value) > 2:
#         fig.update_traces(width=.8)

#     return fig
