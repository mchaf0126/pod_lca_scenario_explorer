"""Results page of dashboard"""
from pathlib import Path
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import src.utils.general as utils
from src.components.selection import create_dropdown

register_page(__name__, path='/template_model')

current_file_path = Path(__file__)
main_directory = current_file_path.parents[2]

config_path = main_directory.joinpath('src/components/config.yml')

config = utils.read_yaml(config_path)
assert config is not None, 'The config dictionary could not be set'

tm_dropdown_yaml = config.get('tm_dropdown')
assert tm_dropdown_yaml is not None, 'The config for tm dropdown could not be set'

tm_dropdown = create_dropdown(
    label=tm_dropdown_yaml['label'],
    dropdown_list=tm_dropdown_yaml['dropdown_list'],
    first_item=tm_dropdown_yaml['first_item'],
    dropdown_id=tm_dropdown_yaml['dropdown_id']
)

card_child = dbc.CardBody(
    [
        dbc.Label('Template Model Selector', class_name='fs-5 fw-bold my-0'),
        html.Hr(),
        tm_dropdown,
    ],
    class_name='pb-0'
)

tm_controls = dbc.Card(
    [
        card_child,
    ],
    id='dropdown_card'
)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        tm_controls
                    ], xs=4, sm=4, md=3, lg=3, xl=3, xxl=3
                ),
                dbc.Col(
                    [
                        html.Img(id='tm_image'),
                        dcc.Markdown(id='tm_description')
                    ], xs=8, sm=8, md=9, lg=9, xl=9, xxl=9
                ),
            ],
            justify='center',
            className='mb-4'
        ),
    ],
)


@callback(
    Output('template_model_name', 'data'),
    [
        Input(tm_dropdown_yaml['dropdown_id'], 'options'),
        Input(tm_dropdown_yaml['dropdown_id'], 'value')
    ]
)
def update_tm_name(template_model_options, dropdown_value):
    for item in template_model_options:
        if item['value'] == dropdown_value:
            template_model_index = template_model_options.index(item)

    template_model_name = template_model_options[template_model_index]['label']
    return {
        "template_model_name": template_model_name,
        'template_model_value': dropdown_value
    }


@callback(
    [Output('tm_image', 'src'),
     Output('tm_description', 'children')],
    Input('template_model_name', 'data')
)
def update_image(template_model_name_dict):
    markdown_text = f'### This is {template_model_name_dict.get("template_model_name")}'
    return f'assets/tm_images/{template_model_name_dict.get("template_model_value")}.png', markdown_text
