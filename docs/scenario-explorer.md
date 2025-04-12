---
icon: binoculars
---

# Scenario Explorer

## Description

The scenario explorer page allows the user to investigate the environmental impacts of the template model for different scenarios. In the context of this tool, a scenario can be defined as a set of assumptions that allow the tool to calculate environmental impacts. There are two types of scenarios that the tool employs:&#x20;

* Prebuilt - These scenarios apply to all materials in the tool. They are coarse, but useful assumptions that can provide insight specific design decisions.
* Custom - These scenarios apply a user-defined decision to one component in the tool. These are more specific and can provide a more exact approach to decision-making.&#x20;

Each of these scenarios is visualized per life cycle stage selected. See below for a full round-up of the scenarios in the tool.

## Transportation Scenarios

### **North American Average Transportation distance -** Default&#x20;

Typical transportation distances and emissions based on North American production. This scenario is based on the ASHRAE/ICC 240P Standard, including default transportation modes and distances.

### Prebuilt Scenarios

**Regionally-specific Average Transport distance** - Using the US National Commodity Flow Survey (CFS), the distances used for materials would reflect those traveled in the specific region selected by the user.

**Global Supply Chain** - Using a globally-focused data source, a more generalized transportation distance and emission factors materials would be used to reflect sourcing from outside of the country. NOT CURRENTLY IMPLEMENTED

### Custom Scenarios

**Intentional Sourcing** - In this custom scenario, a user can choose a specific material, transport mode, and distance to calculate A4 emissions for that material

## Construction Scenarios

### North American Average **-** Default&#x20;

This scenario reflects default values for material-specific wastage rates based on ASHRAE/ICC 240P Standard. This scenario currently does not include construction activities.

### Prebuilt Scenarios

**"Enhanced Waste Management" -** This scenario represents increased diversion of C\&D waste materials aligned with LEED v4 waste management credit.

### Custom Scenarios

**Off-site Fabrication -** This custom scenario would allow users to input custom information on construction processes/fuels and wastage rates reflective of a specific offsite facility. THIS IS NOT YET IMPLEMENTED

## Replacement Scenarios

### Typical Replacement Rates **-** Default&#x20;

This scenario reflects typical replacement for North American construction based on ASHRAE/ICC 240P Standard.&#x20;

### Prebuilt Scenarios

**RICS Replacement Rates -** This scenario reflects typical replacement for commercial buildings based on RICS whole life carbon assessment (WLCA) standard, 2nd edition.

**Range of potential replacement rates** - This scenario would show a range of potential impacts based on the likeliness of replacing a building component. Scenario could be calibrated the reflect low replacement and high replacement scenarios per building type. NOT CURRENTLY IMPLEMENTED

### Custom Scenarios

**Intentional Replacement -** A user would be able to choose a specific material and a replacement year in order to recalculate emissions for that material.

## Energy Use Scenarios

### Default Energy Use with Regional Grid mix&#x20;

This scenario represents building performance that meets the minimum requirements of building code and pulls emissions from the typical grid mix for the building location.

### Prebuilt Scenarios

**All-electric building with regional grid mix** - This scenario represents an all-electric building and pulls entirely from the local grid mix with no on-site fossil fuel combustion NOT CURRENTLY IMPLEMENTED

### Custom Scenarios

**Default energy use with Custom Grid Mix -** This scenario represents building performance that represents typical building performance and systems design based on CBEX database but allows users to set a specific grid mix for the project. NOT CURRENTLY IMPLEMENTED

## End-of-life Scenarios

### National Ave C\&D treatment mix - Default

This scenario represents emissions associated with national average construction and demolition waste treatment scenarios as established by the US EPA.

### Prebuilt Scenarios

**Regional C\&D treatment mix** - This scenario represents emissions associated with regional averages for construction and demolition waste treatment as established by the US EPA. NOT CURRENTLY IMPLEMENTED

### Custom Scenarios

**Custom EoL Mix (for entire building) -** This scenario allows a user to create a custom scenario with a specific mix of end-of-life treatments (percent of waste sent to landfill, incineration, and recycling) or the entire building. NOT CURRENTLY IMPLEMENTED

**Custom EoL Mix (for single element)** - This scenario allows a user to create a custom scenario with a specific mix of end-of-life treatments (percent of waste sent to landfill, incineration, and recycling) for a specific material or assembly type (e.g., wood, metals or prefabricated elements). NOT CURRENTLY IMPLEMENTED
