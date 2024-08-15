"""Results page of dashboard"""
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import src.utils.general as utils
from src.components.selection import create_dropdown, create_checklist, create_radio
from src.components.a5_components import create_custom_dropdowns

register_page(__name__, path='/a5_scenario_builder')

current_file_path = Path(__file__)
main_directory = current_file_path.parents[2]
data_directory = main_directory.joinpath('data/tally_commercial_includeBC.csv')

df = pd.read_csv(data_directory, index_col=False)

config_path = main_directory.joinpath('src/components/config.yml')

config = utils.read_yaml(config_path)
assert config is not None, 'The config dictionary could not be set'

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

card_child = dbc.CardBody(
    [
        dbc.Label('Construction Scenarios', class_name='fs-5 fw-bold my-0'),
        html.Hr(),
        a5_radioitem,
    ],
    class_name='pb-0'
)
second_child = dbc.CardBody(
    id='second_card_body_a5',
    class_name='my_0 py-0',
)
special_dropdowns = create_custom_dropdowns()

controls_cont = dbc.Card(
    [
        card_child,
        second_child
    ],
    id='a5_card'
)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        controls_cont
                    ], xs=4, sm=4, md=3, lg=3, xl=3, xxl=3
                ),
                dbc.Col(
                    [
                        dcc.Graph(id="a5_scenario_bar"),
                    ], xs=8, sm=8, md=9, lg=9, xl=9, xxl=9
                ),
            ],
            justify='center',
            className='mb-4'
        ),
    ],
)


@callback(
    Output('second_card_body_a5', 'children'),
    Input('a5_scenario_radioitem', 'value')
)
def update_second_card_body(radio_item):
    if radio_item == 'prebuilt':
        return [impact_dropdown]
    return [special_dropdowns, equipment_checklist]


@callback(
    Output('a5_scenario_bar', 'figure'),
    [
        Input('a5_scenario_checklist', 'value'),
    ]
)
def update_chart(checklist_value):

    # update with actual logic
    percent_dict = {
        '1_all_elec_equip': 25,
        '2_waste_recovery': 50,
        '3_off_site_fab': 85
    }
    new_df = df.replace(
        [
            '[A1-A3] Product',
            '[A4] Transportation',
            '[B2-B5] Maintenance and Replacement',
            '[C2-C4] End of Life',
            '[D] Module D'
        ],
        'Other Life Cycle Stages'
    )
    new_df = pd.melt(
        new_df,
        id_vars="Life Cycle Stage",
        value_vars='Global Warming Potential Total (kgCO2eq)',
        var_name='Impacts',
        value_name='Impact Amount'
    )
    new_df = new_df.groupby("Life Cycle Stage").sum()
    new_df['Impacts'] = '0_avg_construction'

    list_of_dfs = [new_df]
    for num in checklist_value:
        temp = df.copy()
        temp.loc[
            temp['Life Cycle Stage'] == '[A5] Construction',
            'Global Warming Potential Total (kgCO2eq)'
        ] = temp['Global Warming Potential Total (kgCO2eq)'] * (1 - (percent_dict.get(num) / 100))
        temp = temp.replace(
            [
                '[A1-A3] Product',
                '[A4] Transportation',
                '[B2-B5] Maintenance and Replacement',
                '[C2-C4] End of Life',
                '[D] Module D'
            ],
            'Other Life Cycle Stages'
        )
        temp_eol_adjusted_df = pd.melt(
            temp,
            id_vars="Life Cycle Stage",
            value_vars='Global Warming Potential Total (kgCO2eq)',
            var_name='Impacts',
            value_name='Impact Amount'
        )
        temp_eol_adjusted_df = temp_eol_adjusted_df.groupby('Life Cycle Stage').sum()
        temp_eol_adjusted_df['Impacts'] = num

        list_of_dfs.append(temp_eol_adjusted_df)

    checklist_df = pd.concat(list_of_dfs).sort_index(ascending=False)

    fig = px.bar(
        checklist_df,
        x='Impacts',
        y='Impact Amount',
        color=checklist_df.index,
        color_discrete_map={
            'Other Life Cycle Stages': '#D3D3D3',
            '[A5] Construction': '#652e98'
        }
    ).update_yaxes(
        title='Total Global Warming Potential by Life Cycle Stage',
        tickformat=',.0f',
    ).update_xaxes(
        title='',
        categoryorder='category ascending'
    )

    fig.update_traces(width=.2 + .2 * len(checklist_value))
    if len(checklist_value) > 3:
        fig.update_traces(width=.8)

    return fig
