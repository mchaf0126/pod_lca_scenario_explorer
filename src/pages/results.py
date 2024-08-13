from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import src.utils.general as utils
from src.components.dropdowns import create_dropdown

register_page(__name__, path='/results')

current_file_path = Path(__file__)
main_directory = current_file_path.parents[2]
data_directory = main_directory.joinpath('data/tally_commercial_includeBC.csv')

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
        Input('impact_dropdown', 'value')
    ]
)
def update_chart(scope, impact_type):

    new_df = pd.melt(
        df,
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
        histfunc='sum'
    )
    fig.update_yaxes(
        title=f'Impacts by {scope}',
        categoryorder='category descending'
    )

    fig.update_xaxes(
        title=f'{impact_type}'
    )

    return fig
