RICS_service_life:
------------------

service life -  in years; 60+ indicating building lifespan

RICS_mapper
-----------
Use Revit Category as an extra category to map. e.g., 'Steel, reinforcing rod' would not have been mapped without the extra category.
[Revit category are built into Revit and are intuitive building assemblies
https://www.autodesk.com/support/technical/article/caas/tsarticles/ts/40TllwlxZoInjymoTI0lkB.html#:~:text=Model%20elements-,Revit%20categories,to%20behave%20in%20a%20project.]

from Template model: 	Material Name => material_type (in RICS_mapper)
			Revit category => assembly (in RICS_mapper)

Clarification needed:
- ids 7-9, 11 ---are these integral to the floor or the finishes (i.e., therefore be classified 'Superstructure: Structural elements' or 'Floor finishes'
- ids 18-25 ---are these fascade or internal partitioning? Are these structural walls (Assume that 16 and 17 are structural walls)


ASHRAE_service_life:
--------------------

service life -  in years; 60+ indicating building lifespan
TODO: Double check type with OmniClass table 21 


ASHRAE_mapper
-------------
10/15/2024: NO ASHRAE mapper required. REVIT models will be built with OmniClass Level 3, which is used in ASHRAE Service live