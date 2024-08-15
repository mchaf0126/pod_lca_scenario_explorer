from dash import html, dcc
import dash_bootstrap_components as dbc


def create_custom_dropdowns() -> html.Div:
    """_summary_

    Returns:
        html.Div: _description_
    """
    custom_dropdowns = html.Div(
        [
            html.Div(
                [
                    dbc.Label('Envelope'),
                    dcc.Dropdown(
                        options=[
                            '20 Year Full Replacement',
                            '25 Year Full Replacement',
                            '40 Year Full Replacement'
                        ],
                        value='20 Year Full Replacement',
                        id='custom_b4_envelope_id',
                        clearable=False,
                        className='mb-3'
                    ),
                ],
            ),
            html.Div(
                [
                    dbc.Label('Finishes'),
                    dcc.Dropdown(
                        options=[
                            '20 Year Full Replacement',
                            '25 Year Full Replacement',
                            '40 Year Full Replacement'
                        ],
                        value='20 Year Full Replacement',
                        id='custom_b4_finishes_id',
                        clearable=False,
                        className='mb-3'
                    ),
                ],
            ),
            html.Div(
                [
                    dbc.Label('Circularity'),
                    dcc.Dropdown(
                        options=[
                            '20% Design for Deconstruction',
                            '40% Design for Deconstruction',
                            '60% Design for Deconstruction'
                        ],
                        value='20% Design for Deconstruction',
                        id='custom_b4_circularity_id',
                        clearable=False,
                        className='mb-3'
                    ),
                ],
            ),
        ],
        className='mb-3'
    )
    return custom_dropdowns
