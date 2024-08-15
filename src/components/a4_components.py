from dash import html
import dash_bootstrap_components as dbc


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
                            {"label": "Wood fiber insulation", "value": 1},
                            {"label": "CLT", "value": 2},
                            {"label": "Glulam", "value": 3}
                        ],
                        value=value
                    ),
                ],
                className="mb-1",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupText("Distance"),
                    dbc.Input(placeholder=" ", type="number"),
                    dbc.Select(
                        options=[
                            {"label": "km", "value": 1},
                            {"label": "mi", "value": 2},
                        ],
                        value=1
                    ),
                ],
                className="mb-3",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupText("Transport Type"),
                    dbc.Select(
                        options=[
                            {"label": "Truck", "value": 1},
                            {"label": "Rail", "value": 2},
                            {"label": "Barge", "value": 2},
                        ],
                        value=1
                    ),
                ],
                className="mb-3",
            ),
        ]
    )
    return special_mat1
