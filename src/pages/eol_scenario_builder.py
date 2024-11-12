"""Results page of dashboard"""
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import html, dcc, callback, Input, Output, register_page, no_update
import dash_bootstrap_components as dbc
import src.utils.general as utils
from src.components.selection import create_dropdown, create_checklist, \
    create_radio
# from src.components.eol_components import create_custom_form, \
#     create_special_material_form

register_page(__name__, path='/eol_scenario_builder')

current_file_path = Path(__file__)
main_directory = current_file_path.parents[2]
prebuilt_scenario_directory = main_directory.joinpath('data/frontend/combined_prebuilt_scenarios.csv')
template_model_impact_directory = main_directory.joinpath('data/frontend/combined_impacts.csv')

prebuilt_scenario_df = pd.read_csv(prebuilt_scenario_directory, index_col=False)
template_model_impact_df = pd.read_csv(template_model_impact_directory, index_col=False)

config_path = main_directory.joinpath('src/components/config.yml')

config = utils.read_yaml(config_path)
assert config is not None, 'The config dictionary could not be set'

eol_radioitem_yaml = config.get('eol_scenario_radioitem')
assert eol_radioitem_yaml is not None, 'The config for eol radioitem could not be set'

scope_dropdown_yaml = config.get('scope_dropdown_eol_scenario')
assert scope_dropdown_yaml is not None, 'The config for cat. dropdowns could not be set'

scenario_checklist_yaml = config.get('eol_scenario_checklist')
assert scenario_checklist_yaml is not None, 'The config for scenario checklist could not be set'

impact_dropdown_yaml = config.get('eol_impact_dropdown')
assert impact_dropdown_yaml is not None, 'The config for the impact dropdowns could not be set'

eol_radioitem = create_radio(
    label=eol_radioitem_yaml['label'],
    radiolist=eol_radioitem_yaml['radiolist'],
    first_item=eol_radioitem_yaml['first_item'],
    radio_id=eol_radioitem_yaml['radio_id']
)

scope_dropdown = create_dropdown(
    label=scope_dropdown_yaml['label'],
    dropdown_list=scope_dropdown_yaml['dropdown_list'],
    first_item=scope_dropdown_yaml['first_item'],
    dropdown_id=scope_dropdown_yaml['dropdown_id']
)

scenario_checklist = create_checklist(
    label=scenario_checklist_yaml['label'],
    checklist=scenario_checklist_yaml['checklist'],
    first_item=scenario_checklist_yaml['first_item'],
    dropdown_id=scenario_checklist_yaml['checklist_id']
)

impact_dropdown = create_dropdown(
    label=impact_dropdown_yaml['label'],
    dropdown_list=impact_dropdown_yaml['dropdown_list'],
    first_item=impact_dropdown_yaml['first_item'],
    dropdown_id=impact_dropdown_yaml['dropdown_id']
)

card_child = dbc.CardBody(
    [
        dbc.Label('End of Life Scenarios', class_name='fs-5 fw-bold my-0'),
        html.Hr(),
        eol_radioitem,
    ],
    class_name='pb-0'
)
second_child = dbc.CardBody(
    children=[scope_dropdown, impact_dropdown, scenario_checklist],
    id='second_card_body_eol',
    class_name='my_0 py-0',
)
# form = create_custom_form()
# special_mat1 = create_special_material_form(
#     label='Special Material 1',
#     value=1

# )
# special_mat2 = create_special_material_form(
#     label='Special Material 2',
#     value=2
# )

controls_cont = dbc.Card(
    [
        card_child,
        second_child
    ],
    id='eol_card'
)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        controls_cont
                    ], xs=4, sm=4, md=3, lg=3, xl=3, xxl=3
                ),
                dbc.Col(
                    [
                        dcc.Graph(id="eol_scenario_bar"),
                        dcc.Markdown(id='eol_potential_error_message', className='text-center')
                    ], xs=8, sm=8, md=9, lg=9, xl=9, xxl=9
                ),
            ],
            justify='center',
            className='mb-4'
        ),
    ],
)

@callback(
    Output('second_card_body_eol', 'children'),
    Input('eol_scenario_radioitem', 'value')
)
def update_second_card_body(radio_item):
    if radio_item == 'custom':
        return html.Div('Custom Scenarios are not implemented yet')
    else:
        return [scope_dropdown, impact_dropdown, scenario_checklist]


@callback(
    [
        Output('eol_scenario_bar', 'figure'),
        Output('eol_potential_error_message', 'children')
    ],
    [
        Input('template_model_name', 'data'),
        Input(scope_dropdown_yaml.get('dropdown_id'), 'value'),
        Input(scenario_checklist_yaml.get('checklist_id'), 'value'),
        Input(impact_dropdown_yaml.get('dropdown_id'), 'value'),
    ],
    prevent_initial_callback=True
)
def update_chart(template_model_name_dict: dict,
                 categorization: str,
                 prebuilt_scenario: list[str],
                 impact_type: str):

    print(prebuilt_scenario)
    # check if template model has been selected
    if template_model_name_dict is None:
        return no_update, '## Please select a Template Model first'

    # filter down to selected template model's a4 impacts
    temp_model_filter = template_model_impact_df['Revit model'] == template_model_name_dict.get('template_model_value')
    b4_filter = template_model_impact_df['Life Cycle Stage'] == '[C2-C4] End of Life'

    filtered_template_model_df = template_model_impact_df[
        temp_model_filter & b4_filter
    ]

    # filter down to selected template model from prebuilt scenarios
    filtered_prebuilt_scenario_df = prebuilt_scenario_df[
        prebuilt_scenario_df['Revit model'] == template_model_name_dict.get('template_model_value')
    ]

    # get eol impacts from the template model
    new_df = pd.melt(
        filtered_template_model_df,
        id_vars=categorization,
        value_vars=impact_type,
        var_name='Impacts',
        value_name='Impact Amount'
    )
    new_df = new_df.groupby(categorization).sum()
    new_df['Impacts'] = f'{template_model_name_dict.get("template_model_name")} - Default End-of-life'

    # create dataframes with the selected impact_type for each prebuilt scenario chosen
    list_of_dfs = [new_df]
    for unique_p_scenario in prebuilt_scenario:
        temp = filtered_prebuilt_scenario_df[
            filtered_prebuilt_scenario_df['prebuilt_scenario'] == unique_p_scenario
        ]
        p_scenario_df = pd.melt(
            temp,
            id_vars=categorization,
            value_vars=impact_type,
            var_name='Impacts',
            value_name='Impact Amount'
        )
        p_scenario_df = p_scenario_df.groupby(categorization).sum()
        p_scenario_df['Impacts'] = f'{template_model_name_dict.get("template_model_name")} - {unique_p_scenario}'

        list_of_dfs.append(p_scenario_df)

    # combine these dataframes to visualize them
    checklist_df = pd.concat(list_of_dfs)

    # create graph
    fig = px.bar(
        checklist_df,
        x='Impacts',
        y='Impact Amount',
        color=checklist_df.index,
        title=f'Impacts for End-of-life Scenarios of {template_model_name_dict.get("template_model_name")}'
    ).update_yaxes(
        title=f'Total Global Warming Potential by {categorization}',
        tickformat=',.0f',
    ).update_xaxes(
        categoryorder='category ascending',
        title=''
    )
    fig.update_traces(width=.2 + .2 * len(prebuilt_scenario))
    if len(prebuilt_scenario) > 2:
        fig.update_traces(width=.8)

    return fig, ''
