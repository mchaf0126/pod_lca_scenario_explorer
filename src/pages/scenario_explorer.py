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
from src.components.descriptions import description_map, description_list

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
                                        dcc.Graph(id="se_figure"),
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
        Input({'type': 'custom_checklist', 'id': ALL}, 'value'),
        Input('template_model_name', 'data'),
        State('template_model_impacts', 'data'),
        Input('intentional_sourcing_impacts', 'data')
        # State('prebuilt_scenario_impacts', 'data'),
    ]
)
def update_se_figure(life_cycle_stage: str,
                     impact: str,
                     scope: str,
                     # checklist: list,
                     custom_trans_checklist: list,
                     template_model_name: dict,
                     template_model_impacts: dict,
                     intentional_sourcing_impacts: dict,
                     # prebuilt_scenario_impacts: dict
                     ):
    lcs_map = {
        'Transportation': 'Transportation: A4',
        'Construction': 'Construction: A5',
        'Replacement': 'Replacement: B2-B5',
        'End-of-life': 'End-of-life: C2-C4'
    }
    units_map = {
        'Acidification Potential': 'kgSO2e',
        'Eutrophication Potential': 'kgNe',
        'Global Warming Potential_fossil': 'kgCO2e',
        'Ozone Depletion Potential': 'CFC-11e',
        'Smog Formation Potential': 'kgO3e'
    }
    tm_impacts_df = pd.DataFrame.from_dict(template_model_impacts.get('tm_impacts'))
    unpacked_tm_name = template_model_name.get('template_model_value')
    tm_df_to_graph = tm_impacts_df[
        (tm_impacts_df['template_model'] == unpacked_tm_name)
        & (tm_impacts_df['life_cycle_stage'] == lcs_map.get(life_cycle_stage))
    ].copy()
    tm_df_to_graph.loc[:, 'scenario'] = 'Default scenario'

    if (life_cycle_stage == 'Transportation'):
        if custom_trans_checklist == [[]]:
            # pb_impacts_df = pd.DataFrame.from_dict(
            #     prebuilt_scenario_impacts.get('prebuilt_scenario_impacts')
            # )
            combined_df_to_graph = tm_df_to_graph
        else:
            custom_impacts_df = pd.DataFrame.from_dict(intentional_sourcing_impacts.get('intentional_sourcing_impacts'))
            custom_impacts_df.loc[:, 'scenario'] = 'Intentional Sourcing'
            custom_impacts_df.to_csv('testtrans.csv')
            combined_df_to_graph = pd.concat(
                [
                    tm_df_to_graph,
                    custom_impacts_df
                ]
            )

    # pb_df_to_graph = pb_impacts_df[
    #     (pb_impacts_df['Revit model'] == unpacked_tm_name)
    #     & (pb_impacts_df['Life Cycle Stage'] == lcs_map.get(life_cycle_stage))
    #     & (pb_impacts_df['scenario'].isin(sum(checklist, [])))
    # ]

    # categories = sec.category_orders.get(life_cycle_stage)

    # combined_df_to_graph = pd.concat(
    #     [
    #         tm_df_to_graph,
    #         # pb_df_to_graph
    #     ]
    # )
    # combined_df_to_graph['scenario'] = pd.Categorical(
    #     combined_df_to_graph['scenario'],
    #     ordered=True,
    #     categories=categories
    # )
    # combined_df_to_graph = combined_df_to_graph.sort_values('scenario')

    fig = px.histogram(
        combined_df_to_graph,
        x='scenario',
        y=impact,
        color=scope,
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
    [
        Input({'type': 'prebuilt_scenario', 'id': ALL}, 'value'),
        Input({"type": "custom_checklist", "id": 'transportation_custom_checklist'}, 'value'),
    ]
)
def update_description(checklist, custom_checklist):
    flattened_checklist = sum(checklist, [])
    final_checklist = flattened_checklist + custom_checklist
    sorted_list = sorted(final_checklist, key=description_list.index)
    title = [
        dcc.Markdown(
            '''
            ### Descriptions
            See below for a description of the different scenarios that have been selected.
            ''',
            className='fw-light'
        )
    ]
    return title + [description_map.get(value) for value in sorted_list]
