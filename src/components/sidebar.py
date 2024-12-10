from dash import html
import dash_bootstrap_components as dbc


def create_sidebar() -> html.Div:
    """_summary_

    Returns:
        html.Div: _description_
    """
    sidebar = dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H2("Roadmap"),
                                html.Hr(),
                                dbc.Nav(
                                    [
                                        dbc.NavLink(
                                            "Home",
                                            href="/",
                                            active="exact",
                                            className='fw-bolder'
                                        ),
                                        dbc.NavLink(
                                            "1. Template Model Selection",
                                            href="/template_model",
                                            active="exact",
                                            className='fw-bolder'
                                        ),
                                        dbc.NavLink(
                                            "2. Novel Material Selection",
                                            href="/novel_material",
                                            active="exact",
                                            className='fw-bolder'
                                        ),
                                        dbc.NavLink(
                                            "3. Results",
                                            href="/results",
                                            active="exact",
                                            className='fw-bolder'
                                        ),
                                    ],
                                    vertical=True,
                                    pills=True,
                                )
                            ],
                        )
                    ],
                )
            ],
            fluid=True,
        ),
        color='light',
    )
    return sidebar
# dbc.Nav([
#     dbc.NavItem(
#         [
#             dbc.NavLink(
#                 'Home',
#                 href='/',
#                 className='fs-5 text-white fw-bolder'
#             )
#         ]
#     ),
#     dbc.NavItem(
#         [
#             dbc.NavLink(
#                 'Template Models',
#                 href='/template_model',
#                 className='fs-5 text-white fw-bolder'
#             )
#         ]
#     ),
#     dbc.NavItem(
#         [
#             dbc.NavLink(
#                 'Results',
#                 href='/results',
#                 className='fs-5 text-white fw-bolder'
#             ),
#         ],
#     ),
#     dbc.DropdownMenu(
#         label='Scenarios',
#         children=[
#             dbc.DropdownMenuItem(
#                 "Transportation Scenarios",
#                 href="a4_scenario_builder"
#             ),
#             dbc.DropdownMenuItem(
#                 "Construction Scenarios",
#                 href="a5_scenario_builder"
#             ),
#             dbc.DropdownMenuItem(
#                 "Replacement Scenarios",
#                 href="b4_scenario_builder"
#             ),
#             dbc.DropdownMenuItem(
#                 "End-of-life Scenarios",
#                 href="eol_scenario_builder"
#             )
#         ],
#         align_end=True,
#         nav=True,
#         toggleClassName='fs-5 text-white fw-bolder',
#     ),
# ])
