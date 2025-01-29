from pathlib import Path
from dash import html, dcc, register_page
import dash_bootstrap_components as dbc


register_page(__name__, path='/')

current_file_path = Path(__file__)
main_directory = current_file_path.parents[2]

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label(
                            'Milestone M3.3, Due Q10 - January 24, 2025',
                            class_name='fs-5 fw-bold my-2'
                        ),
                        dcc.Markdown(
                            '''
                            “Delivery of structured cradle-to-grave WBLCA template models
                            with modeled scenarios to compare at least five mid/endpoint impact
                            categories including GWP/climate change, dynamic impacts over the
                            lifetime of the building, supply chain impacts including land use /
                            land use change of input materials, and end-of-life impacts of HESTIA
                            building designs to those of conventional
                            building practice/assemblies/materials.”
                            ''',
                            className='fw-light'
                        ),
                        html.Br(),
                        dbc.Label(
                            'Scenario Explorer goals & structure',
                            class_name='fs-5 fw-bold my-2'
                        ),
                        dcc.Markdown(
                            '''
                            The POD|LCA WBLCA Scenario Explorer is made from a set of structured
                            WBLCA template models with pre-built scenarios. The tool allows users
                            to enter project information and explore changes to the model results
                            related to specific scenarios and methodological decisions.

                            This version, currently in development, is a proof-of-concept model that
                            will allow us to continue to develop background data infrastructure and
                            model code base for future POD LCA tools. At the time of submission of
                            Milestone 3.3, the team aims to have a fully functional model along with
                            updated documentation and datasets for use by our internal tool
                            development & framework team.

                            The models currently included in the Scenario Explorer represent
                            cradle-to-grave prototype models for evaluating impacts over the
                            lifetime of the building, inclusive of building materials, processes,
                            and energy. The team has constructed two reference buildings, one
                            commercial office building, and one single-family residential house.
                            In accordance with the POD|LCA Modeling Framework Part B,
                            both models cover the following minimum scope:

                            - __Building elements:__ Structure and enclosure are included in the
                            base model scope. For the residential model, some interior materials
                            have also been included. MEP and site elements are excluded from
                            both models. 
                            - __Life cycle stages:__ Modules A-C, including operational and
                            embodied emissions, are reported for both models. For a detailed
                            description of the processes and flows included per life cycle stage,
                            see M1.6 Draft LCA Modeling Framework Part B: Buildings Report.
                            - __Impact categories:__ The five core TRACI 2.1 impact categories
                            (global warming potential, ozone depletion potential, 
                            acidification potential, eutrophication potential, and
                            smog formation potential) are included and reported separately.
                            The model reports carbon emissions from fossil and biogenic
                            sources separately.
                            - __Stored carbon:__ Biogenic carbon storage is reported as an
                            inventory metric for all bio-based materials in the template models
                            and is enabled as a manual input for novel materials or assemblies.
                            ''',
                            className='fw-light'
                        ),
                        html.Br(),
                        dbc.Label(
                            'About the Scenario Explorer',
                            class_name='fs-5 fw-bold my-2'
                        ),
                        dcc.Markdown(
                            '''
                            At present, the Scenario Explorer consists of four unique pages:
                            - __Template Model Selection:__ The first page of the proof-of-concept model
                            allows the user to select the template model for analysis. There are
                            over 60 models to choose from based on selections of building use
                            type, structural material, and enclosure design options. The page
                            also provides a summary of results for the given template model.
                            - __Novel Material Selection:__ Here, a proof-of-concept display is shown
                            for how the user would implement novel materials into the Scenario
                            Explorer. This page currently only shows the intent of novel material
                            selection.
                            - __Scenario Explorer:__ This page provides the selection of scenarios
                            for a given life cycle stage. At present, transportation, construction,
                            and replacement scenarios are functional and show the change in
                            environmental impacts for various scenarios. These scenarios are
                            described below the main graphs.
                            - __Model Comparison:__ Finally, this page
                            allows users to compare the impact of scenarios on the __whole__
                            life cycle assessment of the template model. Here, a collection of scenarios
                            can be selected and compared to the default template model selected on the
                            __Template Model Selection__ page.
                            ''',
                            className='fw-light'
                        ),
                    ],
                    width={"size": 8},
                    class_name='pe-5'
                ),
            ],
            justify='center',
            className='m-2'
        ),
    ]
)
