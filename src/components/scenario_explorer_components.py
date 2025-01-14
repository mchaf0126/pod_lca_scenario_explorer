from dash import html, dcc, callback, Input, Output, State, ALL
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from src.utils.selection import create_dropdown
from src.components.transportation_components import transportation_scenarios
from src.components.construction_components import construction_scenarios
from src.components.replacement_components import replacement_scenarios
from src.components.eol_components import eol_scenarios
from src.utils.load_config import app_config
from src.components.descriptions import description_map, description_list

config = app_config

life_cycle_stage_dropdown_yaml = config.get('life_cycle_stage_dropdown')
assert life_cycle_stage_dropdown_yaml is not None, 'The config for lcs could not be set'

scope_dropdown_yaml = config.get('scope_dropdown')
assert scope_dropdown_yaml is not None, 'The config for cat. dropdowns could not be set'

impact_dropdown_yaml = config.get('impact_dropdown')
assert impact_dropdown_yaml is not None, 'The config for the impact dropdowns could not be set'

category_orders = config.get('category_orders')
assert category_orders is not None, 'The ids for category_orders could not be set'

life_cycle_stage_dropdown = create_dropdown(
    label=life_cycle_stage_dropdown_yaml['label'],
    dropdown_list=life_cycle_stage_dropdown_yaml['dropdown_list'],
    first_item=life_cycle_stage_dropdown_yaml['first_item'],
    dropdown_id=life_cycle_stage_dropdown_yaml['dropdown_id']
)

scope_dropdown = create_dropdown(
    label=scope_dropdown_yaml['label'],
    dropdown_list=scope_dropdown_yaml['dropdown_list'],
    first_item=scope_dropdown_yaml['first_item'],
    dropdown_id=scope_dropdown_yaml['dropdown_id']
)

impact_dropdown = create_dropdown(
    label=impact_dropdown_yaml['label'],
    dropdown_list=impact_dropdown_yaml['dropdown_list'],
    first_item=impact_dropdown_yaml['first_item'],
    dropdown_id=impact_dropdown_yaml['dropdown_id']
)

se_sidebar = dbc.Container(
    [
        dbc.Row(
            [
                life_cycle_stage_dropdown,
                scope_dropdown,
                impact_dropdown
            ]
        ),
        dbc.Row(
            html.Div(id='scenario_card')
        )
    ],
    class_name='p-0 mt-2',
    fluid=True
)

scenario_explorer_layout = html.Div(
    children=[
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            se_sidebar
                        ], xs=2, sm=2, md=2, lg=2, xl=2, xxl=2,
                        class_name=''
                    ),
                    dbc.Col(
                        [
                            dbc.Container(
                                [
                                    dbc.Row(
                                        dcc.Graph(id="se_figure"),
                                    )
                                ],
                                class_name='mt-2',
                                fluid=True
                            )
                        ], xs=7, sm=7, md=7, lg=7, xl=7, xxl=7,
                        class_name=''
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                id='se_description',
                                className='pt-2'
                            )
                        ], xs=3, sm=3, md=3, lg=3, xl=3, xxl=3
                    ),
                ],
                # justify='center',
                className=''
            ),
            fluid=True,
            class_name='mw-100'
        ),
    ],
)


@callback(
    Output('scenario_card', 'children'),
    Input('life_cycle_stage_dropdown', 'value')
)
def update_scenario_card(life_cycle_stage):
    if life_cycle_stage == 'Transportation':
        return transportation_scenarios
    elif life_cycle_stage == 'Construction':
        return construction_scenarios
    elif life_cycle_stage == 'Replacement':
        return replacement_scenarios
    elif life_cycle_stage == 'End-of-life':
        return eol_scenarios
    else:
        return "try again!"


@callback(
    Output('se_figure', 'figure'),
    [
        Input('life_cycle_stage_dropdown', 'value'),
        Input('impact_dropdown', 'value'),
        Input('scope_dropdown', 'value'),
        Input({'type': 'prebuilt_scenario', 'id': ALL}, 'value'),
        State('template_model_name', 'data'),
        State('template_model_impacts', 'data'),
        State('prebuilt_scenario_impacts', 'data'),
    ]
)
def update_se_figure(life_cycle_stage: str,
                     impact: str,
                     scope: str,
                     checklist: list,
                     template_model_name: dict,
                     template_model_impacts: dict,
                     prebuilt_scenario_impacts: dict):

    lcs_map = {
        'Transportation': '[A4] Transportation',
        'Construction': '[A5] Construction',
        'Replacement': '[B2-B5] Maintenance and Replacement',
        'End-of-life': '[C2-C4] End of Life'
    }
    tm_impacts_df = pd.DataFrame.from_dict(template_model_impacts.get('tm_impacts'))
    pb_impacts_df = pd.DataFrame.from_dict(
        prebuilt_scenario_impacts.get('prebuilt_scenario_impacts')
    )
    unpacked_tm_name = template_model_name.get('template_model_value')
    tm_df_to_graph = tm_impacts_df[
        (tm_impacts_df['Revit model'] == unpacked_tm_name)
        & (tm_impacts_df['Life Cycle Stage'] == lcs_map.get(life_cycle_stage))
    ]
    pb_df_to_graph = pb_impacts_df[
        (pb_impacts_df['Revit model'] == unpacked_tm_name)
        & (pb_impacts_df['Life Cycle Stage'] == lcs_map.get(life_cycle_stage))
        & (pb_impacts_df['scenario'].isin(sum(checklist, [])))
    ]

    categories = category_orders.get(life_cycle_stage)

    combined_df_to_graph = pd.concat([tm_df_to_graph, pb_df_to_graph])
    combined_df_to_graph['scenario'] = pd.Categorical(
        combined_df_to_graph['scenario'],
        ordered=True,
        categories=categories
    )
    combined_df_to_graph = combined_df_to_graph.sort_values('scenario')

    fig = px.histogram(
        combined_df_to_graph,
        x='scenario',
        y=impact,
        color=scope,
        # title=f'GWP Impacts of {unpacked_tm_name}',
        height=600,
    ).update_yaxes(
        title='',
        tickformat=',.0f',
    ).update_xaxes(
        title='',
    ).update_layout(
        # showlegend=False
    )
    return fig


@callback(
    Output('se_description', 'children'),
    [
        Input({'type': 'prebuilt_scenario', 'id': ALL}, 'value'),
    ]
)
def update_description(checklist):
    flattened_checklist = sum(checklist, [])
    sorted_list = sorted(flattened_checklist, key=description_list.index)
    title = [
        dcc.Markdown(
            '''
            ### Descriptions
            See below for a description of the different scenarios that have been selected.
            ''',
            className='fw-light'
        )
    ]
    return title + [description_map.get(value) for value in sorted_list]
