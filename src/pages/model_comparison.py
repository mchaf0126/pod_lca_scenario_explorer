"""Results page of dashboard"""
import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output, register_page, State
import dash_bootstrap_components as dbc
import src.components.model_comp_components as mc

register_page(__name__, path='/model_comparison')


layout = html.Div(
    children=[
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            mc.model_comp_sidebar
                        ], xs=4, sm=4, md=4, lg=4, xl=4, xxl=3,
                        class_name='',
                        style={'max-height': '1200px'}
                    ),
                    dbc.Col(
                        [
                            dbc.Container(
                                [
                                    dbc.Row(
                                        dcc.Graph(id="mc_figure"),
                                        class_name='mt-2',
                                    ),
                                    dbc.Row(
                                        html.Div(
                                            id='mc_description',
                                            className='pt-2'
                                        )
                                    ),
                                ],
                                fluid=True,
                                class_name='m-3'
                            )
                        ], xs=8, sm=8, md=8, lg=8, xl=8, xxl=9,
                    ),
                ],
                # justify='center',
                className=''
            ),
            fluid=True,
            class_name='mw-100',
        ),
    ],
)


@callback(
    Output('mc_figure', 'figure'),
    [
        Input('impact_dropdown_model_comp', 'value'),
        Input('scope_dropdown_model_comp', 'value'),
        Input('transporation_scenario_radio', 'value'),
        # Input('construction_scenario_radio', 'value'),
        Input('replacement_scenario_radio', 'value'),
        Input('eol_scenario_radio', 'value'),
        State('template_model_name', 'data'),
        State('template_model_impacts', 'data'),
        State('prebuilt_scenario_impacts', 'data'),
    ]
)
def update_se_figure(impact: str,
                     scope: str,
                     trans_scenario: str,
                     # constr_scenario: str,
                     repl_scenario: str,
                     eol_scenario: str,
                     template_model_name: dict,
                     template_model_impacts: dict,
                     prebuilt_scenario_impacts: dict):

    lcs_map = {
        '[A4] Transportation': trans_scenario,
        # '[A5] Construction': constr_scenario,
        '[B2-B5] Maintenance and Replacement': repl_scenario,
        '[C2-C4] End of Life': eol_scenario
    }
    tm_impacts_df = pd.DataFrame.from_dict(template_model_impacts.get('tm_impacts'))
    pb_impacts_df = pd.DataFrame.from_dict(
        prebuilt_scenario_impacts.get('prebuilt_scenario_impacts')
    )
    unpacked_tm_name = template_model_name.get('template_model_value')
    tm_df_to_graph = tm_impacts_df[
        (tm_impacts_df['Revit model'] == unpacked_tm_name)

    ].copy()
    tm_df_to_graph.loc[:, 'model_comp'] = 'Default'

    user_selected_df_to_concat = []
    user_selected_df_to_concat.append(tm_df_to_graph[tm_df_to_graph['Life Cycle Stage'] == '[A1-A3] Product'])
    user_selected_df_to_concat.append(tm_df_to_graph[tm_df_to_graph['Life Cycle Stage'] == '[D] Module D'])
    for lcs, selected_scenario in lcs_map.items():
        if selected_scenario == 'default':
            temp_df = tm_df_to_graph[tm_df_to_graph['Life Cycle Stage'] == lcs]
            user_selected_df_to_concat.append(temp_df)
        else:
            temp_df = pb_impacts_df[
                (
                    (pb_impacts_df['Revit model'] == unpacked_tm_name)
                    & (pb_impacts_df['Life Cycle Stage'] == lcs)
                    & (pb_impacts_df['scenario'] == selected_scenario)
                )
            ]
            user_selected_df_to_concat.append(temp_df)

    user_selected_df_to_graph = pd.concat(user_selected_df_to_concat)
    user_selected_df_to_graph.loc[:, 'model_comp'] = 'User selected custom scenarios'

    combined_df_to_graph = pd.concat([tm_df_to_graph, user_selected_df_to_graph])
    combined_df_to_graph = combined_df_to_graph.sort_values('model_comp')

    fig = px.histogram(
        combined_df_to_graph,
        x='model_comp',
        y=impact,
        color=scope,
        # title=f'GWP Impacts of {unpacked_tm_name}',
    ).update_yaxes(
        title='',
        tickformat=',.0f',
    ).update_xaxes(
        title='',
    ).update_layout(
        # showlegend=False
    )
    return fig


@callback(
    Output('mc_description', 'children'),
    [
        Input('transporation_scenario_radio', 'value'),
        Input('construction_scenario_radio', 'value'),
        Input('replacement_scenario_radio', 'value'),
        Input('eol_scenario_radio', 'value'),
    ]
)
def update_description(trans_scenario: str,
                       constr_scenario: str,
                       repl_scenario: str,
                       eol_scenario: str,):
    text = dcc.Markdown(
        f'''
        ### User selected custom scenarios
        The following scenarios have been selected:
        - Transportation: {trans_scenario}
        - Construction: {constr_scenario}
        - Replacement: {repl_scenario}
        - End-of-life: {eol_scenario}
        ''',
        className='fw-light'
    )
    return text
