from dash import dcc

domestic_supply_chain = dcc.Markdown(
    '''
    #### Domestic Supply Chain
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure do mollit anim id est laborum.
    ''',
    className='fw-light'
)

global_supply_chain = dcc.Markdown(
    '''
    #### Global Supply Chain
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure do mollit anim id est laborum.
    ''',
    className='fw-light'
)

intentional_sourcing = dcc.Markdown(
    '''
    #### Intentional Sourcing
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure do mollit anim id est laborum.
    ''',
    className='fw-light'
)

advanced_waste_recovery = dcc.Markdown(
    '''
    #### Advanced Waste Recovery
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure do mollit anim id est laborum.
    ''',
    className='fw-light'
)

offsite_fabrication = dcc.Markdown(
    '''
    #### Off-site Fabrication
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure do mollit anim id est laborum.
    ''',
    className='fw-light'
)

Rics = dcc.Markdown(
    '''
    #### RICS Replacement Rates
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure do mollit anim id est laborum.
    ''',
    className='fw-light'
)

Ashrae_240 = dcc.Markdown(
    '''
    #### ASHRAE 240 Replacement Rates
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure do mollit anim id est laborum.
    ''',
    className='fw-light'
)

eol_regional_mix = dcc.Markdown(
    '''
    #### End-of-life Regional Mix
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure do mollit anim id est laborum.
    ''',
    className='fw-light'
)

description_map = {
    'domestic_supply_chain': domestic_supply_chain,
    'global_supply_chain': global_supply_chain,
    'Intentional Sourcing': intentional_sourcing,
    'Advanced Waste Recovery': advanced_waste_recovery,
    'Off-site Fabrication': offsite_fabrication,
    'RICS': Rics,
    'ASHRAE_240': Ashrae_240,
    'regional_mix': eol_regional_mix
}

description_list = [
    'domestic_supply_chain',
    'global_supply_chain',
    'Intentional Sourcing',
    'Advanced Waste Recovery',
    'Off-site Fabrication',
    'RICS',
    'ASHRAE_240',
    'regional_mix'
]
