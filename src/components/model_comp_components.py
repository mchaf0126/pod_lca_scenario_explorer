from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from src.utils.selection import create_dropdown
import src.components.transportation_components as tc
import src.components.construction_components as cc
import src.components.replacement_components as rc
import src.components.eol_components as ec
from src.utils.load_config import app_config

config = app_config

scope_dropdown_yaml = config.get('scope_dropdown_model_comp')
assert scope_dropdown_yaml is not None, 'The config for cat. dropdowns could not be set'

impact_dropdown_yaml = config.get('impact_dropdown_model_comp')
assert impact_dropdown_yaml is not None, 'The config for the impact dropdowns could not be set'

category_orders = config.get('category_orders')
assert category_orders is not None, 'The ids for category_orders could not be set'

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

model_comp_sidebar = dbc.Container(
    [
        dbc.Row(
            [
                scope_dropdown,
                impact_dropdown
            ]
        ),
        dbc.Row(
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        [
                            tc.transportation_radio_model_comp,
                            tc.a4_special_mat_model_comp
                        ],
                        title="Transportation",
                    ),
                    dbc.AccordionItem(
                        [
                            cc.construction_radio_model_comp,
                        ],
                        title="Construction",
                    ),
                    dbc.AccordionItem(
                        [
                            rc.replacement_radio_model_comp,
                            rc.replacement_special_mat_model_comp,
                        ],
                        title="Replacement",
                    ),
                    dbc.AccordionItem(
                        [
                            ec.eol_radio_model_comp,
                            ec.eol_form_mc,
                            ec.eol_special_material_mc
                        ],
                        title="End-of-life",
                    ),
                ],
                start_collapsed=True,
                always_open=True
            )
        )
    ],
    class_name='p-0 mt-2',
    fluid=True
)

model_comp_layout = html.Div(
    children=[
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            model_comp_sidebar
                        ], xs=3, sm=3, md=3, lg=3, xl=3, xxl=3,
                        class_name=''
                    ),
                    dbc.Col(
                        [
                            dbc.Container(
                                [
                                    dbc.Row(
                                        dcc.Graph(id="mc_figure"),
                                        class_name='mt-2',
                                    ),
                                    dbc.Row(
                                        html.Div(
                                            id='mc_description',
                                            className='pt-2'
                                        )
                                    ),
                                ],
                                fluid=True,
                                class_name='m-3'
                            )
                        ], xs=9, sm=9, md=9, lg=9, xl=9, xxl=9,
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
    Output('mc_figure', 'figure'),
    [
        Input('impact_dropdown_model_comp', 'value'),
        Input('scope_dropdown_model_comp', 'value'),
        Input('transporation_scenario_radio', 'value'),
        # Input('construction_scenario_radio', 'value'),
        Input('replacement_scenario_radio', 'value'),
        Input('eol_scenario_radio', 'value'),
        State('template_model_name', 'data'),
        State('template_model_impacts', 'data'),
        State('prebuilt_scenario_impacts', 'data'),
    ]
)
def update_se_figure(impact: str,
                     scope: str,
                     trans_scenario: str,
                     # constr_scenario: str,
                     repl_scenario: str,
                     eol_scenario: str,
                     template_model_name: dict,
                     template_model_impacts: dict,
                     prebuilt_scenario_impacts: dict):

    lcs_map = {
        '[A4] Transportation': trans_scenario,
        # '[A5] Construction': constr_scenario,
        '[B2-B5] Maintenance and Replacement': repl_scenario,
        '[C2-C4] End of Life': eol_scenario
    }
    tm_impacts_df = pd.DataFrame.from_dict(template_model_impacts.get('tm_impacts'))
    pb_impacts_df = pd.DataFrame.from_dict(
        prebuilt_scenario_impacts.get('prebuilt_scenario_impacts')
    )
    unpacked_tm_name = template_model_name.get('template_model_value')
    tm_df_to_graph = tm_impacts_df[
        (tm_impacts_df['Revit model'] == unpacked_tm_name)

    ].copy()
    tm_df_to_graph.loc[:, 'model_comp'] = 'Default'

    user_selected_df_to_concat = []
    user_selected_df_to_concat.append(tm_df_to_graph[tm_df_to_graph['Life Cycle Stage'] == '[A1-A3] Product'])
    user_selected_df_to_concat.append(tm_df_to_graph[tm_df_to_graph['Life Cycle Stage'] == '[D] Module D'])
    for lcs, selected_scenario in lcs_map.items():
        if selected_scenario == 'default':
            temp_df = tm_df_to_graph[tm_df_to_graph['Life Cycle Stage'] == lcs]
            user_selected_df_to_concat.append(temp_df)
        else:
            temp_df = pb_impacts_df[
                (
                    (pb_impacts_df['Revit model'] == unpacked_tm_name)
                    & (pb_impacts_df['Life Cycle Stage'] == lcs)
                    & (pb_impacts_df['scenario'] == selected_scenario)
                )
            ]
            user_selected_df_to_concat.append(temp_df)

    user_selected_df_to_graph = pd.concat(user_selected_df_to_concat)
    user_selected_df_to_graph.loc[:, 'model_comp'] = 'User selected custom scenarios'

    combined_df_to_graph = pd.concat([tm_df_to_graph, user_selected_df_to_graph])
    combined_df_to_graph = combined_df_to_graph.sort_values('model_comp')

    fig = px.histogram(
        combined_df_to_graph,
        x='model_comp',
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
    Output('mc_description', 'children'),
    [
        Input('transporation_scenario_radio', 'value'),
        Input('construction_scenario_radio', 'value'),
        Input('replacement_scenario_radio', 'value'),
        Input('eol_scenario_radio', 'value'),
    ]
)
def update_description(trans_scenario: str,
                       constr_scenario: str,
                       repl_scenario: str,
                       eol_scenario: str,):
    text = dcc.Markdown(
        f'''
        ### User selected custom scenarios
        The following scenarios have been selected:
        - Transportation: {trans_scenario}
        - Construction: {constr_scenario}
        - Replacement: {repl_scenario}
        - End-of-life: {eol_scenario}
        ''',
        className='fw-light'
    )
    return text
