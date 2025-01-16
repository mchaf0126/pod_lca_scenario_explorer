"""Results page of dashboard"""
import pandas as pd
import plotly.express as px
from dash import html, callback, Input, Output, State, register_page
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
                                tmc.figure
                            ),
                            dbc.Row(
                                tmc.display_data,
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
    Output('template_model_name', 'data'),
    [
        Input('location_dropdown', 'value'),
        Input('building_use_type_dropdown', 'value'),
        Input('str_horiz_grav_sys_dropdown', 'value'),
        Input('str_vert_grav_sys_dropdown', 'value'),
        Input('str_lat_sys_dropdown', 'value'),
        Input('cladding_type_dropdown', 'value'),
        Input('glazing_type_dropdown', 'value'),
        Input('roofing_type_dropdown', 'value'),
        Input('wwr_dropdown', 'value'),
        State('template_model_metadata', 'data')
    ]
)
def update_tm_name(location_dropdown_value: str,
                   building_use_dropdown_value: str,
                   str_horiz_grav_sys_dropdown_value: str,
                   str_vert_grav_sys_dropdown_value: str,
                   str_lat_sys_dropdown_value: str,
                   cladding_dropdown_value: str,
                   glazing_dropdown_value: str,
                   roofing_dropdown_value: str,
                   wwr_dropdown_value: str,
                   tm_metadata: dict):
    tm_metadata_df = pd.DataFrame.from_dict(tm_metadata.get('tm_metadata'))
    selected_template_model = tm_metadata_df.loc[
        (
            (tm_metadata_df['location'] == location_dropdown_value)
            & (tm_metadata_df['building_use_type'] == building_use_dropdown_value)
            & (tm_metadata_df['str_vert_grav_sys'] == str_vert_grav_sys_dropdown_value)
            & (tm_metadata_df['str_horiz_grav_sys'] == str_horiz_grav_sys_dropdown_value)
            & (tm_metadata_df['str_lat_sys'] == str_lat_sys_dropdown_value)
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
    print(unpacked_tm_name)
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

    criteria_text = f'''
        ### Building Information
        The template model is located in {location}, {state}. The {project_area:,} square foot {building_use_type.lower()} building
        is {stories_above_grade} stories and measures at {building_height} feet tall.

        See below for a breakdown of the structure and envelope design criteria.

        ### Structure
        - __H. Gravity System:__ {str_horiz_grav_sys}
        - __V. Gravity System:__ {str_vert_grav_sys}
        - __Lateral System:__ {str_lat_sys}
        - __Bay Size:__ {bay_size}

        ### Enclosure
        - __Cladding Type:__ {cladding_type}
        - __Glazing Type:__ {glazing_type}
        - __Roofing Type:__ {roofing_type}
        - __Window-to-wall Ratio:__ {wwr}
    '''
    return criteria_text


@callback(
    Output('tm_summary', 'figure'),
    [
        Input('template_model_name', 'data'),
        State('template_model_impacts', 'data')
    ]
)
def update_tm_summary_graph(tm_name: dict, tm_impacts: dict):
    tm_impacts_df = pd.DataFrame.from_dict(tm_impacts.get('tm_impacts'))
    if tm_name is None:
        return px.bar()
    unpacked_tm_name = tm_name.get('template_model_value')
    df_to_graph = tm_impacts_df[tm_impacts_df['Revit model'] == unpacked_tm_name]

    df_to_graph = df_to_graph.groupby('Revit category').sum()

    fig = px.bar(
        df_to_graph,
        y='Global Warming Potential Total (kgCO2eq)',
        color=df_to_graph.index,
        # title=f'GWP Impacts of {unpacked_tm_name}',
        # height=600
    ).update_yaxes(
        title='',
        tickformat=',.0f',
    ).update_xaxes(
        categoryorder='category ascending',
        title=''
    ).update_layout(
        showlegend=False
    )
    return fig
