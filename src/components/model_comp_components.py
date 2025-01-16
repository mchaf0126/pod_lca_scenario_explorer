import dash_bootstrap_components as dbc
from src.utils.selection import create_dropdown
import src.components.transportation_components as tc
import src.components.construction_components as cc
import src.components.replacement_components as rc
import src.components.energy_use_components as euc
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
            dbc.Label(
                'Model Comparison',
                class_name='fs-5 fw-bold my-2'
            ),
        ),
        dbc.Row(
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        [
                            scope_dropdown,
                            impact_dropdown
                        ],
                        title="Results",
                        item_id='results'
                    ),
                    dbc.AccordionItem(
                        [
                            tc.transportation_radio_model_comp,
                            tc.a4_special_mat_model_comp
                        ],
                        title="Transportation Scenario",
                        item_id='trans'
                    ),
                    dbc.AccordionItem(
                        [
                            cc.construction_radio_model_comp,
                        ],
                        title="Construction Scenario",
                        item_id='constr'
                    ),
                    dbc.AccordionItem(
                        [
                            rc.replacement_radio_model_comp,
                            rc.replacement_special_mat_model_comp,
                        ],
                        title="Material Replacement Scenario",
                        item_id='repl'
                    ),
                    dbc.AccordionItem(
                        [
                            euc.energy_use_radio_model_comp
                        ],
                        title="Building Energy Use Scenario",
                        item_id='repl'
                    ),
                    dbc.AccordionItem(
                        [
                            ec.eol_radio_model_comp,
                            ec.eol_form_mc,
                            ec.eol_special_material_mc
                        ],
                        title="End-of-life Scenario",
                        item_id='eol'
                    ),
                ],
                start_collapsed=False,
                always_open=True,
                active_item=['results', 'trans', 'constr', 'repl', 'eol'],
            ),
            class_name=''
        )
    ],
    class_name='overflow-scroll h-100 p-0 mt-2 mx-2',
    fluid=True
)
