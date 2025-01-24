"""Results page of dashboard"""
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag
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
                            dbc.Row(
                                dbc.Container(
                                    [
                                        dbc.Row(
                                            dcc.Graph(id="mc_figure"),
                                        )
                                    ],
                                    class_name='mt-2 mx-3',
                                    fluid=True
                                )
                            ),
                            dbc.Row(
                                html.Div(
                                    id='mc_description',
                                    className='pt-2 px-4 mx-5'
                                )
                            ),
                            dbc.Row(
                                id='mc_default_table',
                                class_name='mx-5'
                            ),
                            dbc.Row(
                                id='mc_user_defined_table',
                                class_name='mx-5'
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
        Input('intentional_sourcing_impacts_mc', 'data'),
        Input('intentional_replacement_impacts_mc', 'data'),
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
    if intentional_sourcing_impacts is None:
        return px.bar()
    if intentional_replacement_impacts is None:
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
    else:
        repl_df = pd.DataFrame.from_dict(
            intentional_replacement_impacts.get(
                'mc_intentional_replacement_impacts'
            )
        )

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
    Output('user_defined_impacts', 'data'),
    [
        Input('transporation_scenario_radio', 'value'),
        Input('construction_scenario_radio', 'value'),
        Input('replacement_scenario_radio', 'value'),
        # Input('eol_scenario_radio', 'value'),
        State('current_tm_impacts', 'data'),
        State('current_pb_impacts', 'data'),
        Input('intentional_sourcing_impacts_mc', 'data'),
        Input('intentional_replacement_impacts_mc', 'data'),
    ]
)
def update_user_defined_impacts(trans_scenario: str,
                                constr_scenario: str,
                                repl_scenario: str,
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
    if current_tm_impacts is None:
        return px.bar()
    tm_impacts_df = pd.DataFrame.from_dict(current_tm_impacts.get('current_tm_impacts'))
    pb_impacts_df = pd.DataFrame.from_dict(
        current_pb_impacts.get(
            'current_pb_impacts'
        )
    )

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
    else:
        repl_df = pd.DataFrame.from_dict(
            intentional_replacement_impacts.get(
                'mc_intentional_replacement_impacts'
            )
        )

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

    if 'level_0' in user_selected_df_to_graph:
        user_selected_df_to_graph = user_selected_df_to_graph.drop(columns='level_0')

    return {'user_defined_impacts': user_selected_df_to_graph.reset_index().to_dict()}


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
def update_description_mc(trans_scenario: str,
                          constr_scenario: str,
                          repl_scenario: str,
                          op_scenario: str,
                          eol_scenario: str,):
    text = [
        dbc.Label(
            'User-defined Model with Scenarios',
            class_name='fs-5 fw-bold mt-2'
        ),
        dcc.Markdown(
            f'''
            The following scenarios have been selected:
            - Transportation: {trans_scenario}
            - Construction: {constr_scenario}
            - Replacement: {repl_scenario}
            - Operational Energy: {op_scenario}
            - End-of-life: {eol_scenario}
            ''',
            className='fw-light'
        )
    ]
    return text


@callback(
    Output('mc_default_table', 'children'),
    Input('current_tm_impacts', 'data')
)
def update_tm_table_mc(current_tm_impacts: dict):
    impacts_map = {
        'Global Warming Potential_fossil': 'GWP fossil',
        'Acidification Potential': 'AP',
        'Eutrophication Potential': 'EP',
        'Smog Formation Potential': 'SFP',
        'Ozone Depletion Potential': 'ODP',
        'Global Warming Potential_biogenic': 'GWP biogenic',
        'Global Warming Potential_luluc': 'GWP luluc',
        'Stored Biogenic Carbon': 'Stored Carbon'
    }
    table_label = dbc.Label(
        'Template Model Impacts',
        class_name='fs-5 fw-bold mt-2'
    )
    if current_tm_impacts is None:
        return None
    tm_impacts_df = pd.DataFrame.from_dict(current_tm_impacts.get('current_tm_impacts'))
    tm_impacts_df = tm_impacts_df.groupby(
        'life_cycle_stage'
    )[list(impacts_map.keys())].sum().reset_index()
    tm_impacts_df.loc[
        tm_impacts_df['life_cycle_stage'] == 'A5: Construction',
        'Stored Biogenic Carbon'
    ] = 0
    tm_impacts_df = tm_impacts_df.rename(columns={'life_cycle_stage': 'Life Cycle Stage'})
    tm_impacts_df = tm_impacts_df.rename(columns=impacts_map)
    # table = dbc.Table.from_dataframe(tm_impacts_df.T.reset_index(), striped=True)

    impact_col_width = 115
    table = dag.AgGrid(
        rowData=tm_impacts_df.to_dict("records"),
        defaultColDef={
            "wrapHeaderText": True,
            "autoHeaderHeight": True,
        },
        columnDefs=[
            {
                'field': 'Life Cycle Stage',
                'cellClass': 'fw-bold',
                'cellStyle': {
                    "wordBreak": "normal"
                },
                "wrapText": True,
                "resizable": True,
                "autoHeight": True,
                'width': 190,
                'pinned': 'left'
            },
            {
                'field': impacts_map.get('Global Warming Potential_fossil'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',

                'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right',
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Acidification Potential'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Eutrophication Potential'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.2f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Smog Formation Potential'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Ozone Depletion Potential'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.5f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Global Warming Potential_biogenic'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Global Warming Potential_luluc'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Stored Biogenic Carbon'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
        ],
        dashGridOptions={"domLayout": "autoHeight"},
        style={'width': '100%'},
    )

    final_table = html.Div(
        table,
        className='my-3'
    )
    return [table_label, final_table]


@callback(
    Output('mc_user_defined_table', 'children'),
    Input('user_defined_impacts', 'data')
)
def update_user_defined_table(user_defined_impacts: dict):
    impacts_map = {
        'Global Warming Potential_fossil': 'GWP fossil',
        'Acidification Potential': 'AP',
        'Eutrophication Potential': 'EP',
        'Smog Formation Potential': 'SFP',
        'Ozone Depletion Potential': 'ODP',
        'Global Warming Potential_biogenic': 'GWP biogenic',
        'Global Warming Potential_luluc': 'GWP luluc',
        'Stored Biogenic Carbon': 'Stored Carbon'
    }
    table_label = dbc.Label(
        'User-defined Impacts',
        class_name='fs-5 fw-bold mt-2'
    )
    if user_defined_impacts is None:
        return None
    tm_impacts_df = pd.DataFrame.from_dict(user_defined_impacts.get('user_defined_impacts'))
    tm_impacts_df = tm_impacts_df.groupby(
        'life_cycle_stage'
    )[list(impacts_map.keys())].sum().reset_index()
    tm_impacts_df.loc[
        tm_impacts_df['life_cycle_stage'] == 'A5: Construction',
        'Stored Biogenic Carbon'
    ] = 0
    tm_impacts_df = tm_impacts_df.rename(columns={'life_cycle_stage': 'Life Cycle Stage'})
    tm_impacts_df = tm_impacts_df.rename(columns=impacts_map)

    impact_col_width = 115
    table = dag.AgGrid(
        rowData=tm_impacts_df.to_dict("records"),
        defaultColDef={
            "wrapHeaderText": True,
            "autoHeaderHeight": True,
        },
        columnDefs=[
            {
                'field': 'Life Cycle Stage',
                'cellClass': 'fw-bold',
                'cellStyle': {
                    "wordBreak": "normal"
                },
                "wrapText": True,
                "resizable": True,
                "autoHeight": True,
                'width': 190,
                'pinned': 'left'
            },
            {
                'field': impacts_map.get('Global Warming Potential_fossil'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',

                'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right',
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Acidification Potential'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Eutrophication Potential'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.2f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Smog Formation Potential'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Ozone Depletion Potential'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.5f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Global Warming Potential_biogenic'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Global Warming Potential_luluc'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
            {
                'field': impacts_map.get('Stored Biogenic Carbon'),
                'type': 'rightAligned',
                'cellClass': 'fw-light',
                'cellDataType': 'number',
                'valueFormatter': {"function": "d3.format(',.0f')(params.value)"},
                'cellStyle': {
                    'textAlign': 'right'
                },
                'width': impact_col_width
            },
        ],
        dashGridOptions={"domLayout": "autoHeight"},
        style={'width': '100%'},
    )

    final_table = html.Div(
        table,
        className='my-3'
    )
    return [table_label, final_table]
