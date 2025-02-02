from dash import html, callback, Input, Output, State, no_update
import dash_bootstrap_components as dbc
import pandas as pd
from src.utils.selection import create_checklist, create_radio
from src.utils.load_config import app_config

config = app_config

replacement_checklist_yaml = config.get('replacement_scenario_checklist')
assert replacement_checklist_yaml is not None, 'The config for scenario checklist could not be set'

replacement_custom_checklist_yaml = config.get('replacement_custom_scenario_checklist')
assert replacement_custom_checklist_yaml is not None, 'The config for scenario checklist could not be set'

replacement_radio_yaml = config.get('replacement_scenario_radio')
assert replacement_radio_yaml is not None, 'The config for scenario radio could not be set'

replacement_checklist = create_checklist(
    label=replacement_checklist_yaml['label'],
    checklist=replacement_checklist_yaml['checklist'],
    first_item=replacement_checklist_yaml['first_item'],
    dropdown_id={"type": "prebuilt_scenario", "id": 'replacement_checklist'}
)

replacement_custom_checklist = create_checklist(
    label=replacement_custom_checklist_yaml['label'],
    checklist=replacement_custom_checklist_yaml['checklist'],
    first_item=replacement_custom_checklist_yaml['first_item'],
    dropdown_id={"type": "custom_checklist", "id": 'replacement_custom_checklist'}
)

replacement_radio_model_comp = create_radio(
    label=replacement_radio_yaml['label'],
    radiolist=replacement_radio_yaml['radiolist'],
    first_item=replacement_radio_yaml['first_item'],
    radio_id=replacement_radio_yaml['radio_id']
)

replacement_special_mat = html.Div(
    [
        dbc.InputGroup(
            [
                dbc.Select(
                    id='replacement_custom_mat_type'
                ),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Replacement Rate (yr)"),
                dbc.Input(
                    value=40,
                    type="number",
                    id='replacement_custom_year'
                ),
            ],
            className="mb-3",
        ),
    ]
)

replacement_special_mat_model_comp = html.Div(
    [
        dbc.InputGroup(
            [
                dbc.Select(
                    id='replacement_custom_mat_type_mc'
                ),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Replacement Rate (yr)"),
                dbc.Input(
                    value=40,
                    type="number",
                    id='replacement_custom_year_mc'
                ),
            ],
            className="mb-3",
        ),
    ]
)

replacement_scenarios = [
    replacement_checklist,
    replacement_custom_checklist,
    replacement_special_mat
]


@callback(
    [
        Output('replacement_custom_mat_type', 'disabled'),
        Output('replacement_custom_year', 'disabled'),
    ],
    Input({"type": "custom_checklist", "id": 'replacement_custom_checklist'}, 'value'),
)
def update_intentional_replacement_visibility_se(checklist):
    if checklist:
        return False, False
    else:
        return True, True


@callback(
    [
        Output('replacement_custom_mat_type_mc', 'disabled'),
        Output('replacement_custom_year_mc', 'disabled'),
    ],
    Input('replacement_scenario_radio', 'value'),
)
def update_intentional_replacement_visibility_mc(radio):
    if radio == 'Intentional Replacement':
        return False, False
    else:
        return True, True


@callback(
    [
        Output('replacement_custom_mat_type', 'options'),
        Output('replacement_custom_mat_type', 'value'),
    ],
    Input('current_tm_impacts', 'data'),
)
def update_intentional_replacement_dropdown_se(current_tm_impacts: dict,):
    if current_tm_impacts is None:
        return None, None
    tm_df_for_values = pd.DataFrame.from_dict(current_tm_impacts.get('current_tm_impacts'))
    options_for_dropdown = tm_df_for_values['Assembly'].dropna().unique()
    first_option = options_for_dropdown[0]
    return options_for_dropdown, first_option


@callback(
    [
        Output('replacement_custom_mat_type_mc', 'options'),
        Output('replacement_custom_mat_type_mc', 'value'),
    ],
    Input('current_tm_impacts', 'data'),
)
def update_intentional_replacement_dropdown_mc(current_tm_impacts: dict,):
    if current_tm_impacts is None:
        return None, None
    tm_df_for_values = pd.DataFrame.from_dict(current_tm_impacts.get('current_tm_impacts'))
    options_for_dropdown = tm_df_for_values['Assembly'].dropna().unique()
    first_option = options_for_dropdown[0]
    return options_for_dropdown, first_option


@callback(
    Output('intentional_replacement_impacts', 'data'),
    [
        Input('replacement_custom_mat_type', 'value'),
        Input('replacement_custom_year', 'value'),
        State('current_tm_impacts', 'data'),
    ]
)
def create_intentional_replacement_impacts_se(mat_type: str,
                                              input_years: int,
                                              current_tm_impacts: dict,
                                              ):
    se_intentional_replacement_impacts = create_intentional_replacement_impacts(
        mat_type=mat_type,
        input_years=input_years,
        current_tm_impacts=current_tm_impacts
    )

    if se_intentional_replacement_impacts is None:
        return no_update

    return {"se_intentional_replacement_impacts": se_intentional_replacement_impacts.to_dict()}


@callback(
    Output('intentional_replacement_impacts_mc', 'data'),
    [
        Input('replacement_custom_mat_type_mc', 'value'),
        Input('replacement_custom_year_mc', 'value'),
        State('current_tm_impacts', 'data'),
    ],
)
def create_intentional_replacement_impacts_mc(mat_type: str,
                                              input_years: int,
                                              current_tm_impacts: dict,
                                              ):
    mc_intentional_replacement_impacts = create_intentional_replacement_impacts(
        mat_type=mat_type,
        input_years=input_years,
        current_tm_impacts=current_tm_impacts
    )

    if mc_intentional_replacement_impacts is None:
        return no_update

    return {"mc_intentional_replacement_impacts": mc_intentional_replacement_impacts.to_dict()}


def create_intentional_replacement_impacts(mat_type: str,
                                           input_years: int,
                                           current_tm_impacts: dict,
                                           ):
    impacts_list = [
        'Global Warming Potential_fossil',
        'Global Warming Potential_biogenic',
        'Global Warming Potential_luluc',
        'Acidification Potential',
        'Eutrophication Potential',
        'Smog Formation Potential',
        'Ozone Depletion Potential',
    ]
    lcs_map = {
        'product': 'A1-A3: Product',
        'trans': 'A4: Transportation',
        'constr': 'A5: Construction',
        'repl': 'B2-B5: Replacement',
        'op': 'B6: Operational Energy',
        'eol': 'C2-C4: End-of-life'
    }
    rsp = 60
    if current_tm_impacts is None:
        return None

    tm_df_to_update = pd.DataFrame.from_dict(
        current_tm_impacts.get('current_tm_impacts')
    ).set_index('element_index')

    tm_product_impacts = tm_df_to_update[
        (tm_df_to_update['life_cycle_stage'] == lcs_map.get('product'))
        & (tm_df_to_update['Assembly'] == mat_type)
    ]
    tm_trans_impacts = tm_df_to_update[
        (tm_df_to_update['life_cycle_stage'] == lcs_map.get('trans'))
        & (tm_df_to_update['Assembly'] == mat_type)
    ]
    tm_constr_impacts = tm_df_to_update[
        (tm_df_to_update['life_cycle_stage'] == lcs_map.get('constr'))
        & (tm_df_to_update['Assembly'] == mat_type)
    ]
    tm_eol_impacts = tm_df_to_update[
        (tm_df_to_update['life_cycle_stage'] == lcs_map.get('eol'))
        & (tm_df_to_update['Assembly'] == mat_type)
    ]

    if input_years >= 60:
        number_of_replacements = 0
    elif input_years <= 0:
        number_of_replacements = 0
    else:
        number_of_replacements = rsp // input_years

    for name in impacts_list:
        tm_df_to_update.loc[
            (
                (tm_df_to_update['Assembly'] == mat_type)
                & (tm_df_to_update['life_cycle_stage'] == lcs_map.get('repl'))
            ), name
        ] = (
            tm_product_impacts.loc[:, name]
            + tm_trans_impacts.loc[:, name]
            + tm_constr_impacts.loc[:, name]
            + tm_eol_impacts.loc[:, name]
        ).mul(number_of_replacements)

    tm_df_to_update = tm_df_to_update[tm_df_to_update['life_cycle_stage'] == lcs_map.get('repl')]

    return tm_df_to_update
