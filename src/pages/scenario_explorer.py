"""Results page of dashboard"""
from dash import html, dcc, callback, Input, Output, register_page, State, ALL
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import src.components.scenario_explorer_components as sec
from src.components.transportation_components import transportation_scenarios
from src.components.construction_components import construction_scenarios
from src.components.replacement_components import replacement_scenarios
from src.components.eol_components import eol_scenarios
from src.components.descriptions import description_map

register_page(__name__, path='/scenario_explorer')

layout = html.Div(
    children=[
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            sec.se_sidebar,
                        ], xs=4, sm=4, md=4, lg=4, xl=4, xxl=3,
                        class_name='',
                        style={'max-height': '1000px'}
                    ),
                    dbc.Col(
                        [
                            dbc.Container(
                                [
                                    dbc.Row(
                                        dbc.Spinner(
                                            children=[dcc.Graph(id="se_figure")],
                                            color='primary'
                                        )
                                    ),
                                    dbc.Row(
                                        id='se_description',
                                        className='pt-2 mx-5'
                                    )
                                ],
                                class_name='mt-2',
                                fluid=True
                            )
                        ], xs=8, sm=8, md=8, lg=8, xl=8, xxl=9,
                        class_name=''
                    ),
                ],
                # justify='center',
                className=''
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
def update_scenario(life_cycle_stage):
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


@callback(
    Output('se_figure', 'figure'),
    [
        Input('life_cycle_stage_dropdown', 'value'),
        Input('impact_dropdown', 'value'),
        Input('scope_dropdown', 'value'),
        Input({'type': 'prebuilt_scenario', 'id': ALL}, 'value'),
        Input({'type': 'custom_checklist', 'id': ALL}, 'value'),
        State('current_tm_impacts', 'data'),
        Input('intentional_sourcing_impacts', 'data'),
        Input('intentional_replacement_impacts', 'data'),
        State('current_pb_impacts', 'data'),
    ]
)
def update_se_figure(life_cycle_stage: str,
                     impact: str,
                     scope: str,
                     prebuilt_scenario_checklist: list,
                     custom_trans_checklist: list,
                     current_tm_impacts: dict,
                     intentional_sourcing_impacts: dict,
                     intentional_replacement_impacts: dict,
                     current_pb_impacts: dict
                     ):
    lcs_map = {
        'Transportation': 'A4: Transportation',
        'Construction': 'A5: Construction',
        'Replacement': 'B2-B5: Replacement',
        'op': 'B6: Operational Energy',
        'End-of-life': 'C2-C4: End-of-life'
    }
    units_map = {
        'Acidification Potential': 'kgSO2e',
        'Eutrophication Potential': 'kgNe',
        'Global Warming Potential_fossil': 'kgCO2e',
        'Global Warming Potential_biogenic': 'kgCO2e',
        'Ozone Depletion Potential': 'CFC-11e',
        'Smog Formation Potential': 'kgO3e'
    }
    custom_trans_checklist = sum(custom_trans_checklist, [])
    prebuilt_scenario_checklist = sum(prebuilt_scenario_checklist, [])

    if current_tm_impacts is None:
        return px.bar()
    tm_impacts_df = pd.DataFrame.from_dict(current_tm_impacts.get('current_tm_impacts'))
    pb_impacts_df = pd.DataFrame.from_dict(
        current_pb_impacts.get(
            'current_pb_impacts'
        )
    )

    tm_df_to_graph = tm_impacts_df[
        (tm_impacts_df['life_cycle_stage'] == lcs_map.get(life_cycle_stage))
    ].copy()
    tm_df_to_graph.loc[:, 'scenario'] = 'Default Scenario'

    pb_df_to_graph = pb_impacts_df[
        (pb_impacts_df['life_cycle_stage'] == lcs_map.get(life_cycle_stage))
        & (pb_impacts_df['scenario'].isin(prebuilt_scenario_checklist))
    ]

    if life_cycle_stage == 'Transportation':
        if "Intentional Sourcing" not in custom_trans_checklist:
            combined_df_to_graph = pd.concat([tm_df_to_graph, pb_df_to_graph])
        else:
            custom_impacts_df = pd.DataFrame.from_dict(
                intentional_sourcing_impacts.get(
                    'se_intentional_sourcing_impacts'
                )
            )
            custom_impacts_df.loc[:, 'scenario'] = 'Intentional Sourcing'
            combined_df_to_graph = pd.concat(
                [
                    tm_df_to_graph,
                    pb_df_to_graph,
                    custom_impacts_df
                ]
            )
    elif life_cycle_stage == 'Replacement':
        if "Intentional Replacement" not in custom_trans_checklist:
            combined_df_to_graph = pd.concat([tm_df_to_graph, pb_df_to_graph])
        else:
            custom_impacts_df = pd.DataFrame.from_dict(
                intentional_replacement_impacts.get(
                    'se_intentional_replacement_impacts'
                )
            )
            custom_impacts_df.loc[:, 'scenario'] = 'Intentional Replacement'
            combined_df_to_graph = pd.concat(
                [
                    tm_df_to_graph,
                    pb_df_to_graph,
                    custom_impacts_df
                ]
            )
    else:
        combined_df_to_graph = pd.concat([tm_df_to_graph, pb_df_to_graph])

    fig = px.histogram(
        combined_df_to_graph.sort_values(by=scope),
        x='scenario',
        y=impact,
        color=scope,
        category_orders={'scenario': sec.category_orders.get(life_cycle_stage)}
        # title=f'GWP Impacts of {unpacked_tm_name}',
    ).update_yaxes(
        title=f'{impact} ({units_map.get(impact)})',
        tickformat=',.0f',
    ).update_xaxes(
        title='',
    ).update_layout(
        # showlegend=False
        title=''
    )
    return fig


@callback(
    Output('se_description', 'children'),
    Input('life_cycle_stage_dropdown', 'value'),
)
def update_description(lcs):
    title = [
        dbc.Label(
            'Descriptions',
            class_name='fs-5 fw-bold my-2'
        ),
        dcc.Markdown(
            '''
            See below for a description of the different scenarios that have been selected.
            ''',
            className='fw-light'
        )
    ]
    return title + description_map.get(lcs)
