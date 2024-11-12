"""Results page of dashboard"""
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import src.utils.general as utils
from src.components.selection import create_dropdown
from src.components.results_data_work import create_all_impacts_df

register_page(__name__, path='/results')


current_file_path = Path(__file__)
main_directory = current_file_path.parents[2]
data_directory = main_directory.joinpath('data/frontend/combined_impacts.csv')

df = pd.read_csv(data_directory, index_col=False)

config_path = main_directory.joinpath('src/components/config.yml')

config = utils.read_yaml(config_path)
assert config is not None, 'The config dictionary could not be set'

scope_dropdown_yaml = config.get('scope_dropdown')
assert scope_dropdown_yaml is not None, 'The config for cat. dropdowns could not be set'

impact_dropdown_yaml = config.get('impact_dropdown')
assert impact_dropdown_yaml is not None, 'The config for impact dropdowns could not be set'

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
                        dcc.Graph(id="stacked_bar"),
                    ], xs=8, sm=8, md=9, lg=9, xl=9, xxl=9
                ),
            ],
            justify='center',
            className='mb-4'
        ),
    ],
)


@callback(
    Output('stacked_bar', 'figure'),
    [
        Input('scope_dropdown', 'value'),
        Input('impact_dropdown', 'value'),
        Input('impact_dropdown', 'options'),
        Input('template_model_name', 'data')
    ],
    prevent_initial_callback=True
)
def update_chart(scope, impact_type, impact_options, template_model_name_dict):

    for item in impact_options:
        if item['value'] == impact_type:
            impact_index = impact_options.index(item)

    filtered_df_by_tm = df[df['Revit model'] == template_model_name_dict.get('template_model_value')]

    if impact_type == 'All':

        new_grouped_impacts = create_all_impacts_df(
            df=filtered_df_by_tm,
            scope=scope
        )

        fig = px.histogram(
            new_grouped_impacts,
            x='Impacts',
            y='percentage',
            color=scope,
            title=f'Impacts for {template_model_name_dict.get("template_model_name")}'
        ).update_yaxes(
            title=f'Percent contribution by {scope}',
            tickformat=".1%"
        ).update_xaxes(
            categoryorder='array',
            categoryarray=[
                'GWP',
                'AP',
                'EP',
                'ODP',
                'SFP'
            ],
            title=''
        )

    else:
        new_df = pd.melt(
            filtered_df_by_tm,
            id_vars=scope,
            value_vars=impact_type,
            var_name='Impacts',
            value_name='Impact Amount'
        )

        fig = px.histogram(
            new_df.sort_values(scope),
            y=scope,
            x='Impact Amount',
            color=scope,
            histfunc='sum',
            title=f'Impacts for {template_model_name_dict.get("template_model_name")}'
        )
        fig.update_yaxes(
            title=f'Impacts by {scope}',
            categoryorder='category descending'
        )
        fig.update_xaxes(
            title=f'{impact_options[impact_index]["value"]}',
            tickformat=',.0f',
        )
        if impact_type == 'Ozone Depletion Potential Total (CFC-11eq)':
            fig.update_xaxes(
                tickformat='.4f',
            )

    return fig
