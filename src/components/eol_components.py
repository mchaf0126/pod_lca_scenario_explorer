from dash import html
import dash_bootstrap_components as dbc
from src.utils.selection import create_checklist, create_radio
from src.utils.load_config import app_config

config = app_config

eol_checklist_yaml = config.get('eol_scenario_checklist')
assert eol_checklist_yaml is not None, 'The config for scenario checklist could not be set'

eol_radio_yaml = config.get('eol_scenario_radio')
assert eol_radio_yaml is not None, 'The config for scenario radio could not be set'

eol_checklist = create_checklist(
    label=eol_checklist_yaml['label'],
    checklist=eol_checklist_yaml['checklist'],
    first_item=eol_checklist_yaml['first_item'],
    dropdown_id={"type": "prebuilt_scenario", "id": 'eol_checklist'}
)

eol_radio_model_comp = create_radio(
    label=eol_radio_yaml['label'],
    radiolist=eol_radio_yaml['radiolist'],
    first_item=eol_radio_yaml['first_item'],
    radio_id=eol_radio_yaml['radio_id']
)

eol_form = html.Div(
    [
        dbc.Label('Custom Mix (full building)'),
        dbc.InputGroup(
            [
                dbc.InputGroupText("% Landfill"),
                dbc.Input(
                    placeholder="percent",
                    type="number",
                    id='eol_custom_landfill',
                    disabled=True
                ),
                dbc.InputGroupText("%"),
            ],
            className="mb-1",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("% Incineration"),
                dbc.Input(
                    placeholder="percent",
                    type="number",
                    id='eol_custom_incineration',
                    disabled=True
                ),
                dbc.InputGroupText("%"),
            ],
            className="mb-1",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("% Recycling"),
                dbc.Input(
                    placeholder="percent",
                    type="number",
                    id='eol_custom_recycling',
                    disabled=True
                ),
                dbc.InputGroupText("%"),
            ],
            className="mb-1",
        ),
    ],
    className='mb-3'
)

eol_form_mc = html.Div(
    [
        dbc.Label('Custom Mix (full building)'),
        dbc.InputGroup(
            [
                dbc.InputGroupText("% Landfill"),
                dbc.Input(
                    placeholder="percent",
                    type="number",
                    id='eol_custom_landfill_mc',
                    disabled=True
                ),
                dbc.InputGroupText("%"),
            ],
            className="mb-1",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("% Incineration"),
                dbc.Input(
                    placeholder="percent",
                    type="number",
                    id='eol_custom_incineration_mc',
                    disabled=True
                ),
                dbc.InputGroupText("%"),
            ],
            className="mb-1",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("% Recycling"),
                dbc.Input(
                    placeholder="percent",
                    type="number",
                    id='eol_custom_recycling_mc',
                    disabled=True
                ),
                dbc.InputGroupText("%"),
            ],
            className="mb-1",
        ),
    ],
    className='mb-3'
)

eol_special_material = html.Div(
    [
        dbc.Label("Custom Mix (component)"),
        dbc.InputGroup(
            [
                dbc.Select(
                    options=[
                        {"label": "CLT Floor", "value": 1},
                        {"label": "Glulam Beam", "value": 2},
                    ],
                    value=1,
                    disabled=True,
                    id='eol_custom_mat_type'
                ),
            ],
            className="mb-1",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("% Reuse"),
                dbc.Input(
                    placeholder="percent",
                    type="number",
                    id='eol_custom_reuse',
                    disabled=True
                ),
                dbc.InputGroupText("%"),
            ],
            className="mb-3",
        ),
    ]
)

eol_special_material_mc = html.Div(
    [
        dbc.Label("Custom Mix (component)"),
        dbc.InputGroup(
            [
                dbc.Select(
                    options=[
                        {"label": "CLT Floor", "value": 1},
                        {"label": "Glulam Beam", "value": 2},
                    ],
                    disabled=True,
                    value=1,
                    id='eol_custom_mat_type_mc'
                ),
            ],
            className="mb-1",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("% Reuse"),
                dbc.Input(
                    placeholder="percent",
                    type="number",
                    id='eol_custom_reuse_mc',
                    disabled=True
                ),
                dbc.InputGroupText("%"),
            ],
            className="mb-3",
        ),
    ]
)

eol_scenarios = dbc.Container(
    [
        dbc.Row(
            [
                eol_checklist,
                eol_form,
                eol_special_material
            ]
        )
    ]
)
