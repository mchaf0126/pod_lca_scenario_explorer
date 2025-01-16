import dash_bootstrap_components as dbc
from dash import html


form = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Label(
                    'Novel Material Selection',
                    class_name='fw-bold my-2 fs-5'
                ),
            ],
        ),
        dbc.Row(
            html.Br(),
        ),
        dbc.Row(
            [
                dbc.Label(
                    'Building Elements to Replace',
                    class_name='fw-bold my-2'
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Omniclass"),
                        dbc.Select(
                            [
                                'Standard Foundations',
                                'Floor Construction',
                                'Exterior Walls',
                                'Exterior Windows',
                                'Roofing',
                                'Electrical Service and Distribution',
                            ],
                            value='Floor Construction'
                        ),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Assembly"),
                        dbc.Select(
                            [
                                'TBD'
                            ],
                            disabled=True,
                            value='TBD'
                        ),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Component"),
                        dbc.Select(
                            [
                                'TBD'
                            ],
                            disabled=True,
                            value='TBD'
                        ),
                    ],
                    className="mb-1",
                ),
            ],
            class_name='mb-4'
        ),
        dbc.Row(
            [
                dbc.Label(
                    'Novel Material Characterization',
                    class_name='fw-bold my-2'
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Novel Material Name"),
                        dbc.Input(placeholder="Name", type="text"),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Functional Unit"),
                        dbc.Input(placeholder="number", type="number"),
                        dbc.Select(
                            [
                                'kg',
                                'kg/m2',
                            ],
                            value='kg',
                        ),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Density"),
                        dbc.Input(placeholder="number", type="number"),
                        dbc.InputGroupText("kg/m3"),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Service Life"),
                        dbc.Input(placeholder="Number of years", type="number"),
                        dbc.InputGroupText("years"),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Construction Wastage Rate"),
                        dbc.Input(placeholder="percentage", type="percent"),
                        dbc.InputGroupText("%"),
                    ],
                    className="mb-1",
                ),
            ],
            class_name='mb-4'
        ),
        dbc.Row(
            [
                dbc.Button(
                    'Import Environmental Impacts from PODLCA Material Tool',
                    color='primary',
                    outline=True,
                    class_name='my-4 d-grid gap-2 col-4 mx-auto'
                ),
                dbc.Label(
                    'Novel Material Impacts - Product',
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
            ],
            class_name='mb-4'
        ),
        dbc.Row(
            [
                dbc.Label(
                    'Novel Material Impacts - Transportation',
                    class_name='fw-bold my-2'
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Distance"),
                        dbc.Input(placeholder="number", type="number"),
                        dbc.Select(
                            [
                                'miles',
                                'kilometers'
                            ],
                            value='miles',
                        ),
                    ],
                    className="mb-1",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Transportation Type"),
                        dbc.Select(
                            [
                                'Truck',
                                'Train',
                                'Barge',
                            ],
                            value='Truck',
                        ),
                    ],
                    className="mb-1",
                ),
            ],
            class_name='mb-4'
        ),
        dbc.Row(
            [
                dbc.Label(
                    'Novel Material Impacts - End-of-life',
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
        ),
    ],
    fluid=True,
    className=''
)
