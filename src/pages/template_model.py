"""Results page of dashboard"""
import pandas as pd
import plotly.express as px
from dash import html, callback, Input, Output, State, register_page, dcc
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import src.components.template_model_components as tmc

register_page(__name__, path='/template_model')


layout = html.Div(
    children=[
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            tmc.sidebar
                        ], xs=4, sm=4, md=4, lg=4, xl=4, xxl=3,
                        class_name='',
                        style={'max-height': '1000px'}
                    ),
                    dbc.Col(
                        [
                            dbc.Row(
                                dbc.Label(
                                    id='tm_description',
                                    class_name='fs-5 fw-bold mt-3 text-center'
                                ),
                            ),
                            dbc.Row(
                                dbc.Spinner(
                                    tmc.figure,
                                    color='primary'
                                )
                            ),
                            dbc.Row(
                                dbc.Col(
                                    [
                                        tmc.tm_graph_dropdown
                                    ], xs=4, sm=4, md=4, lg=4, xl=4, xxl=3
                                ),
                                class_name='mx-5'
                            ),
                            dbc.Row(
                                tmc.display_data,
                                class_name='mx-5'
                            ),
                            dbc.Row(
                                id='tm_table',
                                class_name='mx-5'
                            )
                        ],
                        xs=8, sm=8, md=8, lg=8, xl=8, xxl=9,
                        class_name='',
                    ),
                ],
                justify='center',
                className=''
            ),
            fluid=True,
            class_name='mw-100'
        ),
    ],
)


@callback(
    [
        Output('location_dropdown', 'disabled'),
        Output('str_material_dropdown', 'disabled'),
        Output('cladding_type_dropdown', 'disabled'),
        Output('glazing_type_dropdown', 'disabled'),
        Output('roofing_type_dropdown', 'disabled'),
        Output('wwr_dropdown', 'disabled'),
    ],
    Input('building_use_type_dropdown', 'value'),
)
def update_dropdowns_for_sfh(building_use_dropdown: str):
    if building_use_dropdown == 'Single family home':
        return True, True, True, True, True, True

    return False, False, False, False, False, False,


@callback(
    Output('template_model_name', 'data'),
    [
        Input('location_dropdown', 'value'),
        Input('building_use_type_dropdown', 'value'),
        Input('str_material_dropdown', 'value'),
        Input('column_span_dropdown', 'value'),
        Input('cladding_type_dropdown', 'value'),
        Input('glazing_type_dropdown', 'value'),
        Input('roofing_type_dropdown', 'value'),
        Input('wwr_dropdown', 'value'),
        State('template_model_metadata', 'data')
    ]
)
def update_tm_name(location_dropdown_value: str,
                   building_use_dropdown_value: str,
                   str_material_dropdown_value: str,
                   column_span_dropdown_value: str,
                   cladding_dropdown_value: str,
                   glazing_dropdown_value: str,
                   roofing_dropdown_value: str,
                   wwr_dropdown_value: str,
                   tm_metadata: dict):
    tm_metadata_df = pd.DataFrame.from_dict(tm_metadata.get('tm_metadata'))

    if building_use_dropdown_value == 'Single family home':
        return {
            "template_model_name": 'STR4_ENCO11_ENCT3_ENCR2',
            'template_model_value': 'STR4_ENCO11_ENCT3_ENCR2'
        }

    selected_template_model = tm_metadata_df.loc[
        (
            (tm_metadata_df['location'] == location_dropdown_value)
            & (tm_metadata_df['building_use_type'] == building_use_dropdown_value)
            & (tm_metadata_df['structural_material'] == str_material_dropdown_value)
            & (tm_metadata_df['bay_size_description'] == column_span_dropdown_value)
            & (tm_metadata_df['cladding_type'] == cladding_dropdown_value)
            & (tm_metadata_df['glazing_type'] == glazing_dropdown_value)
            & (tm_metadata_df['roofing_type'] == roofing_dropdown_value)
            & (tm_metadata_df['wwr'] == wwr_dropdown_value)
        ),
        'template_model'
    ]
    if len(selected_template_model) == 1:
        tm_name = selected_template_model.item()
        return {
            "template_model_name": str(tm_name),
            'template_model_value': str(tm_name)
        }


@callback(
    Output('tm_description', 'children'),
    Input('building_use_type_dropdown', 'value')
)
def update_title(template_model_use_type):
    markdown_text = f'{template_model_use_type} Template Model'
    return markdown_text


@callback(
    Output('criteria_text', 'children'),
    [
        Input('template_model_name', 'data'),
        State('template_model_metadata', 'data')
    ]
)
def update_criteria_text(tm_name, tm_metadata):
    tm_metadata_df = pd.DataFrame.from_dict(tm_metadata.get('tm_metadata'))
    if tm_name is None:
        return '''
    ### The current selection is not a valid template model
    At the moment, only horizontal and vertical structural systems of the same material can be selected.
    This will be improved in future iterations.
    '''
    unpacked_tm_name = tm_name.get('template_model_value')
    tm_row = tm_metadata_df[tm_metadata_df['template_model'] == unpacked_tm_name]

    building_use_type = tm_row['building_use_type'].item()
    project_area = tm_row['project_area'].item()
    building_height = tm_row['building_height'].item()
    location = tm_row['location'].item()
    state = tm_row['state'].item()
    stories_above_grade = tm_row['stories_above_grade'].item()
    bay_size = tm_row['bay_size'].item()
    str_vert_grav_sys = tm_row['str_vert_grav_sys'].item()
    str_horiz_grav_sys = tm_row['str_horiz_grav_sys'].item()
    str_lat_sys = tm_row['str_lat_sys'].item()
    cladding_type = tm_row['cladding_type'].item()
    glazing_type = tm_row['glazing_type'].item()
    roofing_type = tm_row['roofing_type'].item()
    wwr = tm_row['wwr'].item()

    criteria_text = [
        dbc.Label(
            'Building Information',
            class_name='fs-5 fw-bold mt-2'
        ),
        dcc.Markdown(
            f'''
            The template model is located in {location}, {state}. The {project_area:,} square foot {building_use_type.lower()} building
            is {stories_above_grade} stories and measures at {building_height} feet tall.

            See below for a breakdown of the structure and envelope design criteria.
            ''',
            className='fw-light'
        ),
        dbc.Label(
            'Structure',
            class_name='fs-5 fw-bold mt-2'
        ),
        dcc.Markdown(
            f'''
            - __H. Gravity System:__ {str_horiz_grav_sys}
            - __V. Gravity System:__ {str_vert_grav_sys}
            - __Lateral System:__ {str_lat_sys}
            - __Bay Size:__ {bay_size}
            ''',
            className='fw-light'
        ),
        dbc.Label(
            'Enclosure',
            class_name='fs-5 fw-bold mt-2'
        ),
        dcc.Markdown(
            f'''
            - __Cladding Type:__ {cladding_type}
            - __Glazing Type:__ {glazing_type}
            - __Roofing Type:__ {roofing_type}
            - __Window-to-wall Ratio:__ {wwr}
            ''',
            className='fw-light'
        )
    ]
    return criteria_text


@callback(
    Output('current_tm_impacts', 'data'),
    [
        Input('template_model_name', 'data'),
        State('template_model_impacts', 'data')
    ]
)
def update_current_template_model_impacts(tm_name, tm_impacts):
    tm_impacts_df = pd.DataFrame.from_dict(tm_impacts.get('tm_impacts')).set_index('template_model')
    if tm_name is None:
        return None
    unpacked_tm_name = tm_name.get('template_model_value')
    current_tm_impacts = tm_impacts_df.loc[unpacked_tm_name].reset_index()
    return {
        "current_tm_impacts": current_tm_impacts.to_dict(),
    }


@callback(
    Output('current_pb_impacts', 'data'),
    [
        Input('template_model_name', 'data'),
        State('prebuilt_scenario_impacts', 'data')
    ]
)
def update_current_prebuilt_scenario_impacts(tm_name, pb_impacts):
    pb_impacts_df = pd.DataFrame.from_dict(pb_impacts.get('prebuilt_scenario_impacts')).set_index('template_model')
    if tm_name is None:
        return None
    unpacked_tm_name = tm_name.get('template_model_value')
    current_pb_impacts = pb_impacts_df.loc[unpacked_tm_name].reset_index()
    return {
        "current_pb_impacts": current_pb_impacts.to_dict(),
    }


@callback(
    Output('tm_summary', 'figure'),
    [
        Input('template_model_graph_dropdown', 'value'),
        Input('current_tm_impacts', 'data')
    ]
)
def update_tm_summary_graph(tm_dropdown: str, current_tm_impacts: dict):
    if current_tm_impacts is None:
        return px.bar()
    tm_impacts_df = pd.DataFrame.from_dict(current_tm_impacts.get('current_tm_impacts'))

    impacts = [
        'Global Warming Potential_fossil',
        'Acidification Potential',
        'Eutrophication Potential',
        'Smog Formation Potential',
        # 'Global Warming Potential_biogenic'
        # 'Ozone Depletion Potential'
    ]
    if tm_dropdown != 'life_cycle_stage':
        df_to_graph = tm_impacts_df.loc[tm_impacts_df['Assembly'] != 'Operational energy', :]

    df_to_graph = tm_impacts_df.melt(
        id_vars=['L3', 'Assembly', 'Component', 'life_cycle_stage'],
        value_vars=impacts
    )
    for impact in impacts:
        temp_sum = df_to_graph.loc[df_to_graph['variable'] == impact, 'value'].sum().item()
        df_to_graph.loc[df_to_graph['variable'] == impact, 'value'] /= temp_sum

    fig = px.histogram(
        df_to_graph.sort_values(by=tm_dropdown),
        x='variable',
        y='value',
        color=tm_dropdown,
        category_orders={'variable': [
            'Global Warming Potential_fossil',
            'Acidification Potential',
            'Eutrophication Potential',
            'Smog Formation Potential',
        ]}
        # title=f'GWP Impacts of {unpacked_tm_name}',
        # height=600
    ).update_yaxes(
        title='Percent Contribution of Categorization',
        tickformat='0%',
    ).update_xaxes(
        # categoryorder='category ascending',
        title=''
    ).update_layout(
        showlegend=True,
        legend_title=""
    )
    return fig


@callback(
    Output('tm_table', 'children'),
    Input('current_tm_impacts', 'data')
)
def update_tm_table(current_tm_impacts: dict):
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
        (tm_impacts_df['life_cycle_stage'] == 'A5: Construction')
        | (tm_impacts_df['life_cycle_stage'] == 'B2-B5: Replacement'),
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
