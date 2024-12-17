from dash import dcc
import dash_bootstrap_components as dbc


form = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Label(
                    'Novel material definition',
                    class_name='fw-bold my-2'
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Novel material name"),
                        dbc.Input(placeholder="name", type="text"),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Assembly to replace"),
                        dbc.Select(
                            [
                                'Curtainwall Panels',
                                'Floors',
                                'Walls',
                                'Structural Columns',
                                'Structural Foundations',
                                'Structural Framing',
                            ]
                        ),
                    ],
                    className="mb-1",
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Label(
                    'Novel material characterization',
                    class_name='fw-bold my-2'
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Novel material density"),
                        dbc.Input(placeholder="number", type="number"),
                    ],
                    className="mb-1",
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Label(
                    'Novel material impacts',
                    class_name='fw-bold my-2'
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("GWP_f emission factor"),
                        dbc.Input(placeholder="number", type="number"),
                        dbc.InputGroupText("kgCO2e/kg"),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("GWP_b emission factor"),
                        dbc.Input(placeholder="number", type="number"),
                        dbc.InputGroupText("kgCO2e/kg"),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("GWP_LULUC emission factor"),
                        dbc.Input(placeholder="number", type="number"),
                        dbc.InputGroupText("kgCO2e/kg"),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("EP emission factor"),
                        dbc.Input(placeholder="number", type="number"),
                        dbc.InputGroupText("kgNe/kg"),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("AP emission factor"),
                        dbc.Input(placeholder="number", type="number"),
                        dbc.InputGroupText("kgSO2e/kg"),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("SFP emission factor"),
                        dbc.Input(placeholder="number", type="number"),
                        dbc.InputGroupText("kgO3e/kg"),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("ODP emission factor"),
                        dbc.Input(placeholder="number", type="number"),
                        dbc.InputGroupText("CFC-11e/kg"),
                    ],
                    className="mb-1",
                ),
            ]
        )
    ],
    fluid=True,
    className=''
)

figure = dbc.Container(
    [
        dbc.Row(
            dbc.Label(
                'Future Graph TBD',
                class_name='fs-5 fw-bold mt-2 text-center'
            ),
        ),
        dbc.Row(
            dcc.Graph(id="nm_summary"),
        )
    ],
    class_name='mt-2',
    fluid=True
)
