from dash import dcc

default_transportation = dcc.Markdown(
    '''
    #### North American Average (default)
    Typical transportation distances and emissions based on North American production.
    This scenario is based on the ASHRAE/ICC 240P Standard, including default transportation modes and distances.
    Calculation of impacts includes a return trip factor for trips longer than 500 miles.
    ''',
    className='fw-light'
)

domestic_supply_chain = dcc.Markdown(
    '''
    #### Regionally-Specific Distances
    This scenario uses the US Commodity Flow Survey to derive transportation distances
    for a specific consumption region for a specific material category as selected by the user.
    ''',
    className='fw-light'
)

global_supply_chain = dcc.Markdown(
    '''
    #### Global Supply Chain
    Using a globally focused data source, a more generalized distance for materials would
    be used to reflect sourcing from outside of the country.
    ''',
    className='fw-light'
)

intentional_sourcing = dcc.Markdown(
    '''
    #### Intentional Sourcing
    In this custom scenario, a user can choose a specific material, transport mode, and
    distance to calculate transportation emissions for that material.
    ''',
    className='fw-light'
)

default_construction = dcc.Markdown(
    '''
    #### North American Average (default)
    This scenario reflects default values for material-specific wastage rates based on
    ASHRAE/ICC 240P Standard.  This scenario currently does not include construction activities.
    ''',
    className='fw-light'
)

advanced_waste_recovery = dcc.Markdown(
    '''
    #### Advanced Waste Recovery
    This scenario represents practices for construction waste management, such as
    increased diversion of C&D waste materials compliant with the LEED v4 waste
    management credit.
    ''',
    className='fw-light'
)

default_replacement = dcc.Markdown(
    '''
    #### Typical Replacement Rates (default)
    This scenario reflects typical replacement for North American construction
    based on ASHRAE/ICC 240P Standard.
    ''',
    className='fw-light'
)

rics = dcc.Markdown(
    '''
    #### RICS Replacement Rates
    This scenario reflects replacement for construction based on the
    RICS whole life carbon assessment (WLCA) standard, 2nd edition.
    ''',
    className='fw-light'
)

default_eol = dcc.Markdown(
    '''
    #### National Average C&D Treatment Mix (default)
    Typical end-of-life impacts based on North American average production data.
    ''',
    className='fw-light'
)

eol_regional_mix = dcc.Markdown(
    '''
    #### End-of-life Regional Mix
    Using open source data from the University of Washington team, the end-of-life
    impacts would reflect those specific region selected by the user. This
    would affect both the transportation in that region and the custom
    mixes that occur in different landfills across the country.
    ''',
    className='fw-light'
)

eol_custom_full_building_mix = dcc.Markdown(
    '''
    #### Custom Mix (full building)
    A user would be able to choose a specific mix of landfilling, incineration, and
    recycling that would be applied to the whole building.
    ''',
    className='fw-light'
)

eol_custom_component_mix = dcc.Markdown(
    '''
    #### Custom Mix (for component)
    A user would be able to choose a specific mix of landfilling, incineration, and
    recycling that would be applied to a particular material.
    ''',
    className='fw-light'
)

transportation_descriptions = [
    default_transportation,
    domestic_supply_chain,
    global_supply_chain,
    intentional_sourcing
]

construction_descriptions = [
    default_construction,
    advanced_waste_recovery
]

replacement_descriptions = [
    default_replacement,
    rics
]

eol_descriptions = [
    default_eol,
    eol_regional_mix,
    eol_custom_full_building_mix,
    eol_custom_component_mix
]

description_map = {
    'Transportation': transportation_descriptions,
    "Construction": construction_descriptions,
    'Replacement': replacement_descriptions,
    'End-of-life': eol_descriptions
}
