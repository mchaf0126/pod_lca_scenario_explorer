from dash import html
import dash_bootstrap_components as dbc


def create_header() -> html.Div:
    """_summary_

    Returns:
        html.Div: _description_
    """
    navbar = dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.A(
                                html.Img(
                                    src='assets/W-Logo_Purple_RGB.png',
                                    height="60px"
                                ),
                                href='https://carbonleadershipforum.org'
                            )
                        ),
                        dbc.Col(
                            dbc.NavbarBrand(
                                'ARPA-E Template Model Explorer',
                                className='fs-3 text-white fw-bolder'
                            ),
                        ),
                    ],
                    align='center',
                    justify='left',
                    className='g-4 p-0'
                ),
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
            ],
            fluid=True
        ),
        color='primary',
    ),
    return navbar
