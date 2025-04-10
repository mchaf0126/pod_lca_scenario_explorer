from dash import dcc
import dash_bootstrap_components as dbc
from src.utils.selection import create_dropdown
from src.utils.load_config import app_config

config = app_config

location_dropdown_yaml = config.get('location_dropdown')
assert location_dropdown_yaml is not None, 'The config for location dropdown could not be set'

building_use_type_dropdown_yaml = config.get('building_use_type_dropdown')
assert building_use_type_dropdown_yaml is not None, 'The config for building use dropdown could not be set'

str_material_dropdown_yaml = config.get('str_material_dropdown')
assert str_material_dropdown_yaml is not None, 'The config for str horiz grav dropdown could not be set'

column_span_dropdown_yaml = config.get('column_span_dropdown')
assert column_span_dropdown_yaml is not None, 'The config for column span dropdown could not be set'

cladding_type_dropdown_yaml = config.get('cladding_type_dropdown')
assert cladding_type_dropdown_yaml is not None, 'The config for cladding dropdown could not be set'

glazing_type_dropdown_yaml = config.get('glazing_type_dropdown')
assert glazing_type_dropdown_yaml is not None, 'The config for glazing dropdown could not be set'

roofing_type_dropdown_yaml = config.get('roofing_type_dropdown')
assert roofing_type_dropdown_yaml is not None, 'The config for roofing dropdown could not be set'

wwr_dropdown_yaml = config.get('wwr_dropdown')
assert wwr_dropdown_yaml is not None, 'The config for wwr dropdown could not be set'

template_model_dropdown_yaml = config.get('template_model_graph_dropdown')
assert template_model_dropdown_yaml is not None, 'The config for tm_graph dropdown could not be set'

location_dropdown = create_dropdown(
    label=location_dropdown_yaml['label'],
    dropdown_list=location_dropdown_yaml['dropdown_list'],
    first_item=location_dropdown_yaml['first_item'],
    dropdown_id=location_dropdown_yaml['dropdown_id']
)

building_use_type_dropdown = create_dropdown(
    label=building_use_type_dropdown_yaml['label'],
    dropdown_list=building_use_type_dropdown_yaml['dropdown_list'],
    first_item=building_use_type_dropdown_yaml['first_item'],
    dropdown_id=building_use_type_dropdown_yaml['dropdown_id']
)

column_span_dropdown = create_dropdown(
    label=column_span_dropdown_yaml['label'],
    dropdown_list=column_span_dropdown_yaml['dropdown_list'],
    first_item=column_span_dropdown_yaml['first_item'],
    dropdown_id=column_span_dropdown_yaml['dropdown_id']
)

structural_material_dropdown = create_dropdown(
    label=str_material_dropdown_yaml['label'],
    dropdown_list=str_material_dropdown_yaml['dropdown_list'],
    first_item=str_material_dropdown_yaml['first_item'],
    dropdown_id=str_material_dropdown_yaml['dropdown_id']
)

cladding_type_dropdown = create_dropdown(
    label=cladding_type_dropdown_yaml['label'],
    dropdown_list=cladding_type_dropdown_yaml['dropdown_list'],
    first_item=cladding_type_dropdown_yaml['first_item'],
    dropdown_id=cladding_type_dropdown_yaml['dropdown_id']
)

glazing_type_dropdown = create_dropdown(
    label=glazing_type_dropdown_yaml['label'],
    dropdown_list=glazing_type_dropdown_yaml['dropdown_list'],
    first_item=glazing_type_dropdown_yaml['first_item'],
    dropdown_id=glazing_type_dropdown_yaml['dropdown_id']
)

roofing_type_dropdown = create_dropdown(
    label=roofing_type_dropdown_yaml['label'],
    dropdown_list=roofing_type_dropdown_yaml['dropdown_list'],
    first_item=roofing_type_dropdown_yaml['first_item'],
    dropdown_id=roofing_type_dropdown_yaml['dropdown_id']
)

wwr_dropdown = create_dropdown(
    label=wwr_dropdown_yaml['label'],
    dropdown_list=wwr_dropdown_yaml['dropdown_list'],
    first_item=wwr_dropdown_yaml['first_item'],
    dropdown_id=wwr_dropdown_yaml['dropdown_id']
)

tm_graph_dropdown = create_dropdown(
    label=template_model_dropdown_yaml['label'],
    dropdown_list=template_model_dropdown_yaml['dropdown_list'],
    first_item=template_model_dropdown_yaml['first_item'],
    dropdown_id=template_model_dropdown_yaml['dropdown_id']
)

sidebar = dbc.Container(
    [
        dbc.Row(
            dbc.Label(
                'Template Model Selector',
                class_name='fs-5 fw-bold my-2'
            ),
        ),
        dbc.Row(
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        [
                            location_dropdown,
                            building_use_type_dropdown
                        ],
                        title="Building information",
                        item_id='build_info'
                    ),
                    dbc.AccordionItem(
                        [
                            structural_material_dropdown,
                            column_span_dropdown
                        ],
                        title="Structure",
                        item_id='str'
                    ),
                    dbc.AccordionItem(
                        [
                            cladding_type_dropdown,
                            glazing_type_dropdown,
                            roofing_type_dropdown,
                            wwr_dropdown
                        ],
                        title="Enclosure",
                        item_id='enc'
                    ),
                ],
                start_collapsed=True,
                always_open=True,
                active_item=['build_info', 'str', 'enc'],
            )
        )
    ],
    class_name='p-0 mt-2 mx-2 overflow-scroll h-100',
    fluid=True
)

display_data = dbc.Container(
    [
        dbc.Row(
            id='criteria_text',
        )
    ],
    class_name='px-3 mt-2',
    fluid=True
)

figure = dbc.Container(
    [
        dbc.Row(
            dcc.Graph(id="tm_summary"),
        )
    ],
    class_name='mt-2',
    fluid=True
)
