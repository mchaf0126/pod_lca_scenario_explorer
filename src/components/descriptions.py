from dash import dcc
import dash_bootstrap_components as dbc

default_transportation = [
    dbc.Label(
        'North American Average (default)',
        class_name='fs-5 fw-bold my-2'
    ),
    dcc.Markdown(
        '''
        Typical transportation distances and emissions based on North American production.
        This scenario is based on the ASHRAE/ICC 240P Standard, including default transportation modes and distances.
        Calculation of impacts includes a return trip factor for trips longer than 500 miles.
        ''',
        className='fw-light'
    )
]

domestic_supply_chain = [
    dbc.Label(
        'Regionally-Specific Distances',
        class_name='fs-5 fw-bold my-2'
    ),
    dcc.Markdown(
        '''
        This scenario uses the US Commodity Flow Survey to derive transportation distances
        for a specific consumption region for a specific material category as selected by the user.
        ''',
        className='fw-light'
    )
]

global_supply_chain = [
    dbc.Label(
        'Global Supply Chain',
        class_name='fs-5 fw-bold my-2'
    ),
    dcc.Markdown(
        '''
        Using a globally focused data source, a more generalized distance for materials would
        be used to reflect sourcing from outside of the country.
        ''',
        className='fw-light'
    )
]

intentional_sourcing = [
    dbc.Label(
        'Intentional Sourcing',
        class_name='fs-5 fw-bold my-2'
    ),
    dcc.Markdown(
        '''
        In this custom scenario, a user can choose a specific material, transport mode, and
        distance to calculate transportation emissions for that material.
        ''',
        className='fw-light'
    )
]

default_construction = [
    dbc.Label(
        'North American Average (default)',
        class_name='fs-5 fw-bold my-2'
    ),
    dcc.Markdown(
        '''
        This scenario reflects default values for material-specific wastage rates based on
        ASHRAE/ICC 240P Standard.  This scenario currently does not include construction activities.
        ''',
        className='fw-light'
    )
]

advanced_waste_recovery = [
    dbc.Label(
        'Advanced Waste Recovery',
        class_name='fs-5 fw-bold my-2'
    ),
    dcc.Markdown(
        '''
        This scenario represents practices for construction waste management, such as
        increased diversion of C&D waste materials compliant with the LEED v4 waste
        management credit.
        ''',
        className='fw-light'
    )
]

default_replacement = [
    dbc.Label(
        'Typical Replacement Rates (default)',
        class_name='fs-5 fw-bold my-2'
    ),
    dcc.Markdown(
        '''
        This scenario reflects typical replacement for North American construction
        based on ASHRAE/ICC 240P Standard.
        ''',
        className='fw-light'
    )
]

rics = [
    dbc.Label(
        'RICS Replacement Rates',
        class_name='fs-5 fw-bold my-2'
    ),
    dcc.Markdown(
        '''
        This scenario reflects replacement for construction based on the
        RICS whole life carbon assessment (WLCA) standard, 2nd edition.
        ''',
        className='fw-light'
    )
]

intentional_replacement = [
    dbc.Label(
        'Intentional Replacement',
        class_name='fs-5 fw-bold my-2'
    ),
    dcc.Markdown(
        '''
        In this custom scenario, a user would be able to choose a specific material and a replacement
        year in order to recalculate emissions for that material
        ''',
        className='fw-light'
    )
]

default_eol = [
    dbc.Label(
        'National Average C&D Treatment Mix (default)',
        class_name='fs-5 fw-bold my-2'
    ),
    dcc.Markdown(
        '''
        Typical end-of-life impacts based on North American average production data.
        ''',
        className='fw-light'
    )
]

eol_regional_mix = [
    dbc.Label(
        'End-of-life Regional Mix',
        class_name='fs-5 fw-bold my-2'
    ),
    dcc.Markdown(
        '''
        Using open source data from the University of Washington team, the end-of-life
        impacts would reflect those specific region selected by the user. This
        would affect both the transportation in that region and the custom
        mixes that occur in different landfills across the country.
        ''',
        className='fw-light'
    )
]

eol_custom_full_building_mix = [
    dbc.Label(
        'Custom Mix (full building)',
        class_name='fs-5 fw-bold my-2'
    ),
    dcc.Markdown(
        '''
        A user would be able to choose a specific mix of landfilling, incineration, and
        recycling that would be applied to the whole building.
        ''',
        className='fw-light'
    )
]

eol_custom_component_mix = [
    dbc.Label(
        'Custom Mix (component)',
        class_name='fs-5 fw-bold my-2'
    ),
    dcc.Markdown(
        '''
        A user would be able to choose a specific mix of landfilling, incineration, and
        recycling that would be applied to a particular material.
        ''',
        className='fw-light'
    )
]

transportation_descriptions = (
    default_transportation
    + domestic_supply_chain
    + global_supply_chain
    + intentional_sourcing
)

construction_descriptions = (
    default_construction
    + advanced_waste_recovery
)

replacement_descriptions = (
    default_replacement
    + rics
    + intentional_replacement
)

eol_descriptions = (
    default_eol
    + eol_regional_mix
    + eol_custom_full_building_mix
    + eol_custom_component_mix
)

description_map = {
    'Transportation': transportation_descriptions,
    "Construction": construction_descriptions,
    'Replacement': replacement_descriptions,
    'End-of-life': eol_descriptions
}
