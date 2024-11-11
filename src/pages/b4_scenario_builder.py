"""Results page of dashboard"""
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import src.utils.general as utils
from src.components.selection import create_dropdown, create_checklist, \
    create_radio
from src.components.b4_components import create_custom_dropdowns

register_page(__name__, path='/b4_scenario_builder')

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

# current_file_path = Path(__file__)
# main_directory = current_file_path.parents[2]
# data_directory = main_directory.joinpath('data/tally_commercial_includeBC.csv')

# df = pd.read_csv(data_directory, index_col=False)

# config_path = main_directory.joinpath('src/components/config.yml')

# config = utils.read_yaml(config_path)
# assert config is not None, 'The config dictionary could not be set'

# b4_radioitem_yaml = config.get('b4_scenario_radioitem')
# assert b4_radioitem_yaml is not None, 'The config for b4 radioitem could not be set'

# scope_dropdown_yaml = config.get('scope_dropdown_b4_scenario')
# assert scope_dropdown_yaml is not None, 'The config for cat. dropdowns could not be set'

# scenario_checklist_yaml = config.get('b4_scenario_checklist')
# assert scenario_checklist_yaml is not None, 'The config for scenario checklist could not be set'

# b4_radioitem = create_radio(
#     label=b4_radioitem_yaml['label'],
#     radiolist=b4_radioitem_yaml['radiolist'],
#     first_item=b4_radioitem_yaml['first_item'],
#     radio_id=b4_radioitem_yaml['radio_id']
# )

# scope_dropdown = create_dropdown(
#     label=scope_dropdown_yaml['label'],
#     dropdown_list=scope_dropdown_yaml['dropdown_list'],
#     first_item=scope_dropdown_yaml['first_item'],
#     dropdown_id=scope_dropdown_yaml['dropdown_id']
# )

# impact_dropdown = create_checklist(
#     label=scenario_checklist_yaml['label'],
#     checklist=scenario_checklist_yaml['checklist'],
#     first_item=scenario_checklist_yaml['first_item'],
#     dropdown_id=scenario_checklist_yaml['checklist_id']
# )

# card_child = dbc.CardBody(
#     [
#         dbc.Label('Use Stage Scenarios', class_name='fs-5 fw-bold my-0'),
#         html.Hr(),
#         b4_radioitem,
#     ],
#     class_name='pb-0'
# )
# second_child = dbc.CardBody(
#     id='second_card_body_b4',
#     class_name='my_0 py-0',
# )
# form = create_custom_dropdowns()


# controls_cont = dbc.Card(
#     [
#         card_child,
#         second_child
#     ],
#     id='b4_card'
# )

# layout = html.Div(
#     children=[
#         dbc.Row(
#             [
#                 dbc.Col(
#                     [
#                         controls_cont
#                     ], xs=4, sm=4, md=3, lg=3, xl=3, xxl=3
#                 ),
#                 dbc.Col(
#                     [
#                         dcc.Graph(id="b4_scenario_bar"),
#                     ], xs=8, sm=8, md=9, lg=9, xl=9, xxl=9
#                 ),
#             ],
#             justify='center',
#             className='mb-4'
#         ),
#     ],
# )


# @callback(
#     Output('second_card_body_b4', 'children'),
#     Input('b4_scenario_radioitem', 'value')
# )
# def update_second_card_body(radio_item):
#     if radio_item == 'prebuilt':
#         return [scope_dropdown, impact_dropdown]
#     return [form]


# @callback(
#     Output('b4_scenario_bar', 'figure'),
#     [
#         Input('scope_dropdown_b4_scenario', 'value'),
#         Input('b4_scenario_checklist', 'value'),
#     ]
# )
# def update_chart(scope, checklist_value):

#     # update with actual logic
#     percent_dict = {
#         '1_rics_repl_rates': 70,
#         '2_ashrae_repl_rates': 30,
#     }
#     new_df = pd.melt(
#         df,
#         id_vars=scope,
#         value_vars='Global Warming Potential Total (kgCO2eq)',
#         var_name='Impacts',
#         value_name='Impact Amount'
#     )
#     new_df = new_df.groupby(scope).sum()
#     new_df['Impacts'] = '0_default_eol'

#     list_of_dfs = [new_df]
#     for num in checklist_value:
#         temp = df.copy()
#         temp.loc[
#             temp['Life Cycle Stage'] == '[B2-B5] Maintenance and Replacement',
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
#         title='',
#         categoryorder='category ascending'
#     )

#     fig.update_traces(width=.2 + .2 * len(checklist_value))
#     if len(checklist_value) > 3:
#         fig.update_traces(width=.8)

#     return fig
