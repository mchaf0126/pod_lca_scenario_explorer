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
                        dcc.Markdown(
                            '''
                            #### Milestone M3.3, Due Q10 - January 24, 2025
                            '''
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
                        dcc.Markdown(
                            '''
                            #### Scenario Explorer Goals & Structure
                            '''
                        ),
                        dcc.Markdown(
                            '''
                            The POD|LCA WBLCA Scenario Explorer is made from a set of structured
                            WBLCA template models with pre-built scenarios. The tool allows users
                            to enter project information and explore changes to the model results
                            related to specific scenarios and methodological decisions.

                            This version, currently in development, is a POC model that will allow
                            us to continue to develop background data infrastructure and model code
                            base for the future POD LCA tools. For M3.3 Milestone we are proposing
                            to create a fully functional model along with updated documentation and
                            datasets for use by our internal tool development & framework team.
                            ''',
                            className='fw-light'
                        ),
                        html.Br(),
                        dcc.Markdown(
                            '''
                            #### About the dashboard
                            '''
                        ),
                        dcc.Markdown(
                            '''
                            At present, the dashboard is in beta. There are
                            currently two types of pages of note:
                            *  **Template Model Selection** - a page to select the template model
                            to be compared against.
                            *  **Novel Material Definition** - a page to define and apply a novel material 
                            to the template model for analysis.


                            An additional section of the dashboard will facilitate the results of the template
                            model in a format to show the different impacts of individual scenarios (Scenario 
                            Explorer) and a way to see the combination of scenarios and their impact on the
                            template model (Model Comparison). These are still in development.
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
