"""Results page of dashboard"""
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import src.utils.general as utils
from src.components.selection import create_dropdown, create_checklist

register_page(__name__, path='/eol_scenario_builder')

current_file_path = Path(__file__)
main_directory = current_file_path.parents[2]
data_directory = main_directory.joinpath('data/tally_commercial_includeBC.csv')

df = pd.read_csv(data_directory, index_col=False)

config_path = main_directory.joinpath('src/components/config.yml')

config = utils.read_yaml(config_path)
assert config is not None, 'The config dictionary could not be set'

scope_dropdown_yaml = config.get('scope_dropdown_eol_scenario')
assert scope_dropdown_yaml is not None, 'The config for cat. dropdowns could not be set'

scenario_checklist_yaml = config.get('eol_scenario_checklist')
assert scenario_checklist_yaml is not None, 'The config for scenario checklist could not be set'

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

controls_cont = dbc.Card(
    [scope_dropdown, impact_dropdown],
    body=True,
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
                        dcc.Graph(id="eol_scenario_bar"),
                    ], xs=8, sm=8, md=9, lg=9, xl=9, xxl=9
                ),
            ],
            justify='center',
            className='mb-4'
        ),
    ],
)


@callback(
    Output('eol_scenario_bar', 'figure'),
    [
        Input('scope_dropdown_eol_scenario', 'value'),
        Input('eol_scenario_checklist', 'value'),
    ]
)
def update_chart(scope, checklist_value):

    # update with actual logic
    percent_dict = {
        '1_regionally_specific': 10,
        '2_50%_recycle': 20,
        '3_100%_recycle': 30
    }
    new_df = pd.melt(
        df,
        id_vars=scope,
        value_vars='Global Warming Potential Total (kgCO2eq)',
        var_name='Impacts',
        value_name='Impact Amount'
    )
    new_df = new_df.groupby(scope).sum()
    new_df['Impacts'] = '0_default_eol'

    list_of_dfs = [new_df]
    for num in checklist_value:
        temp = new_df.copy()
        temp['Impacts'] = num
        temp['Impact Amount'] = \
            temp['Impact Amount'] * (1 - (percent_dict.get(num) / 100))
        list_of_dfs.append(temp)

    checklist_df = pd.concat(list_of_dfs)

    fig = px.bar(
        checklist_df,
        x='Impacts',
        y='Impact Amount',
        color=checklist_df.index,
    ).update_yaxes(
        title=f'Percent contribution by {scope}',
        tickformat=',.0f',
    ).update_xaxes(
        title='',
        categoryorder='category ascending'
    )

    fig.update_traces(width=.2 + .2 * len(checklist_value))
    if len(checklist_value) > 3:
        fig.update_traces(width=.8)

    return fig
