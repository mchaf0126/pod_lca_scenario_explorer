---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Homepage

## Milestone Description <a href="#milestone-description" id="milestone-description"></a>

> “Delivery of structured cradle-to-grave WBLCA template models with modeled scenarios to compare at least five mid/endpoint impact categories including GWP/climate change, dynamic impacts over the lifetime of the building, supply chain impacts including land use / land use change of input materials, and end-of-life impacts of HESTIA building designs to those of conventional building practice/assemblies/materials.”

## Scenario Explorer Goals & Structure <a href="#scenario-explorer-goals-structure" id="scenario-explorer-goals-structure"></a>

The POD|LCA WBLCA Scenario Explorer is made from a set of structured WBLCA template models with pre-built scenarios. The tool allows users to enter project information and explore changes to the model results related to specific scenarios and methodological decisions.

This version, currently in development, is a proof-of-concept model that will allow us to continue to develop background data infrastructure and model code base for future POD LCA tools. At the time of submission of Milestone 3.3, the team aims to have a fully functional model along with updated documentation and datasets for use by our internal tool development & framework team.

The models currently included in the Scenario Explorer represent cradle-to-grave prototype models for evaluating impacts over the lifetime of the building, inclusive of building materials, processes, and energy. The team has constructed two reference buildings, one commercial office building, and one single-family residential house. In accordance with the POD|LCA Modeling Framework Part B, both models cover the following minimum scope:

* **Building elements:** Structure and enclosure are included in the base model scope. For the residential model, some interior materials have also been included. MEP and site elements are excluded from both models.
* **Life cycle stages:** Modules A-C, including operational and embodied emissions, are reported for both models. For a detailed description of the processes and flows included per life cycle stage, see M1.6 Draft LCA Modeling Framework Part B: Buildings Report.
* **Impact categories:** The five core TRACI 2.1 impact categories (global warming potential, ozone depletion potential, acidification potential, eutrophication potential, and smog formation potential) are included and reported separately. The model reports carbon emissions from fossil and biogenic sources separately.
* **Stored carbon:** Biogenic carbon storage is reported as an inventory metric for all bio-based materials in the template models and is enabled as a manual input for novel materials or assemblies.

## About the Scenario Explorer <a href="#about-the-dashboard" id="about-the-dashboard"></a>

At present, the Scenario Explorer consists of four unique pages:

* **Template Model Selection:** The first page of the proof-of-concept model allows the user to select the template model for analysis. There are over 60 models to choose from based on selections of building use type, structural material, and enclosure design options. The page also provides a summary of results for the given template model.
* **Novel Material Selection:** Here, a proof-of-concept display is shown for how the user would implement novel materials into the Scenario Explorer. This page currently only shows the intent of novel material selection.
* **Scenario Explorer:** This page provides the selection of scenarios for a given life cycle stage. At present, transportation, construction, and replacement scenarios are functional and show the change in environmental impacts for various scenarios. These scenarios are described below the main graphs.
* **Model Comparison:** Finally, this page allows users to compare the impact of scenarios on the **whole** life cycle assessment of the template model. Here, a collection of scenarios can be selected and compared to the default template model selected on the **Template Model Selection** page.

## Jump right in

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Template Model</strong></td><td>Share your docs online</td><td><a href=".gitbook/assets/3.png">3.png</a></td><td></td><td><a href="broken-reference">Broken link</a></td></tr><tr><td><strong>Results</strong></td><td>Create your first site</td><td><a href=".gitbook/assets/1.png">1.png</a></td><td></td><td><a href="broken-reference">Broken link</a></td></tr><tr><td><strong>Scenarios</strong></td><td>Learn the basics of GitBook</td><td><a href=".gitbook/assets/2.png">2.png</a></td><td></td><td><a href="broken-reference">Broken link</a></td></tr></tbody></table>
