"""Results page of dashboard"""
import pandas as pd
import plotly.express as px
from dash import html, callback, Input, Output, State, register_page, no_update
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
                        ], xs=4, sm=4, md=4, lg=4, xl=4, xxl=4,
                        class_name='',
                        style={'max-height': '600px'}
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
                            )
                        ],
                        xs=8, sm=8, md=8, lg=8, xl=8, xxl=8,
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
        State('template_model_metadata', 'data')
    ]
)
def update_tm_name(location_dropdown_value, tm_metadata):
    tm_metadata_df = pd.DataFrame.from_dict(tm_metadata.get('tm_metadata'))
    if location_dropdown_value not in tm_metadata_df['location'].unique():
        return no_update
    tm_name = tm_metadata_df.loc[
        tm_metadata_df['location'] == location_dropdown_value,
        'template_model'
    ].item()

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
    unpacked_tm_name = tm_name.get('template_model_value')
    tm_row = tm_metadata_df[tm_metadata_df['template_model'] == unpacked_tm_name]

    building_use_type = tm_row['building_use_type'].item()
    project_area = tm_row['project_area'].item()
    building_height = tm_row['building_height'].item()
    location = tm_row['location'].item()
    stories_above_grade = tm_row['stories_above_grade'].item()
    stories_below_grade = tm_row['stories_below_grade'].item()
    bay_size = tm_row['bay_size'].item()
    str_vert_grav_sys = tm_row['str_vert_grav_sys'].item()
    str_horiz_grav_sys = tm_row['str_horiz_grav_sys'].item()
    str_lat_sys = tm_row['str_lat_sys'].item()
    cladding_type = tm_row['cladding_type'].item()
    roofing_type = tm_row['roofing_type'].item()
    wwr = tm_row['wwr'].item()

    criteria_text = f'''
        ### Architecture
        - **Location:** {location}
        - __Building Use Type:__ {building_use_type}
        - __Project Area:__ {project_area}
        - __Building Height:__ {building_height}
        - __Stories Above Grade:__ {stories_above_grade}
        - __Stories Below Grade:__ {stories_below_grade}
        - __Bay Size:__ {bay_size}

        ### Structure
        - __H. Gravity System:__ {str_horiz_grav_sys}
        - __V. Gravity System:__ {str_vert_grav_sys}
        - __Lateral System:__ {str_lat_sys}

        ### Enclosure
        - __Cladding Type:__ {cladding_type}
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
