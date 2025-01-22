from dash import html, callback, Input, Output, State, no_update
import dash_bootstrap_components as dbc
import pandas as pd
from src.utils.selection import create_checklist, create_radio
from src.utils.load_config import app_config

config = app_config

transportation_checklist_yaml = config.get('transporation_scenario_checklist')
assert transportation_checklist_yaml is not None, 'The config for scenario checklist could not be set'

transportation_custom_checklist_yaml = config.get('transporation_custom_scenario_checklist')
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
    dropdown_id={"type": "prebuilt_scenario", "id": 'transportation_custom_scenario_checklist'}
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
                        {"label": "Truck", "value": 1},
                        {"label": "Rail", "value": 2},
                        {"label": "Barge", "value": 3},
                    ],
                    value=1,
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
                    options=[],
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
                        {"label": "Truck", "value": 1},
                        {"label": "Rail", "value": 2},
                        {"label": "Barge", "value": 3},
                    ],
                    value=1,
                    id='transport_custom_transport_type_mc'
                ),
            ],
            className="mb-3",
        ),
    ]
)

transportation_scenarios = dbc.Container(
    [
        dbc.Row(
            [
                transportation_checklist,
                transportation_custom_checklist,
                a4_special_mat
            ]
        )
    ]
)


@callback(
    [
        Output('transport_custom_mat_type', 'disabled'),
        Output('transport_custom_distance', 'disabled'),
        Output('transport_custom_transport_type', 'disabled'),
    ],
    Input({"type": "prebuilt_scenario", "id": 'transportation_custom_scenario_checklist'}, 'value'),
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
    [
        Input('template_model_name', 'data'),
        State('template_model_impacts', 'data'),
    ]
)
def update_intentional_sourcing_dropdown(template_model_name: dict,
                                         template_model_impacts: dict,
                                         ):
    tm_impacts_df = pd.DataFrame.from_dict(template_model_impacts.get('tm_impacts'))
    unpacked_tm_name = template_model_name.get('template_model_value')
    tm_df_for_values = tm_impacts_df[
        (tm_impacts_df['template_model'] == unpacked_tm_name)
    ].copy()
    options_for_dropdown = tm_df_for_values['Building Material_name'].dropna().unique()
    first_option = options_for_dropdown[0]
    return options_for_dropdown, first_option


@callback(
    Output('intentional_sourcing_impacts', 'data'),
    [
        Input('transport_custom_mat_type', 'value'),
        Input('transport_custom_distance', 'value'),
        Input('transport_custom_transport_type', 'value'),
        State('template_model_name', 'data'),
        State('template_model_impacts', 'data'),
        State('transportation_emission_factors', 'data'),
    ]
)
def create_intentional_sourcing_impacts(mat_type: str,
                                        distance: int,
                                        trans_custom_transport_type: str,
                                        template_model_name: dict,
                                        template_model_impacts: dict,
                                        trans_emission_factors: dict
                                        ):
    impacts_map = {
        'Global Warming Potential_fossil': 'GWPf',
        'Global Warming Potential_biogenic': 'GWPb',
        'Global Warming Potential_luluc': 'GWP-LULUC',
        'Acidification Potential': 'acp',
        'Eutrophication Potential': 'eup',
        'Smog Formation Potential': 'smg',
        'Ozone Depletion Potential': 'odp'
    }
    emissions_map = {
        1: 'Transport, combination truck, average fuel mix',
        2: 'Transport, train, diesel powered',
        3: 'Transport, barge, average fuel mix',
    }
    mi_to_km_conversion = 1.60934
    emissions_df = pd.DataFrame.from_dict(
        trans_emission_factors.get(
            'transportation_emission_factors'
        )
    ).fillna(0).set_index('Product system name')
    tm_impacts_df = pd.DataFrame.from_dict(template_model_impacts.get('tm_impacts'))
    unpacked_tm_name = template_model_name.get('template_model_value')
    tm_df_to_update = tm_impacts_df[
        (tm_impacts_df['template_model'] == unpacked_tm_name)
        & (tm_impacts_df['life_cycle_stage'] == "Transportation: A4")
    ].copy()

    if distance == 0:
        return no_update

    if distance > 500:
        additional_factor = 1.5
    else:
        additional_factor = 1.0

    emissions_name = emissions_map.get(trans_custom_transport_type)

    for name, col_name in impacts_map.items():
        # emission = mass of product * emission factor * distance
        emissions_factor_with_emissions_distance = (
            additional_factor
            * emissions_df.loc[emissions_name, col_name]
            * (distance * mi_to_km_conversion)
        )
        print(emissions_factor_with_emissions_distance)
        tm_df_to_update.loc[
            (tm_df_to_update['Building Material_name'] == mat_type), name
        ] = (
            (tm_df_to_update['Weight (kg)'] / 1000)
            * emissions_factor_with_emissions_distance
        )

    print(tm_df_to_update)
    return {"intentional_sourcing_impacts": tm_df_to_update.to_dict()}
