from dash import html, callback, Input, Output, State, no_update
import dash_bootstrap_components as dbc
import pandas as pd
from src.utils.selection import create_checklist, create_radio
from src.utils.load_config import app_config

config = app_config

transportation_checklist_yaml = config.get('transporation_scenario_checklist')
assert transportation_checklist_yaml is not None, 'The config for scenario checklist could not be set'

transportation_custom_checklist_yaml = config.get('transportation_custom_scenario_checklist')
assert transportation_custom_checklist_yaml is not None, 'The config for scenario checklist could not be set'

transportation_radio_yaml = config.get('transporation_scenario_radio')
assert transportation_radio_yaml is not None, 'The config for scenario checklist could not be set'

transportation_checklist = create_checklist(
    label=transportation_checklist_yaml['label'],
    checklist=transportation_checklist_yaml['checklist'],
    first_item=transportation_checklist_yaml['first_item'],
    dropdown_id={"type": "prebuilt_scenario", "id": 'transportation_checklist'}
)

transportation_custom_checklist = create_checklist(
    label=transportation_custom_checklist_yaml['label'],
    checklist=transportation_custom_checklist_yaml['checklist'],
    first_item=transportation_custom_checklist_yaml['first_item'],
    dropdown_id={"type": "custom_checklist", "id": 'transportation_custom_checklist'}
)

transportation_radio_model_comp = create_radio(
    label=transportation_radio_yaml['label'],
    radiolist=transportation_radio_yaml['radiolist'],
    first_item=transportation_radio_yaml['first_item'],
    radio_id=transportation_radio_yaml['radio_id']
)

a4_special_mat = html.Div(
    [
        dbc.InputGroup(
            [
                dbc.Select(
                    id='transport_custom_mat_type'
                ),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Distance (mi)"),
                dbc.Input(
                    value=0,
                    type="number",
                    id='transport_custom_distance'
                ),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Transport Type"),
                dbc.Select(
                    options=[
                        {"label": "Truck", "value": 'truck'},
                        {"label": "Rail", "value": 'rail'},
                        {"label": "Barge", "value": 'barge'},
                    ],
                    value='truck',
                    id='transport_custom_transport_type'
                ),
            ],
            className="mb-3",
        ),
    ]
)

a4_special_mat_model_comp = html.Div(
    [
        dbc.InputGroup(
            [
                dbc.Select(
                    id='transport_custom_mat_type_mc'
                ),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Distance (mi)"),
                dbc.Input(
                    placeholder="0",
                    type="number",
                    id='transport_custom_distance_mc'
                ),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Transport Type"),
                dbc.Select(
                    options=[
                        {"label": "Truck", "value": 'truck'},
                        {"label": "Rail", "value": 'rail'},
                        {"label": "Barge", "value": 'barge'},
                    ],
                    value='truck',
                    id='transport_custom_transport_type_mc'
                ),
            ],
            className="mb-3",
        ),
    ]
)

transportation_scenarios = [
    transportation_checklist,
    transportation_custom_checklist,
    a4_special_mat
]


@callback(
    [
        Output('transport_custom_mat_type', 'disabled'),
        Output('transport_custom_distance', 'disabled'),
        Output('transport_custom_transport_type', 'disabled'),
    ],
    Input({"type": "custom_checklist", "id": 'transportation_custom_checklist'}, 'value'),
)
def update_intentional_sourcing_visibility(checklist):
    if checklist:
        return False, False, False
    else:
        return True, True, True


@callback(
    [
        Output('transport_custom_mat_type', 'options'),
        Output('transport_custom_mat_type', 'value'),
    ],
    Input('current_tm_impacts', 'data'),
)
def update_intentional_sourcing_dropdown_se(current_tm_impacts: dict):
    if current_tm_impacts is None:
        return None, None
    tm_df_for_values = pd.DataFrame.from_dict(current_tm_impacts.get('current_tm_impacts'))
    options_for_dropdown = tm_df_for_values['Building Material_name'].unique()
    first_option = options_for_dropdown[0]
    return options_for_dropdown, first_option


@callback(
    Output('intentional_sourcing_impacts', 'data'),
    [
        Input('transport_custom_mat_type', 'value'),
        Input('transport_custom_distance', 'value'),
        Input('transport_custom_transport_type', 'value'),
        State('current_tm_impacts', 'data'),
        State('transportation_emission_factors', 'data'),
    ],
)
def create_intentional_sourcing_impacts_se(mat_type: str,
                                           distance: int,
                                           trans_custom_transport_type: int,
                                           current_tm_impacts: dict,
                                           trans_emission_factors: dict
                                           ) -> pd.DataFrame:

    se_intentional_sourcing_impacts = create_intentional_sourcing_impacts(
        mat_type=mat_type,
        distance=distance,
        trans_custom_transport_type=trans_custom_transport_type,
        current_tm_impacts=current_tm_impacts,
        trans_emission_factors=trans_emission_factors
    )
    if se_intentional_sourcing_impacts is None:
        return no_update

    return {"se_intentional_sourcing_impacts": se_intentional_sourcing_impacts.to_dict()}


@callback(
    [
        Output('transport_custom_mat_type_mc', 'disabled'),
        Output('transport_custom_distance_mc', 'disabled'),
        Output('transport_custom_transport_type_mc', 'disabled'),
    ],
    Input("transporation_scenario_radio", 'value'),
)
def update_intentional_sourcing_visibility_mc(trans_radio):
    if trans_radio == 'Intentional Sourcing':
        return False, False, False
    else:
        return True, True, True


@callback(
    [
        Output('transport_custom_mat_type_mc', 'options'),
        Output('transport_custom_mat_type_mc', 'value'),
    ],
    Input('current_tm_impacts', 'data'),
)
def update_intentional_sourcing_dropdown_mc(current_tm_impacts: dict):
    if current_tm_impacts is None:
        return None, None
    tm_df_for_values = pd.DataFrame.from_dict(current_tm_impacts.get('current_tm_impacts'))
    options_for_dropdown = tm_df_for_values['Building Material_name'].unique()
    first_option = options_for_dropdown[0]
    return options_for_dropdown, first_option


@callback(
    Output('intentional_sourcing_impacts', 'data', allow_duplicate=True),
    [
        Input('transport_custom_mat_type_mc', 'value'),
        Input('transport_custom_distance_mc', 'value'),
        Input('transport_custom_transport_type_mc', 'value'),
        State('current_tm_impacts', 'data'),
        State('transportation_emission_factors', 'data'),
    ],
    prevent_initial_call=True
)
def create_intentional_sourcing_impacts_mc(mat_type: str,
                                           distance: int,
                                           trans_custom_transport_type: int,
                                           current_tm_impacts: dict,
                                           trans_emission_factors: dict
                                           ) -> pd.DataFrame:

    mc_intentional_sourcing_impacts = create_intentional_sourcing_impacts(
        mat_type=mat_type,
        distance=distance,
        trans_custom_transport_type=trans_custom_transport_type,
        current_tm_impacts=current_tm_impacts,
        trans_emission_factors=trans_emission_factors
    )
    if mc_intentional_sourcing_impacts is None:
        print('hi')
        return no_update

    return {"mc_intentional_sourcing_impacts": mc_intentional_sourcing_impacts.to_dict()}


def create_intentional_sourcing_impacts(mat_type: str,
                                        distance: int,
                                        trans_custom_transport_type: int,
                                        current_tm_impacts: dict,
                                        trans_emission_factors: dict
                                        ) -> pd.DataFrame:
    impacts_map = {
        'Global Warming Potential_fossil': 'GWPf',
        'Global Warming Potential_biogenic': 'GWPb',
        'Global Warming Potential_luluc': 'GWP-LULUC',
        'Acidification Potential': 'acp',
        'Eutrophication Potential': 'eup',
        'Smog Formation Potential': 'smg',
        'Ozone Depletion Potential': 'odp'
    }
    lcs_map = {
        'product': 'A1-A3: Product',
        'trans': 'A4: Transportation',
        'constr': 'A5: Construction',
        'repl': 'B2-B5: Replacement',
        'op': 'B6: Operational Energy',
        'eol': 'C2-C4: End-of-life'
    }
    emissions_map = {
        'truck': 'Transport, combination truck, average fuel mix',
        'rail': 'Transport, train, diesel powered',
        'barge': 'Transport, barge, average fuel mix',
    }
    mi_to_km_conversion = 1.60934
    emissions_df = pd.DataFrame.from_dict(
        trans_emission_factors.get(
            'transportation_emission_factors'
        )
    ).set_index('Product system name')
    if current_tm_impacts is None:
        return None
    tm_impacts_df = pd.DataFrame.from_dict(current_tm_impacts.get('current_tm_impacts'))
    tm_df_to_update = tm_impacts_df[
        tm_impacts_df['life_cycle_stage'] == lcs_map.get('trans')
    ]

    if distance is None:
        return None

    if distance > 500:
        additional_factor = 1.5
    else:
        additional_factor = 1.0

    emissions_name = emissions_map.get(trans_custom_transport_type)

    for name, col_name in impacts_map.items():
        # emission = mass of product * emission factor * distance
        tm_df_to_update.loc[
            (tm_df_to_update['Building Material_name'] == mat_type), name
        ] = (
            additional_factor
            * (tm_df_to_update['Weight (kg)'] / 1000)
            * emissions_df.loc[emissions_name, col_name]
            * (distance * mi_to_km_conversion)
        )

    return tm_df_to_update
