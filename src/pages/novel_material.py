"""Results page of dashboard"""
import pandas as pd
import plotly.express as px
from dash import html, callback, Input, Output, State, register_page, no_update, dcc
import dash_bootstrap_components as dbc
import src.components.novel_material_components as nmc

register_page(__name__, path='/novel_material')


layout = html.Div(
    children=[
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(id='tm_card_info')
                        ], xs=2, sm=2, md=2, lg=2, xl=2, xxl=2,
                        class_name=''
                    ),
                    dbc.Col(
                        [
                            nmc.form
                        ], xs=6, sm=6, md=6, lg=6, xl=6, xxl=6,
                        class_name=''
                    ),
                    dbc.Col(
                        [
                            html.Div('hi')
                        ], xs=4, sm=4, md=4, lg=4, xl=4, xxl=4
                    ),
                ],
                justify='center',
                className='vh-100 pt-2'
            ),
            fluid=True,
            class_name='mw-100'
        ),
    ],
)


@callback(
    Output('tm_card_info', 'children'),
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

    card_info = [
        dbc.CardHeader(
            'Template Model Criteria',
            class_name='fw-bold'
        ),
        dbc.CardBody(
            dcc.Markdown(
                f'''
                ##### Architecture
                - __Location:__ {location}
                - __Building Use Type:__ {building_use_type}
                - __Project Area:__ {project_area}
                - __Building Height:__ {building_height}
                - __Stories Above Grade:__ {stories_above_grade}
                - __Stories Below Grade:__ {stories_below_grade}
                - __Bay Size:__ {bay_size}

                ##### Structure
                - __H. Gravity System:__ {str_horiz_grav_sys}
                - __V. Gravity System:__ {str_vert_grav_sys}
                - __Lateral System:__ {str_lat_sys}

                ##### Enclosure
                - __Cladding Type:__ {cladding_type}
                - __Roofing Type:__ {roofing_type}
                - __Window-to-wall Ratio:__ {wwr}
               '''
            )
        )
    ]
    return card_info


# @callback(
#     Output('tm_summary', 'figure'),
#     [
#         Input('template_model_name', 'data'),
#         State('template_model_impacts', 'data')
#     ]
# )
# def update_tm_summary_graph(tm_name, tm_impacts):
#     tm_impacts_df = pd.DataFrame.from_dict(tm_impacts.get('tm_impacts'))
#     unpacked_tm_name = tm_name.get('template_model_value')
#     df_to_graph = tm_impacts_df[tm_impacts_df['Revit model'] == unpacked_tm_name]

#     df_to_graph = df_to_graph.groupby('Revit category').sum()

#     fig = px.bar(
#         df_to_graph,
#         x='Global Warming Potential Total (kgCO2eq)',
#         color=df_to_graph.index,
#         # title=f'GWP Impacts of {unpacked_tm_name}',
#         height=600
#     ).update_yaxes(
#         title='',
#         tickformat=',.0f',
#     ).update_xaxes(
#         categoryorder='category ascending',
#         title=''
#     ).update_layout(
#         showlegend=False
#     )
#     return fig
