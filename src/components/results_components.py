from pathlib import Path
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import src.utils.general as utils
from src.components.selection import create_dropdown
import src.components.a4_components as transportation

current_file_path = Path(__file__)
main_directory = current_file_path.parents[2]

config_path = main_directory.joinpath('src/components/config.yml')

config = utils.read_yaml(config_path)
assert config is not None, 'The config dictionary could not be set'

life_cycle_stage_dropdown_yaml = config.get('life_cycle_stage_dropdown')
assert life_cycle_stage_dropdown_yaml is not None, 'The config for lcs could not be set'

scope_dropdown_yaml = config.get('scope_dropdown')
assert scope_dropdown_yaml is not None, 'The config for cat. dropdowns could not be set'

impact_dropdown_yaml = config.get('impact_dropdown')
assert impact_dropdown_yaml is not None, 'The config for the impact dropdowns could not be set'

life_cycle_stage_dropdown = create_dropdown(
    label=life_cycle_stage_dropdown_yaml['label'],
    dropdown_list=life_cycle_stage_dropdown_yaml['dropdown_list'],
    first_item=life_cycle_stage_dropdown_yaml['first_item'],
    dropdown_id=life_cycle_stage_dropdown_yaml['dropdown_id']
)

scope_dropdown = create_dropdown(
    label=scope_dropdown_yaml['label'],
    dropdown_list=scope_dropdown_yaml['dropdown_list'],
    first_item=scope_dropdown_yaml['first_item'],
    dropdown_id=scope_dropdown_yaml['dropdown_id']
)

impact_dropdown = create_dropdown(
    label=impact_dropdown_yaml['label'],
    dropdown_list=impact_dropdown_yaml['dropdown_list'],
    first_item=impact_dropdown_yaml['first_item'],
    dropdown_id=impact_dropdown_yaml['dropdown_id']
)

se_sidebar = dbc.Container(
    [
        dbc.Row(
            [
                life_cycle_stage_dropdown,
                scope_dropdown,
                impact_dropdown
            ]
        ),
        dbc.Row(
            html.Div(id='scenario_card')
        )
    ],
    class_name='p-0 mt-2',
    fluid=True
)

# display_data = dbc.Container(
#     [
#         dbc.Row(
#             dbc.Label(
#                 id='tm_description',
#                 class_name='fs-5 fw-bold mt-2 text-center'
#             ),
#         ),
#         dbc.Row(
#             html.Img(id='tm_image'),
#             class_name='py-4'
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     [
#                         dbc.Card(
#                             [
#                                 dbc.CardHeader(
#                                     "Architecture",
#                                     class_name='fs-5 fw-bold'
#                                 ),
#                                 dbc.CardBody(
#                                     [
#                                         dcc.Markdown(
#                                             id='arch_criteria_text',
#                                             className="card-text",
#                                         ),
#                                     ]
#                                 )
#                             ]
#                         )
#                     ]
#                 ),
#                 dbc.Col(
#                     [
#                         dbc.Card(
#                             [
#                                 dbc.CardHeader(
#                                     "Structure",
#                                     class_name='fs-5 fw-bold'
#                                 ),
#                                 dbc.CardBody(
#                                     [
#                                         dcc.Markdown(
#                                             id='str_criteria_text',
#                                             className="card-text",
#                                         ),
#                                     ]
#                                 )
#                             ]
#                         )
#                     ]
#                 ),
#                 dbc.Col(
#                     [
#                         dbc.Card(
#                             [
#                                 dbc.CardHeader(
#                                     "Enclosure",
#                                     class_name='fs-5 fw-bold'
#                                 ),
#                                 dbc.CardBody(
#                                     [
#                                         dcc.Markdown(
#                                             id='enc_criteria_text',
#                                             className="card-text",
#                                         ),
#                                     ]
#                                 )
#                             ]
#                         )
#                     ]
#                 )
#             ],
#             class_name='pt-4'
#         )
#     ],
#     class_name='px-3 mt-2',
#     fluid=True
# )

# figure = dbc.Container(
#     [
#         dbc.Row(
#             dbc.Label(
#                 'Total Global Warming Potential by Building Element',
#                 class_name='fw-bold text-center'
#             ),
#         ),
#         dbc.Row(
#             dcc.Graph(id="tm_summary"),
#         )
#     ],
#     class_name='mt-2',
#     fluid=True
# )


scenario_explorer_layout = html.Div(
    children=[
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            se_sidebar
                        ], xs=2, sm=2, md=2, lg=2, xl=2, xxl=2,
                        class_name=''
                    ),
                    # dbc.Col(
                    #     [
                    #         sec.display_data
                    #     ], xs=6, sm=6, md=6, lg=6, xl=6, xxl=6,
                    #     class_name=''
                    # ),
                    # dbc.Col(
                    #     [
                    #         sec.description
                    #     ], xs=4, sm=4, md=4, lg=4, xl=4, xxl=4
                    # ),
                ],
                # justify='center',
                className='vh-100'
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
def update_scenario_card(life_cycle_stage):
    if life_cycle_stage == 'Transportation':
        return transportation.a4_scenarios
    else:
        return 'try again!'
