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
                        ], xs=3, sm=3, md=3, lg=3, xl=3, xxl=3,
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
                        ], xs=3, sm=3, md=3, lg=3, xl=3, xxl=3
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
    if location_dropdown_value not in tm_metadata_df['city'].unique():
        return no_update
    tm_name = tm_metadata_df.loc[
        tm_metadata_df['city'] == location_dropdown_value,
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
    Output('arch_criteria_text', 'children'),
    [
        Input('location_dropdown', 'value'),
        Input('building_use_type_dropdown', 'value')
    ]
)
def update_arch_criteria_text(location, building_use_type):
    return f'''
        __Location:__ {location}
        __Building Use Type:__ {building_use_type}
        '''
