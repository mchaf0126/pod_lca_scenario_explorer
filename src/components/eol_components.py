from dash import html
import dash_bootstrap_components as dbc


def create_custom_form() -> html.Div:
    """_summary_

    Returns:
        html.Div: _description_
    """
    form = html.Div(
        [
            dbc.Label('Custom Mix'),
            dbc.InputGroup(
                [
                    dbc.InputGroupText("% Landfill"),
                    dbc.Input(placeholder="percent", type="number"),
                    dbc.InputGroupText("%"),
                ],
                className="mb-1",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupText("% Incineration"),
                    dbc.Input(placeholder="percent", type="number"),
                    dbc.InputGroupText("%"),
                ],
                className="mb-1",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupText("% Recycling"),
                    dbc.Input(placeholder="percent", type="number"),
                    dbc.InputGroupText("%"),
                ],
                className="mb-1",
            ),
        ],
        className='mb-3'
    )
    return form


def create_special_material_form(label: str,
                                 value: str) -> html.Div:
    """_summary_

    Args:
        label (str): _description_

    Returns:
        html.Div: _description_
    """
    special_mat1 = html.Div(
        [
            dbc.Label(label),
            dbc.InputGroup(
                [
                    dbc.Select(
                        options=[
                            {"label": "CLT Floor", "value": 1},
                            {"label": "Glulam Beam", "value": 2},
                        ],
                        value=value
                    ),
                ],
                className="mb-1",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupText("% Reuse"),
                    dbc.Input(placeholder="percent", type="number"),
                    dbc.InputGroupText("%"),
                ],
                className="mb-3",
            ),
        ]
    )
    return special_mat1
