"""Results page of dashboard"""
import pandas as pd
from dash import html, dcc, callback, Input, Output, State, register_page, no_update
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
                        ], xs=2, sm=2, md=2, lg=2, xl=2, xxl=2,
                        class_name=''
                    ),
                    dbc.Col(
                        [
                            tmc.display_data
                        ], xs=6, sm=6, md=6, lg=6, xl=6, xxl=6,
                        class_name=''
                    ),
                    dbc.Col(
                        [
                            dcc.Graph(id="tm_summary"),
                        ], xs=4, sm=4, md=4, lg=4, xl=4, xxl=4
                    ),
                ],
                justify='center',
                className='vh-100'
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
    [
        Output('tm_image', 'src'),
        Output('tm_description', 'children')
    ],
    Input('template_model_name', 'data')
)
def update_image(template_model_name_dict):
    markdown_text = f'This is {template_model_name_dict.get("template_model_name")}'
    return f'assets/tm_images/{template_model_name_dict.get("template_model_value")}.png', markdown_text


@callback(
    [  
        Output('arch_criteria_text', 'children'),
        Output('str_criteria_text', 'children'),
        Output('enc_criteria_text', 'children'),
    ],
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

    arch_text = f'''
        - __Location:__ {location}
        - __Building Use Type:__ {building_use_type}
        - __Project Area:__ {project_area}
        - __Building Height:__ {building_height}
        - __Stories above grade:__ {stories_above_grade}
        - __Stories Below Grade:__ {stories_below_grade}
        - __Bay Size:__ {bay_size}
    '''
    str_text = f'''
        - __H. Gravity System:__ {str_horiz_grav_sys}
        - __V. Gravity System:__ {str_vert_grav_sys}
        - __Lateral System:__ {str_lat_sys}
    '''
    enc_text = f'''
        - __Cladding Type:__ {cladding_type}
        - __Roofing Type:__ {roofing_type}
        - __Window-to-wall Ratio:__ {wwr}
    '''
    return arch_text, str_text, enc_text
