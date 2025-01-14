"""Results page of dashboard"""
from dash import html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import src.components.scenario_explorer_components as se
import src.components.model_comp_components as mc

register_page(__name__, path='/model_comparison')

tabs = dbc.Container(
    [
        dcc.Tabs(
            [
                dcc.Tab(label="Scenario Explorer", id="tab-1"),
                dcc.Tab(label="Model Comparison", id="tab-2"),
            ],
            id="tab_collection",
            value="tab-1",
            className='fw-bold'
        ),
        dbc.Row(
            html.Div(id='tab-content'),
        )
    ],
    fluid=True
)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        tabs
                    ], xs=12, sm=12, md=12, lg=12, xl=12, xxl=12
                ),
            ],
            justify='center',
            className='mb-4'
        ),
    ],
)


@callback(
    Output('tab-content', 'children'),
    Input('tab_collection', 'value')
)
def update_tabs(active_tab):
    if active_tab == 'tab-1':
        return se.scenario_explorer_layout
    if active_tab == 'tab-2':
        return mc.model_comp_layout
