from pathlib import Path
from dash import html, dcc
import dash_bootstrap_components as dbc
import src.utils.general as utils


form = dbc.Container(
    [
        dbc.Label(
            'Custom Mix',
            class_name='fs-5 fw-bold my-2 text-center'
        ),
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
    fluid=True,
    className=''
)