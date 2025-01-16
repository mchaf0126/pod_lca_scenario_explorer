from dash import dcc
import dash_bootstrap_components as dbc
from src.utils.selection import create_dropdown
from src.utils.load_config import app_config

config = app_config

location_dropdown_yaml = config.get('location_dropdown')
assert location_dropdown_yaml is not None, 'The config for location dropdown could not be set'

building_use_type_dropdown_yaml = config.get('building_use_type_dropdown')
assert building_use_type_dropdown_yaml is not None, 'The config for building use dropdown could not be set'

str_horiz_grav_sys_dropdown_yaml = config.get('str_horiz_grav_sys_dropdown')
assert str_horiz_grav_sys_dropdown_yaml is not None, 'The config for str horiz grav dropdown could not be set'

str_vert_grav_sys_dropdown_yaml = config.get('str_vert_grav_sys_dropdown')
assert str_vert_grav_sys_dropdown_yaml is not None, 'The config for str vert grav dropdown could not be set'

str_lat_sys_dropdown_yaml = config.get('str_lat_sys_dropdown')
assert str_lat_sys_dropdown_yaml is not None, 'The config for str lat dropdown could not be set'

cladding_type_dropdown_yaml = config.get('cladding_type_dropdown')
assert cladding_type_dropdown_yaml is not None, 'The config for cladding dropdown could not be set'

glazing_type_dropdown_yaml = config.get('glazing_type_dropdown')
assert glazing_type_dropdown_yaml is not None, 'The config for glazing dropdown could not be set'

roofing_type_dropdown_yaml = config.get('roofing_type_dropdown')
assert roofing_type_dropdown_yaml is not None, 'The config for roofing dropdown could not be set'

wwr_dropdown_yaml = config.get('wwr_dropdown')
assert wwr_dropdown_yaml is not None, 'The config for wwr dropdown could not be set'

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

str_horiz_grav_sys_dropdown = create_dropdown(
    label=str_horiz_grav_sys_dropdown_yaml['label'],
    dropdown_list=str_horiz_grav_sys_dropdown_yaml['dropdown_list'],
    first_item=str_horiz_grav_sys_dropdown_yaml['first_item'],
    dropdown_id=str_horiz_grav_sys_dropdown_yaml['dropdown_id']
)

str_vert_grav_sys_dropdown = create_dropdown(
    label=str_vert_grav_sys_dropdown_yaml['label'],
    dropdown_list=str_vert_grav_sys_dropdown_yaml['dropdown_list'],
    first_item=str_vert_grav_sys_dropdown_yaml['first_item'],
    dropdown_id=str_vert_grav_sys_dropdown_yaml['dropdown_id']
)

str_lat_sys_dropdown = create_dropdown(
    label=str_lat_sys_dropdown_yaml['label'],
    dropdown_list=str_lat_sys_dropdown_yaml['dropdown_list'],
    first_item=str_lat_sys_dropdown_yaml['first_item'],
    dropdown_id=str_lat_sys_dropdown_yaml['dropdown_id']
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
                            str_horiz_grav_sys_dropdown,
                            str_vert_grav_sys_dropdown,
                            str_lat_sys_dropdown
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
    class_name='p-0 mt-2 overflow-scroll h-100',
    fluid=True
)

display_data = dbc.Container(
    [
        dbc.Row(
            [
                dcc.Markdown(
                    id='criteria_text',
                    className='fw-light'
                ),
            ]
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
