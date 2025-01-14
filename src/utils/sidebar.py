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
                                            "3. Scenario Explorer",
                                            href="/scenario_explorer",
                                            active="exact",
                                            className='fw-bolder'
                                        ),
                                        dbc.NavLink(
                                            "4. Model Comparison",
                                            href="/model_comparison",
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
