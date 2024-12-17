"""Results page of dashboard"""
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import src.utils.general as utils
from src.components.selection import create_dropdown
from src.components.results_data_work import create_all_impacts_df
import src.components.results_components as results

register_page(__name__, path='/results')

tabs = dbc.Container(
    [
        dcc.Tabs(
            [
                dcc.Tab(label="Scenario Explorer", id="tab-1"),
                dcc.Tab(label="Model Comparison", id="tab-2"),
            ],
            id="tab_collection",
            value="tab-1",
            className='fw-bold'
        ),
        dbc.Row(
            html.Div(id='tab-content'),
        )
    ],
    fluid=True
)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        tabs
                    ], xs=12, sm=12, md=12, lg=12, xl=12, xxl=12
                ),
                # dbc.Col(
                #     [
                #         dcc.Graph(id="stacked_bar"),
                #     ], xs=8, sm=8, md=9, lg=9, xl=9, xxl=9
                # ),
            ],
            justify='center',
            className='mb-4'
        ),
    ],
)


@callback(
    Output('tab-content', 'children'),
    Input('tab_collection', 'value')
)
def update_tabs(active_tab):
    print(active_tab)
    if active_tab == 'tab-1':
        return results.scenario_explorer_layout
    if active_tab == 'tab-2':
        return 'model comp time!'



# @callback(
#     Output('stacked_bar', 'figure'),
#     [
#         Input('scope_dropdown', 'value'),
#         Input('impact_dropdown', 'value'),
#         Input('impact_dropdown', 'options'),
#         Input('template_model_name', 'data')
#     ],
#     prevent_initial_callback=True
# )
# def update_chart(scope, impact_type, impact_options, template_model_name_dict):

#     for item in impact_options:
#         if item['value'] == impact_type:
#             impact_index = impact_options.index(item)

#     filtered_df_by_tm = df[df['Revit model'] == template_model_name_dict.get('template_model_value')]

#     if impact_type == 'All':

#         new_grouped_impacts = create_all_impacts_df(
#             df=filtered_df_by_tm,
#             scope=scope
#         )

#         fig = px.histogram(
#             new_grouped_impacts,
#             x='Impacts',
#             y='percentage',
#             color=scope,
#             title=f'Impacts for {template_model_name_dict.get("template_model_name")}'
#         ).update_yaxes(
#             title=f'Percent contribution by {scope}',
#             tickformat=".1%"
#         ).update_xaxes(
#             categoryorder='array',
#             categoryarray=[
#                 'GWP',
#                 'AP',
#                 'EP',
#                 'ODP',
#                 'SFP'
#             ],
#             title=''
#         )

#     else:
#         new_df = pd.melt(
#             filtered_df_by_tm,
#             id_vars=scope,
#             value_vars=impact_type,
#             var_name='Impacts',
#             value_name='Impact Amount'
#         )

#         fig = px.histogram(
#             new_df.sort_values(scope),
#             y=scope,
#             x='Impact Amount',
#             color=scope,
#             histfunc='sum',
#             title=f'Impacts for {template_model_name_dict.get("template_model_name")}'
#         )
#         fig.update_yaxes(
#             title=f'Impacts by {scope}',
#             categoryorder='category descending'
#         )
#         fig.update_xaxes(
#             title=f'{impact_options[impact_index]["value"]}',
#             tickformat=',.0f',
#         )
#         if impact_type == 'Ozone Depletion Potential Total (CFC-11eq)':
#             fig.update_xaxes(
#                 tickformat='.4f',
#             )

#     return fig
