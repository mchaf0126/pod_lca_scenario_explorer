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
                        style={'max-height': '1000px'}
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
                                            className='pt-2 mx-5'
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
        Input('construction_scenario_radio', 'value'),
        Input('replacement_scenario_radio', 'value'),
        # Input('eol_scenario_radio', 'value'),
        State('current_tm_impacts', 'data'),
        State('current_pb_impacts', 'data'),
        Input('intentional_sourcing_impacts', 'data'),
        Input('intentional_replacement_impacts', 'data'),
    ]
)
def update_mc_figure(impact: str,
                     scope: str,
                     trans_scenario: str,
                     constr_scenario: str,
                     repl_scenario: str,
                     #  eol_scenario: str,
                     current_tm_impacts: dict,
                     current_pb_impacts: dict,
                     intentional_sourcing_impacts: dict,
                     intentional_replacement_impacts: dict,
                     ):
    lcs_map = {
        'Product': 'A1-A3: Product',
        'Transportation': 'A4: Transportation',
        'Construction': 'A5: Construction',
        'Replacement': 'B2-B5: Replacement',
        'Operational Energy': 'B6: Operational Energy',
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
    if current_tm_impacts is None:
        return px.bar()
    tm_impacts_df = pd.DataFrame.from_dict(current_tm_impacts.get('current_tm_impacts'))
    pb_impacts_df = pd.DataFrame.from_dict(
        current_pb_impacts.get(
            'current_pb_impacts'
        )
    )

    # default comparison df
    tm_df_to_graph = tm_impacts_df.assign(model_comp='Default Scenarios')

    # product
    product_df = tm_impacts_df.loc[tm_impacts_df['life_cycle_stage'] == lcs_map.get('Product'), :]

    # transportation
    if trans_scenario == 'North American Average (default)':
        trans_df = tm_impacts_df.loc[tm_impacts_df['life_cycle_stage'] == lcs_map.get('Transportation'), :]
    elif trans_scenario == 'Regionally-Specific Distances':
        trans_df = pb_impacts_df.loc[pb_impacts_df['scenario'] == 'Regionally-Specific Distances', :]
    else:
        trans_df = pd.DataFrame.from_dict(
            intentional_sourcing_impacts.get(
                'mc_intentional_sourcing_impacts'
            )
        )

    # construction
    if constr_scenario == 'North American Average (default)':
        constr_df = tm_impacts_df.loc[
            tm_impacts_df['life_cycle_stage'] == lcs_map.get('Construction'),
            :
        ]
    else:
        constr_df = pb_impacts_df.loc[
            pb_impacts_df['scenario'] == 'Enhanced Waste Management',
            :
        ]

    # replacement
    if repl_scenario == 'ASHRAE 240P Replacement Rates (default)':
        repl_df = tm_impacts_df.loc[
            tm_impacts_df['life_cycle_stage'] == lcs_map.get('Replacement'),
            :
        ]
    # else:
    #     repl_df = pd.DataFrame.from_dict(
    #         intentional_replacement_impacts.get(
    #             'mc_intentional_replacement_impacts'
    #         )
    #     )

    # operational energy
    op_df = tm_impacts_df.loc[
        tm_impacts_df['life_cycle_stage'] == lcs_map.get('Operational Energy'),
        :
    ]

    # end-of-life
    eol_df = tm_impacts_df.loc[
        tm_impacts_df['life_cycle_stage'] == lcs_map.get('End-of-life'),
        :
    ]

    # user_selected_df_to_concat = []
    # user_selected_df_to_concat.append(tm_df_to_graph[tm_df_to_graph['Life Cycle Stage'] == '[A1-A3] Product'])
    # for lcs, selected_scenario in lcs_map.items():
    #     if selected_scenario == 'default':
    #         temp_df = tm_df_to_graph[tm_df_to_graph['Life Cycle Stage'] == lcs]
    #         user_selected_df_to_concat.append(temp_df)
    #     else:
    #         temp_df = pb_impacts_df[
    #             (
    #                 (pb_impacts_df['Revit model'] == unpacked_tm_name)
    #                 & (pb_impacts_df['Life Cycle Stage'] == lcs)
    #                 & (pb_impacts_df['scenario'] == selected_scenario)
    #             )
    #         ]
    #         user_selected_df_to_concat.append(temp_df)

    # user_selected_df_to_graph = pd.concat(user_selected_df_to_concat)
    # user_selected_df_to_graph.loc[:, 'model_comp'] = 'User selected custom scenarios'

    user_selected_df_to_graph = pd.concat(
        [
            product_df,
            trans_df,
            constr_df,
            repl_df,
            op_df,
            eol_df
        ]
    )
    user_selected_df_to_graph = user_selected_df_to_graph.assign(model_comp='User-defined model with scenarios')

    combined_df_to_graph = pd.concat(
        [
            tm_df_to_graph,
            user_selected_df_to_graph
        ]
    )
    # combined_df_to_graph = combined_df_to_graph.sort_values('model_comp')

    fig = px.histogram(
        combined_df_to_graph.sort_values(by=scope),
        x='model_comp',
        y=impact,
        color=scope,
        category_orders={'model_comp': ['Default Scenarios', 'User-defined model with scenarios']}
        # title=f'GWP Impacts of {unpacked_tm_name}',
    ).update_yaxes(
        title=f'{impact} ({units_map.get(impact)})',
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
        Input('energy_use_scenario_radio', 'value'),
        Input('eol_scenario_radio', 'value'),
    ]
)
def update_description(trans_scenario: str,
                       constr_scenario: str,
                       repl_scenario: str,
                       op_scenario: str,
                       eol_scenario: str,):
    text = dcc.Markdown(
        f'''
        ### User selected custom scenarios
        The following scenarios have been selected:
        - Transportation: {trans_scenario}
        - Construction: {constr_scenario}
        - Replacement: {repl_scenario}
        - Operational Energy: {op_scenario}
        - End-of-life: {eol_scenario}
        ''',
        className='fw-light'
    )
    return text
